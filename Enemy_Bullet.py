import pygame
import game_state
from pygame.sprite import Sprite
#Enemy_b's projectile.
class Missile(Sprite):
    def __init__(self,x,y):
        super(). __init__ ()
    # def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        # self.radius = radius
        self.image=pygame.surface.Surface((10,20))
        self.image.fill((255, 165, 0))
        self.rect=self.image.get_rect(center=(self.x, self.y))
        # self.enemy_ships = enemy_ships
        # self.facing = facing
        # self.vel = 8 * facing
        #damage value on collision?
    def update (self):
        self.rect.y+=5
        # #hit detetction
        hits = pygame.sprite.spritecollide(self , game_state.gun_chars, True)
        if hits:
             self.kill()
        