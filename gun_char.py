import pygame
import sys
from bullet_char import Projectile
from Game_Over import Game_Over

from pygame.sprite import Sprite
from pygame.locals import *
from constants import WIDTH,HEIGHT

class Gun_char(Sprite):
    def __init__ (self, all_sprites, enemy_ships):
        super(). __init__ ()
        self.image=pygame.surface.Surface((64,64))
        self.image.fill((0, 0, 93))

        self.rect = self.image.get_rect(center = (WIDTH / 2, HEIGHT / 1))
        self.all_sprites = all_sprites
        self.enemy_ships = enemy_ships
        self.shooting=False
    def update (self):

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.rect.x-=10
            if self.rect.left < 0:
                self.rect.left = 0

        elif pressed_keys[K_RIGHT]:
            self.rect.x+=10
            if self.rect.right >=WIDTH:
                self.rect.right =WIDTH 

        if pressed_keys[K_SPACE]:
            if self.shooting==False:
                self.shooting=True
                bullet=Projectile (
                    x=self.rect.centerx,
                    y=self.rect.y, 
                    enemy_ships = self.enemy_ships
                )
                self.all_sprites.add(bullet)
        else: self.shooting=False 

        if pressed_keys[K_k]:
            if self.dead==False:
                self.dead=True
# #Gun_Char's projectile.
# class projectile(object):
#     def __init__(self,x,y,radius,color,facing):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.image=pygame.surface.Surface((2,8))
#         self.image.fill((73, 0, 0))
#         self.facing = facing
#         self.vel = 8 * facing