from vec3 import Vec3
from ray import Ray
from functions import *

def reflection(incident_direction, normal):
	return incident_direction - normal * (2 * incident_direction.dot(normal))

class Material:
	def scattered(self, ray_in, hit_record):
		pass

class Lambert(Material):
	def __init__(self, colour = Vec3(0.87, 0.25, 0.74)):
		self.colour = colour

	def scattered(self, ray_in, hit_record):
		ray_out = Ray(hit_record.point, (hit_record.normal + randomInUnitSphere()).normalized())
		return (True, ray_out, self.colour)

class Metal(Material):
	def __init__(self, colour = Vec3(0.87, 0.25, 0.74), roughness = 0.0):
		self.colour = colour
		self.roughness = roughness

	def scattered(self, ray_in, hit_record):
		diffuse_direction = (hit_record.normal + randomInUnitSphere()).normalized()
		reflection_direction = reflection(ray_in.getDirection(), hit_record.normal)
		ray_out_direction = diffuse_direction * self.roughness + reflection_direction * (1.0 - self.roughness)
		ray_out = Ray(hit_record.point, ray_out_direction.normalized())
		return (True, ray_out, self.colour)
