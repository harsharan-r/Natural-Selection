import pygame 
from Brain import *
from numpy import *


width = 800
height = 800

screen = pygame.display.set_mode((width, height))

goal = (width/2, 30, 20,20)

class Dot:
	def __init__(self,screen,width,height):
		self.brain = Brain(1000)
		self.pos = []
		self.vel = 0
		self.screen = screen
		self.width = width
		self.height = height
		self.dead_bool = False
		self.reachedGoal = False
		self.fitness = 0
		self.brain.randomize()
		self.pos = [self.width/2,self.height/2]
		self.vel = 4
		pygame.draw.rect(self.screen, (255,255,0),(self.pos[0],self.pos[1],50,50))

	def spawn(self):
		pygame.draw.rect(self.screen, (255,255,0),(self.pos[0],self.pos[1],50,50))
		


	def border_check(self):
		if self.pos[0] < 780 and self.pos[0] >= 10 and self.pos[1] >= 10 and self.pos[1] < 780:
			self.dead_bool = False	
		else:
			self.dead_bool = True

		if self.pos[0] < 400 or self.pos[0] > 420 and self.pos[1] < 30 or self.pos[1] > 50:
			self.reachedGoal = False

		else:
			self.reachedGoal = True

	def dead(self):
		pygame.draw.rect(self.screen, (255,0,0),(self.pos[0],self.pos[1],10,10))

	def move(self):
		self.border_check()
		if not self.dead_bool and not self.reachedGoal:
			if self.brain.moves_amount > self.brain.step:
				self.pos[0] += (self.vel*self.brain.moves_x[self.brain.step])
				self.pos[1] += (self.vel*self.brain.moves_y[self.brain.step])
				self.brain.step += 1
				pygame.draw.rect(self.screen, (255,255,0),(self.pos[0],self.pos[1],10,10))
			else:
				self.reachedGoal = True
				pygame.draw.rect(self.screen, (0,0,255),(self.pos[0],self.pos[1],10,10))
			
		else:
			self.dead()	

	def calculateFitness(self):
		distanceToGoal = sqrt(((self.pos[0] - goal[0])**2) + ((self.pos[1] - goal[1])**2))
		self.fitness = 1.0/(distanceToGoal**2)


	