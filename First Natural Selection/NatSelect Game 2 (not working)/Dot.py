from Brain import *
import pygame
from math import sqrt

width =600
height = 600
goal = [int(width/2),20]

screen = pygame.display.set_mode((width, height))

class Dot:
	def __init__(self,screen,width,height):
		self.brain = Brain(800)
		self.screen = screen
		self.width = int(width)
		self.height = int(height)
		self.brain.randomize()
		self.pos = [int(self.width/2),int(self.height/2)]
		self.vel = 3
		self.dead = False
		self.fitness = 0.0	
		self.reachedGoal = False
		self.isBest = False

	def dist(self, x1,y1,x2,y2):
		return sqrt(((x2-x1)**2) + ((y2-y1)**2))


	def show(self):
		if self.isBest:
			pygame.draw.circle(self.screen, (0,255,0), (self.pos[0],self.pos[1]), 4)
		else:	
			pygame.draw.circle(self.screen, (0,0,0), (self.pos[0],self.pos[1]), 2)


	def move(self):
		if(self.brain.size > self.brain.step):
			self.pos[0] += self.vel*self.brain.dir_x[self.brain.step]
			self.pos[1] += self.vel*self.brain.dir_y[self.brain.step]
			self.brain.step += 1 
			self.show()
		else:
			self.dead = True
	def update(self):
		if not self.dead and not self.reachedGoal:		
			self.move()
			if self.pos[0] > (self.width-5) or self.pos[0] <= 5 or self.pos[1] <= 5 or self.pos[1] > (self.height-5):
				self.dead = True
			elif self.dist(self.pos[0],self.pos[1],goal[0],goal[1]) < 10:
				self.reachedGoal =True
				#not working

	def calculatefitness(self):
		if self.reachedGoal:
			self.fitness = 1.0/16.0 + 10000.0/(self.brain.step**2)	
		else:
			distanceToGoal = self.dist(self.pos[0],self.pos[1],goal[0],goal[1])
			self.fitness = 1.0/(distanceToGoal**2)

	def restart(self):
		self.pos = [int(self.width/2),int(self.height/2)]
		self.brain.step = 0