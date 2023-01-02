#Space invaders clone By Way Of Pygame
import pygame
import sys
#gun character
from gun_char import Gun_char
#Enemies
from enemy_B import Enemy_B, armada
from Game_Over import Game_Over
#sprites
from pygame.sprite import Sprite
#some variables
from pygame.locals import *
from constants import WIDTH,HEIGHT,FPS

pygame.init() #background engines
vec = pygame.math.Vector2  # 2 for two dimensional
 

clock = pygame.time.Clock()
#pre-game loop, "monitor"
displaysurface = pygame.display.get_surface()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clone Invaders")

#sprite Group
all_sprites = pygame.sprite.Group()
enemy_ships=pygame.sprite.Group() 

# GUN_char instance
gun_char=Gun_char(all_sprites,enemy_ships)
all_sprites.add(gun_char) 
#enemy creation arrangemnt loopS
for x in range(50,WIDTH-200,75):
    for y in range(50,HEIGHT-375,75):

        #enemies INstances
        # enemy_a=Enemy_A(x*75,50,all_sprites)
        enemy=Enemy_B(x,y,all_sprites)
        all_sprites.add(enemy)
        enemy_ships.add(enemy)

#Lose conditions; conditions that make teh game over screen come up

#endzone is the bottom of the screen that when crossed by an enemy causes lose condition
#endZone Instance

#endzone Creation
#endzone<=Height-475

#player death is when Gun_Char loses all health, causing Lose condition

#game over Screen Instance
# game_over=Game_Over(all_sprites,enemy_ships)
# all_sprites.add(gun_char) 

#game over screen Creation
# for x in range(50,WIDTH-200,75):
#     for y in range(50,HEIGHT-375,75):

        #GAme over INstances
        # game_over=Game_Over(x,y,all_sprites)
        # all_sprites.add(game_over)
        #enemy_ships.add(enemy_a)
#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_p]:
        g=Game_Over(x=WIDTH/2,y=HEIGHT/2,all_sprites=all_sprites)
        all_sprites.add(g)
        

    all_sprites.update()
    if armada.hit_wall:
        armada.direction=-armada.direction
        armada.reset()
        for ship in enemy_ships:
            ship.rect.y +=50 
    #lose conditions
    #if player_health <=0:
        #player_health=-player_health
        #im = Image.open("bear.png")
        #im.show()

    displaysurface.fill((0,0,0))
    all_sprites.draw(displaysurface)
    pygame.display.update()
    clock.tick(FPS)