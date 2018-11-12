from vec3 import Vec3
from ray import Ray
from Hitable import Hitable

from math import abs

class Triangle(Hitable):
	def __init__(self, v, vt = [], vn = []):
		self.v = v
		self.vt = vt
		self.vn = vn
	def hit(self, ray_in, t_min, t_max):
		hit_record = Hit_Record()
		edge1 = self.v[1] - self.v[0]
		edge2 = self.v[2] - self.v[0]
		
		n = edge1.cross(edge2)
		q = ray_in.getDirection().cross(edge2)
		a = edge1.dot(q)

		if n.dot(q) >= 0 or abs(a) <= 0.0001:
			return (False, hit_record)

		s = (ray_in.getOrigin() - self.v[0]) / a
		r = s.cross(edge1)
		
		b = [s.dot(q), r.dot(ray_in.getDirection())]
		bar_coords = Vec3(b[0], b[1], 1.0 - b[0] - b[1])
