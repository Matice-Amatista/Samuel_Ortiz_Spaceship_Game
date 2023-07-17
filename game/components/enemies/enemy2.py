import pygame

from random import randint

from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1,ENEMY_2,SHIP_WIDTH,SHIP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy2(Sprite):
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X ={0 : 'left', 1 :'rigth'}
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH,SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,SCREEN_WIDTH)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[randint(0,1)]
        self.move_x_for = randint(30, 40)
        self.step = 0
    

    def update(self, enemies):
        self.rect.y += self.speed_y
        if self.movement_x =='left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movemet_x()

        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)
            print("enemies 2 : " + str(len(enemies)))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_movemet_x(self):
        self.step += 1
        if  (self.step >= self.move_x_for and self.movement_x == 'rigth') or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
                self.movement_x = 'left'
                self.step = 0


        elif  (self.step >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <=10):
                self.movement_x = 'rigth'
                self.step = 0