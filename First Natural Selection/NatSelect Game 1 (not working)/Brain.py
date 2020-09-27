import random 


class Brain:
	def __init__(self,moves_amount):
		self.moves_amount = moves_amount
		self.moves_x = []
		self.moves_y = []
		self.step = 0

	def randomize(self):
		for i in range(0,self.moves_amount):	
			if random.randint(1,3)==1:
				self.moves_x.append(random.uniform(1,3))
			else:
				self.moves_x.append(random.uniform(-2,0))
			if random.randint(1,3)==1:
				self.moves_y.append(random.uniform(1,3))
			else:
				self.moves_y.append(random.uniform(-2,0))


	def mutate(self):
		mutationRate = 0.01
		for i in range(0,len(self.moves_x[:])):
			rand = random.random()
			if rand < mutationRate:
				if random.randint(1,3)==1:
					self.moves_x[i] = random.uniform(1,3)
				else:
					self.moves_x[i] = random.uniform(-2,0)
				if random.randint(1,3)==1:
					self.moves_y[i] = random.uniform(1,3)
				else:
					self.moves_y[i] = random.uniform(-2,0)

def clone(baby,parent):

	baby.brain.moves_x = parent.brain.moves_x 
	baby.brain.moves_y = parent.brain.moves_y

	return baby