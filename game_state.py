import pygame

#sprite groups
#sprite Group
#any sprites in thsi groupe will be draawn to teh screen
#members of thsi group will be updated once per frame.
all_sprites = pygame.sprite.Group()
#idefntifies whitch sprites to do collision against
enemy_ships=pygame.sprite.Group() 
#opposing sprite collision detection group
gun_chars=pygame.sprite.Group()
