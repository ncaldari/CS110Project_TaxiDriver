import pygame
import random
from classes import Taxi, Obstacle

class Taxidriver:
    def __init__(self):
        #pygame.init()


        white = (255,255,255)
        black = (0,0,0)
        blue = (0,0,255)
        green = (0,220,0)

        mytaxi = Taxi()
        myobstacle = Obstacle()
        myobstacle2 = Obstacle()




        self.gameView = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Taxi Driver')

        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        mytaxi.moveLeft()
                    if event.type == pygame.K_RIGHT:
                        mytaxi.moveRight()

            pygame.draw.rect(self.gameView, blue, mytaxi.shape) #[xcoor,ycoor,width,height]
        #spawner()

            pygame.display.flip()



def startMenu(): #this shouldnt be its own function
    self.startView = pygame.display.set_mode((500,500))
    gamestartExit = False
    while not gamestartExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestartExit = True
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TestRect = text_objects("Taxi Driver", largeText)
        TextRect.center = ((display_width/3), (display_height/3))
        self.startView.blit(TextSurf,TextRect)
        pygame.display.update()

def main():
    #mytaxi = taxi.Taxi()
    Taxidriver()
main()
