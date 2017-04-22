import pygame

#needed to capitalize class names
class Taxi:
	def __init__(self, color='yellow'):
		#self.xcoor = xcoor
		#self.ycoor = ycoor
		self.color = color
		#pygame.Rect(xcoor, ycoor, width, height)
		self.shape = pygame.Rect(250,460, 10, 40)

	def moveLeft(self):
		if self.shape != 150:
			self.shape -= 100

	def moveRight(self):
		if self.xcoor != 350:
			self.xcoor += 100

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color
		return mystr

#we need to integrate the spawning logic into this, might have to change it some
class Obstacle:
	def __init__(self, speed=10, color='gray'):
		self.color = color

		self.shape = pygame.Rect(xcoor,ycoor, 10, 10)
		self.speed = speed

	def move(self, speed):
		while self.ycoor >= 0:
			self.ycoor -= speed

	def place():

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color + '\n'
		mystr += 'Speed: ' + str(self.speed)
		return mystr
