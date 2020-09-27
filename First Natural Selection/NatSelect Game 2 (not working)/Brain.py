import random
class Brain:
	def __init__(self,size):
		self.step = 0	
		self.dir_x = []
		self.dir_y = []
		self.size = size

	def randomize(self):
		for i in range(0,self.size):
			
			if random.randint(0,1) == 0:
				self.dir_x.append(-1)
			else:
				self.dir_x.append(1)
			if random.randint(0,1) == 0:
				self.dir_y.append(-1)	
			else:
				self.dir_y.append(1)

	def mutate(self):
		mutationRate = 0.01
		for i in range(0,self.size):
			rand = random.random()
			if rand < mutationRate:
				if random.randint(0,1) == 0:
					self.dir_x[i]= -1
				else:
					self.dir_x[i]= 1
				if random.randint(0,1) == 0:
					self.dir_y[i]= -1	
				else:
					self.dir_y[i]= 1
