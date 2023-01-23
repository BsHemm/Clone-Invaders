import pygame
import sys
import game_state
from bullet_char import Projectile
from Game_Over import Game_Over

from pygame.sprite import Sprite
from pygame.locals import *
from constants import WIDTH,HEIGHT

class Gun_char(Sprite):
    def __init__ (self, ):
        super(). __init__ ()
        self.image=pygame.surface.Surface((64,64))
        self.image.fill((0, 0, 93))

        self.rect = self.image.get_rect(center = (WIDTH / 2, HEIGHT / 1))
        self.shooting=False
        #health
        self.health=2
        health=self.health
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
                    enemy_ships = game_state.enemy_ships
                )
                game_state.all_sprites.add(bullet)
        else: self.shooting=False 

        # if self.health <=0:
        #     g=Game_Over(x=WIDTH/2,y=HEIGHT/2,all_sprites=all_sprites)
        #     all_sprites.add(g)

        if pressed_keys[K_k]:
            if self.dead==False:
                self.dead=True
