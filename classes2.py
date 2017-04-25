import pygame

class GameObj(object):
	def __init__(self, screen):
		self.screen = screen
	
	def draw(self):
		pass
		
	def update(self):
		pass
		
class Taxi(GameObj):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Taxi_assets/car5.png')
		self.image = pygame.transform.scale(self.image, (60, 40))
		self.rect = self.image.get_rect()
		
		self.rect.x = 250
		self.rect.y = 0

	def update(self):
		pass
	
	def move(self, l_r):
		if l_r == 'left'
			while self.rect.x != 150:
				self.rect = self.rect.move(150,0)
		if l_r == 'right'
			while self.rect.x != 350:
				self.rect = self.rect.move(350,0)

#we need to integrate the spawning logic into this, might have to change it some
class Obstacle:
	def __init__(self, speed=10, color='gray'):
		self.color = color

		self.shape = pygame.Rect(xcoor,ycoor, 10, 10)
		self.speed = speed

	def move(self, speed):
		while self.ycoor >= 0:
			self.ycoor -= speed
