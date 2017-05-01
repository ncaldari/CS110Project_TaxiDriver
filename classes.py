import pygame
import random

class GameObj(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen


        def update(self):
            pass

class Taxi(GameObj):
    def __init__(self):
        super(GameObj,self).__init__()
        self.image = pygame.image.load('Taxi_assets/car5.png')
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()

        self.rect.x = 250
        self.rect.y = 460
        self.pos = 1

    def update(self):
        pass


    def move(self, l_r):
        positions = [150,250,350]
        if l_r == 'left' and self.pos > 0:
            self.pos -= 1
        if l_r == 'right' and self.pos < 2:
            self.pos +=1
        self.rect.x = positions[self.pos]



class Obstacle(GameObj):
    def __init__(self, ypos, vspeed):
        super(GameObj, self).__init__()
        self.image = pygame.image.load('Taxi_assets/car3.png')
        self.image = pygame.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect()

        positions = [150,250,350]
        speeds = [5, 10, 15, 20]
        self.rect.x = random.choice(positions)
        self.rect.y = 0
        self.vspeed = random.choice(speeds)

    def update(self):
        self.rect.y += self.vspeed
        #if self.rect.y > 460:
            #self.kill()
        speeds2 = [15, 20, 25, 30]
        positions2 = [150,250,350]
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.choice(positions2)
            self.vspeed = random.choice(speeds2)

class Lane:
    def __init__(self, xcoor):
        self.xcoor = xcoor
        self.rect = pygame.Rect(xcoor, 0, 2, 500)


