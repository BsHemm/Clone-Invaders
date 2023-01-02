import pygame
import sys

from pygame.sprite import Sprite
from pygame.locals import *
from constants import WIDTH,HEIGHT

#enemy_A "sprite"
class Game_Over(Sprite):
    #constructor
    def __init__(self,x,y,all_sprites):
        super(). __init__ ()
   
        # self.x = x
        # self.y = y
        
        self.image=pygame.surface.Surface((500,500))
        self.image.fill((0, 0, 0))
        self.image = pygame.image.load("Game_Over.png").convert_alpha()
        # corodinates of the Png
        self.rect = self.image.get_rect(center = (x,y))
       # self.direction = +10
        self.all_sprites = all_sprites
    #def update (self):
    # def update (self):

    #     pressed_keys = pygame.key.get_pressed()
    #     if pressed_keys[K_KP_ENTER]:
    #         #restart game
        