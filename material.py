from vec3 import Vec3
from ray import Ray
from functions import *

class Material:
	def scattered(self, ray_in, hit_record):
		pass

class Lambert(Material):
	def __init__(self, colour = Vec3(0.87, 0.25, 0.74)):
		self.colour = colour

	def scattered(self, ray_in, hit_record):
		ray_out = Ray(hit_record.point, (hit_record.normal + randomInUnitSphere()).normalized())
		return (True, ray_out, self.colour)
