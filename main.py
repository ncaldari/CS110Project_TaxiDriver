import pygame
import random
from classes import Taxi, Obstacle, Lane
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

'''
gameObjs = {}
gameObjs['mytaxi'] = Taxi()
gameObjs['obstacle'] = Obstacle(0,10)
gameObjs['obstacle2'] = Obstacle(0,10)
objectList = pygame.sprite.Group()
objectList.add(gameObjs['mytaxi'])
obstacleList = pygame.sprite.Group()
obstacleList.add(gameObjs['obstacle'])
obstacleList.add(gameObjs['obstacle2'])
'''



def exit_menu():
    font = pygame.font.SysFont(None, 50)
    gameoverExit = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Taxi Driver Game Over')
    text_objects3 = font.render("Game Over", True, green)
    gameoverExit.blit(text_objects3, [150, 100])
    gameoverGetOut = False
    while not gameoverGetOut:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameoverGetOut = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameoverGetOut = True
                    #main()
                    #gamestartExit = True
                    startGame()

        pygame.display.flip()


def game_loop():
    gameObjs = {}
    gameObjs['mytaxi'] = Taxi()
    gameObjs['obstacle'] = Obstacle(0,10)
    gameObjs['obstacle2'] = Obstacle(0,10)
    objectList = pygame.sprite.Group()
    objectList.add(gameObjs['mytaxi'])
    obstacleList = pygame.sprite.Group()
    obstacleList.add(gameObjs['obstacle'])
    obstacleList.add(gameObjs['obstacle2'])

    game_over = False
    running = True
    mytaxi = gameObjs['mytaxi']
    obstacles = gameObjs['obstacle']
    obstacles2 = gameObjs['obstacle2']
    score = 0
    mylane0 = Lane(130)
    mylane = Lane(230)
    mylane2 = Lane(330)
    mylane3 = Lane(430)


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
        score = score + 1
        if score % 50 == 0:
            print(score)

        pygame.draw.rect(screen, yellow, mylane.rect)
        pygame.draw.rect(screen, yellow, mylane2.rect)
        pygame.draw.rect(screen, yellow, mylane0.rect)
        pygame.draw.rect(screen, yellow, mylane3.rect)
        objectList.draw(screen)
        obstacleList.draw(screen)

        obstacles.update()
        obstacles2.update()
        if pygame.sprite.spritecollide(mytaxi, obstacleList, True):
            game_over = True
            exit_menu()
        pygame.display.flip()

def startGame():
    #global running, gameObjs
    startView = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Taxi Driver Start Menu')
    font = pygame.font.SysFont(None, 50)
    font3 = pygame.font.SysFont(None, 30)
    text_objects = font.render("Taxi Driver", True, yellow)
    text_objects2 = font.render("Press Space Bar to Start", True, yellow)
    text_objects3 = font3.render("Left Key: Move Left, Right Key: Move Right", True, blue)
    text_objects4 = font3.render("Don't Crash", True, blue)
    startView.blit(text_objects, [150, 100])
    startView.blit(text_objects2, [50, 300])
    startView.blit(text_objects3, [40, 200])
    startView.blit(text_objects4, [180, 230])

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

def main():
    startGame()
main()




