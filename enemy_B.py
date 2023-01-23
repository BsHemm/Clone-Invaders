import pygame
import sys
import random
import game_state

from Enemy_Bullet import Missile
from pygame.sprite import Sprite
from pygame.locals import *
from constants import WIDTH,HEIGHT
#this Enemy fires projectiles

#armada Def
class Armada:
    def __init__(self):
        self.direction=+10
        self.hit_wall=False
    def reset(self):
        self.hit_wall=False
    def hit(self):
        self.hit_wall=True
#armada instance
armada=Armada()


#enemy_A "sprite"
class Enemy_B(Sprite):
    #constructor
    def __init__(self,x,y):
        super(). __init__ ()
   
     
        self.image = pygame.image.load("enemy_B2.png").convert_alpha()
        # corodinates of the Png
        self.rect = self.image.get_rect(center = (x,y))
       # self.direction = +10
        
        #health
        self.health=2 
        #hitbox 

        #collison values
    
    def update (self):
        #top to bottom
        self.rect.y
        #left to right
        self.rect.x=self.rect.x+armada.direction
        #all_sprites update or "once per screen"
        #did i hit th escreen?
        if self.rect.right >=WIDTH:
            # self.direction=-self.direction
            # self.rect.y +=50
            armada.hit()
        elif self.rect.left <=0:
            # self.direction=-self.direction
            # self.rect.y +=50
            armada.hit()
        #Health vs damage
        # hits = pygame.sprite.spritecollide(self , bullet_char, False)
        # if hits:
        #     self.health-=1
        # if self.health >=0:pass
        #     #enemy despawns
        if random.random()<0.003:
            m = Missile(x=self.rect.x,y=self.rect.y,)
            game_state.all_sprites.add(m)