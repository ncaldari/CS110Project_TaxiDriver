import pygame
import random
import json
from classes import Taxi, Obstacle, Lane
import pygame.font

pygame.init()

yellow = (245, 225, 0)
black = (0,0,0)
green = (0,220,0)
blue = (0,0,255)
class Taxidriver:

    def exit_menu(self,score, highscore):
        #setting up the exit_menu screen
        gameoverExit = pygame.display.set_mode((500,500))
        #setting up all the writing on the menu
        font = pygame.font.SysFont(None, 50)
        pygame.display.set_caption('Taxi Driver Game Over')
        game_over_text = font.render("Game Over", True, yellow)
        score_text = font.render('Score: ' + str(score), True, yellow)
        play_again_text = font.render('Play Again? Hit Space.', True, yellow)
        high_score_text = font.render("High Score: " + str(highscore), True, yellow)
        #putting the writing on the screen
        gameoverExit.blit(game_over_text, [150, 100])
        gameoverExit.blit(score_text, [160, 200])
        gameoverExit.blit(play_again_text, [60, 400])
        gameoverExit.blit(high_score_text, [120, 300])
        # a loop for the exit_menu that allows the user quit or play again
        gameoverGetOut = False
        while not gameoverGetOut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameoverGetOut = True
                #if the user hits space it exits the loop and runs the startGame function
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameoverGetOut = True
                        Taxidriver.startGame(self)

            pygame.display.flip()


    def game_loop(self):
        #setting up the game screen
        screen = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Taxi Driver')
        #setting up all the objects and writing
        font = pygame.font.SysFont(None, 30)
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
        mytaxi = gameObjs['mytaxi']
        obstacles = gameObjs['obstacle']
        obstacles2 = gameObjs['obstacle2']
        score = 0
        mylane0 = Lane(130)
        mylane = Lane(230)
        mylane2 = Lane(330)
        mylane3 = Lane(430)
        clock = pygame.time.Clock()
        # the game loop
        while not game_over:
            clock.tick(45)
            score_counter_text = font.render('Score: ' + str(score), True, green)
            # the event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mytaxi.move('left')
                    if event.key == pygame.K_RIGHT:
                        mytaxi.move('right')
            screen.fill(black)
            #accumulating the score, score goes up by 1 every run through the loop
            score = score + 1
            #drawing everything on screen
            pygame.draw.rect(screen, yellow, mylane.rect)
            pygame.draw.rect(screen, yellow, mylane2.rect)
            pygame.draw.rect(screen, yellow, mylane0.rect)
            pygame.draw.rect(screen, yellow, mylane3.rect)
            objectList.draw(screen)
            obstacleList.draw(screen)

            obstacles.update()
            obstacles2.update()
            #detecting a collision between the taxi and an obstacle
            if pygame.sprite.spritecollide(mytaxi, obstacleList, True):
                #using json to keep track of highscore
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
                #exits the loop and calls the exit_menu function after the collision
                game_over = True
                Taxidriver.exit_menu(self, score, jdictionary["High_Score"])

            screen.blit(score_counter_text, [10, 10])
            pygame.display.flip()


    def startGame(self):
        #setting up the startGame menu
        startView = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Taxi Driver Start Menu')
        #setting up all the writing on the menu
        font = pygame.font.SysFont(None, 50)
        font3 = pygame.font.SysFont(None, 30)
        taxi_driver_text = font.render("Taxi Driver", True, yellow)
        press_space_text = font.render("Press Space Bar to Start", True, yellow)
        instructions_text = font3.render("Left Key: Move Left, Right Key: Move Right", True, blue)
        crash_text = font3.render("Don't Crash", True, blue)
        #putting the writing on the screen
        startView.blit(taxi_driver_text, [150, 100])
        startView.blit(press_space_text, [50, 300])
        startView.blit(instructions_text, [40, 200])
        startView.blit(crash_text, [180, 230])
        # a loop for the startGame menu that allows the user quit or play
        gamestartExit = False
        while not gamestartExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamestartExit = True
                #if the user presses space it exits the loop and calls the game_loop function
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gamestartExit = True
                        Taxidriver.game_loop(self)


            pygame.display.flip()

def main():
    #creating the Taxidriver object "T"
    T = Taxidriver()
    #running the game starting with startGame function
    T.startGame()

main()
