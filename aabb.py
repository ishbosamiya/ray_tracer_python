from vec3 import Vec3
from ray import Ray

def ffmin(a, b):
	if a < b:
		return a
	else:
		return b

def ffmax(a, b):
	if a > b:
		return a
	else:
		return b

class AABB:
	def __init__(self, m_min = Vec3(), m_max = Vec3()):
		self.m_min = m_min
		self.m_max = m_max

	def getMin(self):
		return self.m_min
	def getMax(self):
		return self.m_max

	def hit(self, ray_in, t_min, t_max):
		for i in range(0, 3):
			inv_ray_direction = 1.0/ray_in.getDirection()[i]
			t0 = ffmin((self.getMin()[i] - ray_in.getOrigin()[i])*inv_ray_direction,
						(self.getMax()[i] - ray_in.getOrigin()[i])*inv_ray_direction)
			t1 = ffmax((self.getMin()[i] - ray_in.getOrigin()[i])*inv_ray_direction,
						(self.getMax()[i] - ray_in.getOrigin()[i])*inv_ray_direction)
			t_min = ffmax(t0, t_min)
			t_max = ffmin(t1, t_max)
			if t_max <= t_min:
				return (False,)
		return (True,)

def surroundingBox(box0, box1):
	small = Vec3(ffmin(box0.getMin().x, box1.getMin().x),
				ffmin(box0.getMin().y, box1.getMin().y),
				ffmin(box0.getMin().z, box1.getMin().z))
	big = Vec3(ffmax(box0.getMax().x, box1.getMax().x),
				ffmax(box0.getMax().y, box1.getMax().y),
				ffmax(box0.getMax().z, box1.getMax().z))
	return AABB(small, big)
