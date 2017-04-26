import pygame
import random
from classes import Taxi, Obstacle
import pygame.font
import sys

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,220,0)
yellow = (245, 225, 0)

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
FPS = 60

gameObjs = {}
gameObjs['mytaxi'] = Taxi()
gameObjs['obstacle'] = Obstacle(0,10)
objectList = pygame.sprite.Group()
objectList.add(gameObjs['mytaxi'])
objectList.add(gameObjs['obstacle'])

def game_loop():
    global running, gameObjs
    game_over = False
    running = True
    mytaxi = gameObjs['mytaxi']
    obstacles = gameObjs['obstacle']
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mytaxi.move('left')
                if event.key == pygame.K_RIGHT:
                    mytaxi.move('right')
        screen.fill(black)
        #pygame.draw.rect(screen, blue, mytaxi.rect)
        objectList.draw(screen)
        obstacles.update()
        pygame.display.flip()
game_loop()
