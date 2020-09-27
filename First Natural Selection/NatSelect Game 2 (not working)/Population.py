from Dot import *

class Population:

	def __init__(self,size,screen,width,height):
		self.dots = []
		self.size = size
		self.fitnessSum = 0.0
		self.gen = 0
		self.screen = screen
		self.width = width
		self.height = height
		self.bestindex = 0


		for i in range(0,size):
				

	def show(self):
		for i in range(0,self.size):
			self.dots[i].show()


	def update(self):
		for i in range(0,self.size):
			self.dots[i].update()



	def setBestDot(self):
		max_best = 0
		max_index = 0
		for i in range(0,self.size):
			if self.dots[i].fitness > max_best:
				max_best = self.dots[i].fitness
				max_index = i
		self.bestindex = max_index

	def calculatefitness(self):
		for i in range(0,self.size):
			self.dots[i].calculatefitness()


	def allDotsDead(self):
		for i in range(0,self.size):
			if not self.dots[i].dead and not self.dots[i].reachedGoal:
				return False
		return True 

	def calculateFitnessSum(self):
		self.calculatefitness()
		self.fitnessSum = 0
		for i in range(0,self.size):
			self.fitnessSum += self.dots[i].fitness

	def selectParent(self):	
		rand = random.uniform(0,self.fitnessSum)
		red = []
		runningSum = 0
		for i in range(0,self.size):
			runningSum += self.dots[i].fitness
			if runningSum > rand:
				return self.dots[i]
		

	def naturalSelection(self):
		newdots = []
		self.setBestDot()


		for i in range(0,self.size):
			#select parent
			parent = self.selectParent()
			#get baby form them
			baby = Dot(self.screen,self.width,self.height)
			baby.brain.dir_x = parent.brain.dir_x
			baby.brain.dir_y = parent.brain.dir_y
			newdots.append(baby)

		self.dots = newdots
		self.dots.append(Dot(self.screen,self.width,self.height))
		self.dots[-1].brain.dir_x = self.dots[self.bestindex].brain.dir_x
		self.dots[-1].brain.dir_y = self.dots[self.bestindex].brain.dir_y
		self.dots[-1].isBest = True
		print(self.dots[-1].isBest)

		self.gen += 1



	def mutateDemBabies(self):
		for i in range(0,self.size-1):
			self.dots[i].brain.mutate()







