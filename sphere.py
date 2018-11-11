from vec3 import Vec3
from ray import Ray
from math import sqrt
from hit_record import Hit_Record

class Sphere:
	def __init__(self, center = Vec3(0, 0, 0), radius = 0):
		self.center = center
		self.radius = radius
	
	def hit(self, ray_in):
		a = ray_in.getDirection().dot(ray_in.getDirection())
		b = 2.0 * ray_in.getDirection().dot(ray_in.getOrigin() - self.center)
		c = (ray_in.getOrigin() - self.center).dot(ray_in.getOrigin() - self.center) - (self.radius * self.radius)

		d = b * b - (4.0 * a * c)
		hit_record = Hit_Record()
		if d < 0:
			return (False, hit_record)
		else:
			t = (- b - sqrt(d)) / (2.0 * a)
			hit_record.ray_in = ray_in
			hit_record.point = ray_in.pointAtParameter(t)
			hit_record.normal = (hit_record.point - self.center).normalized()
			hit_record.t = t
			return (True, hit_record)
