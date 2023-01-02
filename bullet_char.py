import pygame
import sys

from pygame.sprite import Sprite
from pygame.locals import *
from constants import WIDTH,HEIGHT

#Gun_Char's projectile.
class Projectile(Sprite):
    def __init__(self,x,y,enemy_ships):
        super(). __init__ ()
    # def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        # self.radius = radius
        self.image=pygame.surface.Surface((10,20))
        self.image.fill((73, 0, 200))
        self.rect=self.image.get_rect(center=(self.x, self.y))
        self.enemy_ships = enemy_ships
        # self.facing = facing
        # self.vel = 8 * facing
        #damage value on collision?
    def update (self):
        self.rect.y-=5
        #hit detetction
        hits = pygame.sprite.spritecollide(self , self.enemy_ships, True)
        if hits:
            self.kill()
        #     self.health-=1
        # if self.health >=0:pass
        #     #enemy despawns