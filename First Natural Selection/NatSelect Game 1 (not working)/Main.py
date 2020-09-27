import pygame 
from Dot import *
from Population import *
import sys	


pygame.init()


population(screen,width,height)

show()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((255,255,255))
	pygame.draw.rect(screen, (255,0,255),goal)
	Dead = allDotsDead()

	if Dead:
		print('all have died')
		calculatefitness()
		naturalSelection()
		mutateDemBabies()
		restart()
		show()
		
	else:	
		update()

	pygame.display.update()