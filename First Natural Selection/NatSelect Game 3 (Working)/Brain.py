import random 
import numpy as np
#if problem occurs with iterate tuple change to list

class Brain:

    def rad_to_offset(self,radians): 
        z = random.randint(-1,1)
        x = np.cos(radians) 
        y = np.sin(radians) 

        return np.array([x, y, z])

#---------------------------------------------------------------------------------------------------------------------
    	
    def randomize(self,direction):

        for i in range(0,self.size):
            randAngle = random.uniform(0,2*np.pi)

            direction[i] = self.rad_to_offset(randAngle)

#---------------------------------------------------------------------------------------------------------------------

    def __init__(self,size):
        self.direction = np.empty((size,3),dtype = float)
        self.size = size
        self.step = 0
        self.randomize(self.direction)

#---------------------------------------------------------------------------------------------------------------------

    def mutate(self):
        mutatationRate = 0.01
        for i in range(0,self.size):
            rand = random.random()
            if(rand < mutatationRate):
                randAngle = random.uniform(0,2*np.pi)
                self.direction[i] = self.rad_to_offset(randAngle) 



 

