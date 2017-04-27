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
gameObjs = {}
gameObjs['mytaxi'] = Taxi()
gameObjs['obstacles'] = []
objectList = pygame.sprite.Group()
objectList.add(gameObjs['mytaxi']
#objectList.add(gameObjs['obstacle'])
def game_loop():
    mytaxi = Taxi()
    obstacles= pygame.sprite.Group()
    score = 0

    for i in range(0,2):
        obstacles.add(spawn_obstacle(10))
        score += 1

    obstacles.update()
    obstacles.draw(screen)

def on_render():
    global objectList, gameObjs, clock, screen
    objectList.update()
    clock.tick(60)
    pygame.display.flip()


def on_event(event):
    if event.type == pygame.QUIT:
        game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mytaxi.move('left')
        if event.key == pygame.K_RIGHT:
            mytaxi.move('right')
        screen.fill(black)
        objectList.draw(screen)
        pygame.display.flip()

def on_execute():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            on_event(event)
        on_render()
        game_loop()
on_execute()
