from vec3 import Vec3
from ray import Ray
from Hitable import Hitable

class Triangle(Hitable):
	def __init__(self, v, vt = [], vn = []):
		self.v = v
		self.vt = vt
		self.vn = vn
	def hit(self, ray_in, t_min, t_max):
		
