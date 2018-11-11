from vec3 import Vec3
from ray import Ray
from random import random

class Camera:
	def __init__(self, width, height, camera_origin = Vec3(0.0, 0.0, 0.0), camera_length = 1.0):
		self.width = width
		self.height = height
		self.camera_origin = camera_origin
		self.aspect_ratio = float(width / height)
		self.lower_left_corner = Vec3(-1.0 * self.aspect_ratio, -1.0, camera_length)
		self.horizontal = Vec3(2.0 * self.aspect_ratio, 0.0, 0.0)
		self.vertical = Vec3(0.0, 2.0, 0.0)

	def getRay(self, x, y):
		u = float((x + random())/ self.width)
		v = float((y + random())/ self.height)
		return Ray(self.camera_origin, self.lower_left_corner + self.horizontal * u + self.vertical * v)
