import pygame

#needed to capitalize class names
class Taxi(pygame.sprite.Sprite):
	def __init__(self, color='yellow'):
		pygame.sprite.Sprite.__init__(self)
		#self.xcoor = xcoor
		#self.ycoor = ycoor
		#self.start_x = start_x
		self.color = color
		self.image = pygame.transform.scale(pygame.image.load('car5.png'), [40,20])
		#pygame.Rect(xcoor, ycoor, width, height)
		self.rect = self.image.get_rect()

		self.rect.x = 250
		self.rect.y = 460

	def moveLeft(self, left_x = -100):
		self.left_x = left_x
		'''
		if self.start_x != 150:
			self.start_x -= 100
			'''
		print("moving left:", self.rect.x, " ", self.rect.y)
		if self.rect.x != 150:
			self.rect = self.rect.move(left_x, 0)

	def moveRight(self, right_x = 100):
		'''
		#self.start_x = 250
		if self.start_x != 350:
			self.start_x += 100
			'''
		print("moving right:", self.shape.x, " ", self.shape.y)
		if self.rect.x != 350:
			self.rect = self.rect.move(right_x, 0)

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

	#def place():

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color + '\n'
		mystr += 'Speed: ' + str(self.speed)
		return mystr
