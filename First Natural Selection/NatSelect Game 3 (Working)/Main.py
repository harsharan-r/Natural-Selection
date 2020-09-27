import pygame 
import sys
from Dot import Dot 
from Population import Population

width = 800
height = 800
obsticles = True


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


test = Population(500,screen,width,height)
myfont = pygame.font.SysFont('monospace', 35,bold=True)
text = 'Gen: ' + str(test.gen)
label = myfont.render(text,1,(0,200,220))

while True:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill((255,255,255))

	pygame.draw.circle(screen, (255,0,0), (400,10),10)
	if obsticles:
		pygame.draw.rect(screen, (0,0,255),(100,300,600,10))

	if test.allDotsDead():
		test.calculateFitness()
		test.naturalSelection()
		test.mutateDemBabies()

	else:

		test.update()
		test.show()
	
	text = 'Gen: ' + str(test.gen)
	label = myfont.render(text,1,(0,200,220))
	screen.blit(label, (width-150, height-40))

	#no drawing code after this line	clock.tick(9)
	pygame.display.update()