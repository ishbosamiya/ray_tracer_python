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

	"""
	def getMin(self):
		return self.m_min
	def getMax(self):
		return self.m_max
	"""

	def hit(self, ray_in, t_min, t_max):
		inv_ray_direction = 1.0/ray_in.getDirection().x
		t0 = min((self.m_min.x - ray_in.getOrigin().x)*inv_ray_direction,
					(self.m_max.x - ray_in.getOrigin().x)*inv_ray_direction)
		t1 = max((self.m_min.x - ray_in.getOrigin().x)*inv_ray_direction,
					(self.m_max.x - ray_in.getOrigin().x)*inv_ray_direction)
		t_min = max(t0, t_min)
		t_max = min(t1, t_max)
		if t_max <= t_min:
			return (False,)

		inv_ray_direction = 1.0/ray_in.getDirection().y
		t0 = min((self.m_min.y - ray_in.getOrigin().y)*inv_ray_direction,
					(self.m_max.y - ray_in.getOrigin().y)*inv_ray_direction)
		t1 = max((self.m_min.y - ray_in.getOrigin().y)*inv_ray_direction,
					(self.m_max.y - ray_in.getOrigin().y)*inv_ray_direction)
		t_min = max(t0, t_min)
		t_max = min(t1, t_max)
		if t_max <= t_min:
			return (False,)

		inv_ray_direction = 1.0/ray_in.getDirection().z
		t0 = min((self.m_min.z - ray_in.getOrigin().z)*inv_ray_direction,
					(self.m_max.z - ray_in.getOrigin().z)*inv_ray_direction)
		t1 = max((self.m_min.z - ray_in.getOrigin().z)*inv_ray_direction,
					(self.m_max.z - ray_in.getOrigin().z)*inv_ray_direction)
		t_min = max(t0, t_min)
		t_max = min(t1, t_max)
		if t_max <= t_min:
			return (False,)

		return (True,)

def surroundingBox(box0, box1):
	small = Vec3(min(box0.m_min.x, box1.m_min.x),
				min(box0.m_min.y, box1.m_min.y),
				min(box0.m_min.z, box1.m_min.z))
	big = Vec3(max(box0.m_max.x, box1.m_max.x),
				max(box0.m_max.y, box1.m_max.y),
				max(box0.m_max.z, box1.m_max.z))
	return AABB(small, big)
