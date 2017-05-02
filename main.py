import pygame
import random
import json
from classes import Taxi, Obstacle, Lane
import pygame.font
import sys

pygame.init()

yellow = (245, 225, 0)
black = (0,0,0)
green = (0,220,0)
blue = (0,0,255)
class Taxidriver:

    def exit_menu(self,score, highscore):

        font = pygame.font.SysFont(None, 50)
        self.gameoverExit = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Taxi Driver Game Over')
        text_objects3 = font.render("Game Over", True, yellow)
        text_objects4 = font.render('Score: ' + str(score), True, yellow)
        text_objects5 = font.render('Play Again? Hit Space.', True, yellow)
        text_objects6 = font.render("HighScore: " + str(highscore), True, yellow)
        self.gameoverExit.blit(text_objects3, [150, 100])
        self.gameoverExit.blit(text_objects4, [160, 200])
        self.gameoverExit.blit(text_objects5, [60, 400])
        self.gameoverExit.blit(text_objects6, [120, 300])
        gameoverGetOut = False
        while not gameoverGetOut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameoverGetOut = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameoverGetOut = True
                        Taxidriver.startGame(self)

            pygame.display.flip()


    def game_loop(self):

        self.screen = pygame.display.set_mode((500,500))
        font = pygame.font.SysFont(None, 30)
        pygame.display.set_caption('Taxi Driver')

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
            text_objects4 = font.render('Score: ' + str(score), True, green)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mytaxi.move('left')
                    if event.key == pygame.K_RIGHT:
                        mytaxi.move('right')
            self.screen.fill(black)
            score = score + 1

            pygame.draw.rect(self.screen, yellow, mylane.rect)
            pygame.draw.rect(self.screen, yellow, mylane2.rect)
            pygame.draw.rect(self.screen, yellow, mylane0.rect)
            pygame.draw.rect(self.screen, yellow, mylane3.rect)
            objectList.draw(self.screen)
            obstacleList.draw(self.screen)

            obstacles.update()
            obstacles2.update()
            if pygame.sprite.spritecollide(mytaxi, obstacleList, True):

                jfile = open('high_score.json', 'r')
                jstr = jfile.read()
                jdictionary = json.loads(jstr)

                jfile.close()
                if jdictionary["High_Score"] < score:
                    jfile = open('high_score.json', 'w')
                    jdictionary["High_Score"] = score
                    jstr2 = json.dumps(jdictionary)
                    jfile.write(jstr2)
                    jfile.close()

                game_over = True
                Taxidriver.exit_menu(self, score, jdictionary["High_Score"])

            self.screen.blit(text_objects4, [10, 10])
            pygame.display.flip()


    def startGame(self):

        self.startView = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Taxi Driver Start Menu')
        font = pygame.font.SysFont(None, 50)
        font3 = pygame.font.SysFont(None, 30)
        text_objects = font.render("Taxi Driver", True, yellow)
        text_objects2 = font.render("Press Space Bar to Start", True, yellow)
        text_objects3 = font3.render("Left Key: Move Left, Right Key: Move Right", True, blue)
        text_objects4 = font3.render("Don't Crash", True, blue)
        self.startView.blit(text_objects, [150, 100])
        self.startView.blit(text_objects2, [50, 300])
        self.startView.blit(text_objects3, [40, 200])
        self.startView.blit(text_objects4, [180, 230])

        gamestartExit = False
        while not gamestartExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamestartExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gamestartExit = True
                        Taxidriver.game_loop(self)


            pygame.display.flip()

def main():
    T = Taxidriver()
    T.startGame()

main()
