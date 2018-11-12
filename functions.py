from vec3 import Vec3
from ray import Ray
from random import random

def randomInUnitSphere():
	temp = Vec3(random(), random(), random())
	while temp.length() > 1:
		temp = Vec3(random(), random(), random())
	return temp
