from vec3 import Vec3
from ray import Ray
from math import sqrt
from hit_record import Hit_Record
from hitable import Hitable
from material import *

class Sphere(Hitable):
	def __init__(self, center = Vec3(0, 0, 0), radius = 0, material = Lambert()):
		self.center = center
		self.radius = radius
		self.material = material
	
	def hit(self, ray_in, t_min, t_max):
		a = ray_in.getDirection().dot(ray_in.getDirection())
		b = 2.0 * ray_in.getDirection().dot(ray_in.getOrigin() - self.center)
		c = (ray_in.getOrigin() - self.center).dot(ray_in.getOrigin() - self.center) - (self.radius * self.radius)

		d = b * b - (4.0 * a * c)
		hit_record = Hit_Record()
		if d > 0:
			t1 = (- b - sqrt(d)) / (2.0 * a)
			if t1 > t_min and t1 < t_max:
				hit_record.ray_in = ray_in
				hit_record.point = ray_in.pointAtParameter(t1)
				hit_record.normal = (hit_record.point - self.center).normalized()
				hit_record.t = t1
				hit_record.material = self.material
				return (True, hit_record)
			t2 = (- b + sqrt(d)) / (2.0 * a)
			if t2 > t_min and t2 < t_max:
				hit_record.ray_in = ray_in
				hit_record.point = ray_in.pointAtParameter(t2)
				hit_record.normal = (hit_record.point - self.center).normalized()
				hit_record.t = t2
				hit_record.material = self.material
				return (True, hit_record)
		return (False, hit_record)
