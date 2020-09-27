from Dot import * 
import random
from Brain import clone


howmanyreturned = []
fitnessSum = 0
dots = []
size = 600
newdots = []
gen = 1

def population(screen,width,height):
	for i in range(0,size):
		dots.append(Dot(screen,width,height))

def show():
	global dots
	global size
	for i in range(0,size):
		dots[i].spawn()

def update():
	global dots
	global size
	for i in range(0,size):
		dots[i].move()

def calculatefitness():
	global dots
	global size
	for i in range(0,size):
		dots[i].calculateFitness()

def allDotsDead():
	global dots
	global size
	amountDead = 0
	for i in range(0,size):
		if not dots[i].dead_bool and not dots[i].reachedGoal:
			pass
		else:
			amountDead += 1


	return amountDead == size 	

def calculatefitnessSum():
	global fitnessSum
	global newdots
	global dots
	global size
	for i in range(0,size):
		fitnessSum +=  dots[i].fitness

	fitnessSum /= size+100 

def selectParent():
	global fitnessSum
	global howmanyreturned
	rand = random.uniform(0,fitnessSum)
	runningSum = 0
	for i in range(0,size):
		runningSum += dots[i].fitness
		if runningSum > rand:
			howmanyreturned.append(dots[i].fitness)
			howmanyreturned = set(howmanyreturned)
			howmanyreturned = list(howmanyreturned)
			return dots[i]
		
	


def naturalSelection():
	global dots
	global size
	global newdots
	global parent
	global gen
	newdots = []
	calculatefitnessSum()
	for i in range(0,size):
		#select parent off of fitness
		parent = selectParent()

		#get baby from it
		baby = Dot(screen,width,height)
		newdots.append(clone(baby,parent))
	print(howmanyreturned)
	dots = newdots
	gen += 1


def mutateDemBabies():
	global dots
	global size
	for i in range(0,size):
		dots[i].brain.mutate()

def restart():
	global dots
	global size
	for i in range(0,size):
		dots[i].brain.step = 0
		dots[i].pos = [dots[i].width/2,dots[i].height/2]
		dots[i].dead_bool = False
		dots[i].reachedGoal = False