import pygame
from Population import * 
import sys

pygame.init()


test = Population(1000,screen,width,height)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((255,255,255))
	pygame.draw.circle(screen, (200,10,200), (goal[0],goal[1]),10)

	if test.allDotsDead():
		test.calculateFitnessSum()
		test.naturalSelection()
		test.mutateDemBabies()
	else:
		test.update()
		test.show()

	pygame.display.update()