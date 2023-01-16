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

import game_state

pygame.init() #background engines
vec = pygame.math.Vector2  # 2 for two dimensional
 

clock = pygame.time.Clock()
#pre-game loop, "monitor"
displaysurface = pygame.display.get_surface()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clone Invaders")


g=Game_Over(x=WIDTH/2,y=HEIGHT/2)
game_state.game_over_sprites.add(g)


def reset_game():
    game_state.game_over = False
    game_state.all_sprites.empty()
    game_state.enemy_ships.empty()

    # GUN_char instance
    gun_char=Gun_char()
    game_state.all_sprites.add(gun_char)
    #define Gun_char health? INstance?
    #enemy creation arrangemnt loopS
    for x in range(50,WIDTH-200,75):
        for y in range(50,HEIGHT-375,75):

            #enemies INstances
            # enemy_a=Enemy_A(x*75,50)
            enemy=Enemy_B(x,y)
            game_state.all_sprites.add(enemy)
            game_state.enemy_ships.add(enemy)

    #Lose conditions; conditions that make teh game over screen come up
    #press p (applied), endzone crossed ( not applied), player loses all health (not applied)
    #enemy crosses into endzone
    #gunchar health is <=0


reset_game()
        
#game loop
while True:
    while not game_state.game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_p]:
            game_state.game_over = True

        game_state.all_sprites.update()
        if armada.hit_wall:
            armada.direction=-armada.direction
            armada.reset()
            for ship in game_state.enemy_ships:
                ship.rect.y +=50 
        #lose conditions
        #if player_health <=0:
            #player_health=-player_health
            #im = Image.open("bear.png")
            #im.show()

        displaysurface.fill((0,0,0))
        game_state.all_sprites.draw(displaysurface)
        pygame.display.update()
        clock.tick(FPS)


    while game_state.game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RETURN]:
            reset_game()

        displaysurface.fill((0,0,0))
        game_state.game_over_sprites.draw(displaysurface)
        pygame.display.update()
        clock.tick(FPS)
