from Dot import Dot 
import random
import numpy as np

class Population:
	def __init__(self,size,screen,width,height):
		self.size = size 
		self.dots = []
		self.fitnessSum = 0 
		self.runningSum = 0
		self.width = width
		self.height = height
		self.screen = screen
		self.gen = 1
		self.minSteps = 400 


		for i in range(0,self.size):
			self.dots.append(Dot(screen,width,height))

#---------------------------------------------------------------------------------------------------------------------

	def show(self):
		for i in range(0,self.size):
			self.dots[i].show()

#---------------------------------------------------------------------------------------------------------------------

	def update(self):
		for i in range(0,self.size):
			if self.dots[i].brain.step > self.minSteps:
				self.dots[i].dead = True 
				print(self.dots[i].brain.step)
			else:	
				self.dots[i].update()

#---------------------------------------------------------------------------------------------------------------------

	def calculateFitness(self):
		for i in range(0,self.size):
			self.dots[i].calculateFitness()

#---------------------------------------------------------------------------------------------------------------------

	def allDotsDead(self):
		for i in range(0,self.size):
			if not self.dots[i].dead and not self.dots[i].reachedGoal:
				return False
		return True 

#---------------------------------------------------------------------------------------------------------------------

	def calculateFitnessSum(self):
		self.fitnessSum = 0
		for i in range(0,self.size):
			self.fitnessSum += self.dots[i].fitness


#---------------------------------------------------------------------------------------------------------------------

	def selectParent(self):
		rand = random.uniform(0,self.fitnessSum)

		runningSum = 0

		for i in range(0,self.size):
			runningSum += self.dots[i].fitness
			if runningSum > rand:
				return self.dots[i]

#---------------------------------------------------------------------------------------------------------------------

	def gimmeBaby(self):
		baby = Dot(self.screen, self.width,self.height)
		return baby
#---------------------------------------------------------------------------------------------------------------------

	def setBestDot(self):
		max_ = 0
		maxIndex = 0
		for i in range(0,size):
			if self.dots[i].fitness > max_:
				max_ = dots[i].fitness
				maxIndex = i
		self.bestDot = maxIndex

		if self.dots[self.bestDot].reachedGoal:
			self.minSteps = self.dots[self.bestDot].brain.step


#---------------------------------------------------------------------------------------------------------------------

	def naturalSelection(self):
		newdots = []
		self.calculateFitnessSum()
		self.setBestDot()

		for i in range(1,self.size):

			parent = self.selectParent()
			baby = self.gimmeBaby()
			baby.brain.direction = np.copy(parent.brain.direction)
			newdots.append(baby)


		bestbaby = self.gimmeBaby()
		#using np.copy instead of just '=' to avoid broadcasting and havign a chance of adding unwanted mutation
		bestbaby.brain.direction = np.copy(self.dots[self.bestDot].brain.direction)
		newdots.append(bestbaby)
		newdots[-1].isBest = True

		self.dots = newdots
		self.gen += 1

#---------------------------------------------------------------------------------------------------------------------

	def mutateDemBabies(self):
		for i in range(0,self.size-1):
			self.dots[i].brain.mutate()

#---------------------------------------------------------------------------------------------------------------------

	def setBestDot(self):
		max_ = 0
		maxIndex = 0
		for i in range(0,self.size-1):
			if self.dots[i].fitness > max_:
				max_ = self.dots[i].fitness
				maxIndex = i
		self.bestDot = maxIndex