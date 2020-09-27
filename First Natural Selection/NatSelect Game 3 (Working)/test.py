import random 
import numpy as np
from scipy.spatial import distance

arr1 = np.array([1,2])
arr2 = np.array([4,5,6])

direction = np.empty((10,2),dtype = int)
test = []

a = (1,2)

b = (8,9)

def dist(x1,y1,x2,y2):
	return np.sqrt(((x2-x1)**2) + ((y2-y1)**2))

dist1 = distance.euclidean(a,b)
dist2 = dist(a[0],a[1],b[0],b[1])

print(dist1,dist2)