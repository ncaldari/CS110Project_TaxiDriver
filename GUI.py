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
        objectList.draw(screen)
        obstacles.update()
        pygame.display.flip()

def startGame():
    startView = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Taxi Driver Start Menu')
    font = pygame.font.SysFont(None, 50)
    text_objects = font.render("Taxi Driver", True, yellow)
    text_objects2 = font.render("Press Space Bar to Start", True, green)
    startView.blit(text_objects, [150, 100])
    startView.blit(text_objects2, [40, 300])

    gamestartExit = False
    while not gamestartExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestartExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestartExit = True
                    game_loop()
        pygame.display.flip()
startGame()


# def on_loop():
#     global gameObjs, score, maxScore
#     mytaxi = gameObjs['mytaxi']
#     obstacles = gameObjs['obstacle']


#
#
# class Taxidriver:
#     def __init__(self):
#         #pygame.init()
#
#         mytaxi = Taxi()
#         #myobstacle = Obstacle()
#         #myobstacle2 = Obstacle()
#
#         self.startView = pygame.display.set_mode((500,500))
#         pygame.display.set_caption('Taxi Driver Start Menu')
#         font = pygame.font.SysFont(None, 50)
#         text_objects = font.render("Taxi Driver", True, yellow)
#         text_objects2 = font.render("Press Space Bar to Start", True, green)
#         self.startView.blit(text_objects, [150, 100])
#         self.startView.blit(text_objects2, [40, 300])
#         gamestartExit = False
#         while not gamestartExit:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     gamestartExit = True
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         gamestartExit = True
#
#                         #self.gameView = pygame.display.set_mode((500,500))
#                         pygame.display.set_caption('Taxi Driver')
#                         gameExit = False
#                         while not gameExit:
#                             for event in pygame.event.get():
#                                 if event.type == pygame.QUIT:
#                                     gameExit = True
#                                 if event.type == pygame.KEYDOWN:
#                                     if event.key == pygame.K_LEFT:
#                                         mytaxi.move('left')
#                                     if event.key == pygame.K_RIGHT:
#                                         mytaxi.move('right')
#
#                             self.startView.fill(black)
#                             # draw it write
#                             pygame.draw.rect(self.startView, blue, mytaxi.rect)
#                             #rect.draw(startView)
#                             pygame.display.flip()
#
#             pygame.display.flip()
#
#
#
#
#
# def main():
#     #mytaxi = taxi.Taxi()
#     Taxidriver()
# main()

