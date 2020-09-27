from Brain import *
import pygame


class Dot:
	def __init__(self,screen,width,height):
		self.brain = Brain(400)
		self.screen = screen
		self.width = int(width)
		self.height = int(height)
		self.pos = np.array([self.width/2,self.height-10], dtype=float)
		self.vel = np.zeros((2),dtype = float)
		self.acc = np.zeros((2),dtype = float)
		self.dead =  False
		self.reachedGoal =  False  
		self.fitness = 0 
		self.goal = [int(width/2),10]
		self.isBest = False 
		self.obsticles = True
#---------------------------------------------------------------------------------------------------------------------

	def show(self):
		if self.isBest:
			colour = (0,255,0)
		else:	
			colour = (0,0,0)

		pygame.draw.ellipse(self.screen, colour, (self.pos[0],self.pos[1],5,5))

#---------------------------------------------------------------------------------------------------------------------
	
	def move(self):
		if self.brain.size > self.brain.step:
			self.acc = self.brain.direction[self.brain.step][:2]
			self.brain.step += 1
		else:
			dead = True 

		self.vel += self.acc
		self.pos += self.vel

#---------------------------------------------------------------------------------------------------------------------
	
	def dist(self,x1,y1,x2,y2):
		#calculate the euclidean distance 
		x1,x2,y1,y2 = (x1+3),(x2+3),(y1+3),(y2+3)
		return np.sqrt(((x2-x1)**2) + ((y2-y1)**2))

#---------------------------------------------------------------------------------------------------------------------		
	
	def update(self):
		if not self.dead and not self.reachedGoal:
			self.move()

			if(self.pos[0] < 10 or self.pos[1] < 10 or self.pos[0] > self.width-10 or self.pos[1]>self.height-10):
				self.dead = True 

			elif self.dist(self.pos[0],self.pos[1],self.goal[0],self.goal[1])<7:
				self.reachedGoal = True

			elif(self.pos[0] < 705 and self.pos[1] < 315 and self.pos[0] >95 and self.pos[1] > 295) and self.obsticles:
				self.dead = True

#---------------------------------------------------------------------------------------------------------------------
	def calculateFitness(self):
		if self.reachedGoal:
		 self.fitness = 1/16 + 10000/(self.brain.step**2)
		else:	
			distanceToGoal = self.dist(self.pos[0],self.pos[1],self.goal[0],self.goal[1])	
			self.fitness = 1/(distanceToGoal**3)	

#---------------------------------------------------------------------------------------------------------------------

