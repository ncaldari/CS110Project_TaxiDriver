import classes
import random

loop?:
	lanes = [-1, 0, 1]
	x1 = random.choice(lanes)
	del lanes(x1)
	obst1 = classes.obstacle(x1)
	x2 = random.choice(lanes)
	obst2 = classes.obstacle(x2)
