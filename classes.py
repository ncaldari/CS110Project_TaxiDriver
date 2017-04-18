class taxi:
	def __init__(self, color='yellow', xcoor=0, ycoor=0, model='taxi.png'):
		self.xcoor = xcoor
		self.ycoor = ycoor
		self.color = color
		self.model = model

	def moveLeft(self):
		if self.xcoor != -1:
			self.xcoor -= 1

	def moveRight(self):
		if self.xcoor != 1:
			self.xcoor += 1

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color
		return mystr


class obstacle:
	def __init__(self, xcoor, ycoor=100, speed=10, color='gray', model='obstacle.png'):
		self.color = color
		self.xcoor = xcoor
		self.ycoor = ycoor
		self.speed = speed
		self.model = model

	def move(self, speed):
		while self.ycoor >= 0:
			self.ycoor -= speed

	def __str__(self):
		mystr = ''
		mystr += 'Coordinates: ' + str(self.xcoor) + ', ' + str(self.ycoor) + '\n'
		mystr += 'Color: ' + self.color + '\n'
		mystr += 'Speed: ' + str(self.speed)
		return mystr
