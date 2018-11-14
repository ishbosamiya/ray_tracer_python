from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from hitable import Hitable
from material import *
from aabb import AABB

class Triangle(Hitable):
	def __init__(self, v, vt = [], vn = [], material = Lambert()):
		self.v = v
		self.vt = vt
		self.vn = vn
		self.material = material

		#calculating bounding box
		minx = min([self.v[0].x, self.v[1].x, self.v[2].x])
		miny = min([self.v[0].y, self.v[1].y, self.v[2].y])
		minz = min([self.v[0].z, self.v[1].z, self.v[2].z])

		maxx = max([self.v[0].x, self.v[1].x, self.v[2].x])
		maxy = max([self.v[0].y, self.v[1].y, self.v[2].y])
		maxz = max([self.v[0].z, self.v[1].z, self.v[2].z])

		self.box = AABB(Vec3(minx, miny, minz), Vec3(maxx, maxy, maxz))
	def hit(self, ray_in, t_min, t_max):
		hit_record = Hit_Record()
		edge1 = self.v[1] - self.v[0]
		edge2 = self.v[2] - self.v[0]
		
		n = edge1.cross(edge2).normalized()
		q = ray_in.getDirection().cross(edge2)
		a = edge1.dot(q)

		if n.dot(ray_in.getDirection()) >= 0.0 or abs(a) <= 0.0001:
			return (False, hit_record)

		s = (ray_in.getOrigin() - self.v[0]) / a
		r = s.cross(edge1)
		
		b = [s.dot(q), r.dot(ray_in.getDirection())]
		bar_coords = Vec3(b[0], b[1], 1.0 - b[0] - b[1])
		
		if bar_coords.x < 0.0 or bar_coords.y < 0.0 or bar_coords.z < 0.0:
			return (False, hit_record)

		t = edge2.dot(r)
		if t >= t_min and t <= t_max:
			hit_record.ray_in = ray_in
			hit_record.point = ray_in.pointAtParameter(t)
			hit_record.normal = n
			hit_record.t = t
			hit_record.material = self.material
			return (True, hit_record)
		else:
			return (False, hit_record)

	def boundingBox(self, time0, time1):
		return (True, self.box)
