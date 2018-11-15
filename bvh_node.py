from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from hitable import Hitable
from aabb import *
from random import random
from functools import cmp_to_key

def boxXCompare(ah, bh):
	box_left = ah.boundingBox(0.0, 0.0)
	box_right = bh.boundingBox(0.0, 0.0)
	if not box_left[0] or not box_right[0]:
		print("No bounding box in BVH_Node!")
	if box_left[1].m_min.x - box_right[1].m_min.x < 0.0:
		return False
	else:
		return True

def boxYCompare(ah, bh):
	box_left = ah.boundingBox(0.0, 0.0)
	box_right = bh.boundingBox(0.0, 0.0)
	if not box_left[0] or not box_right[0]:
		print("No bounding box in BVH_Node!")
	if box_left[1].m_min.y - box_right[1].m_min.y < 0.0:
		return False
	else:
		return True

def boxZCompare(ah, bh):
	box_left = ah.boundingBox(0.0, 0.0)
	box_right = bh.boundingBox(0.0, 0.0)
	if not box_left[0] or not box_right[0]:
		print("No bounding box in BVH_Node!")
	if box_left[1].m_min.z - box_right[1].m_min.z < 0.0:
		return False
	else:
		return True

class BVH_Node(Hitable):
	left = Hitable()
	right = Hitable()
	box = AABB()

	def __init__(self, hitable_list, size, time0, time1):
		axis = int(3 * random())
		if axis == 0:
			sorted(hitable_list, key = cmp_to_key(boxXCompare))
		elif axis == 1:
			sorted(hitable_list, key = cmp_to_key(boxYCompare))
		else:
			sorted(hitable_list, key = cmp_to_key(boxZCompare))

		if size == 1:
			self.left = hitable_list[0]
			self.right = hitable_list[0]
		elif size == 2:
			self.left = hitable_list[0]
			self.right = hitable_list[1]
		else:
			self.left = BVH_Node(hitable_list, int(size/2), time0, time1)
			self.right = BVH_Node(hitable_list[int(size/2):], size - int(size/2), time0, time1)

		box_left = self.left.boundingBox(time0, time1)
		box_right = self.right.boundingBox(time0, time1)
		if not box_left[0] or not box_right[0]:
			print("No Bounding Box in BVH_Node Constructor!")
		self.box = surroundingBox(box_left[1], box_right[1])

	def hit(self, ray_in, t_min, t_max):
		hit_record = Hit_Record()
		box_hit = self.box.hit(ray_in, t_min, t_max)
		if box_hit[0]:
			left_record = self.left.hit(ray_in, t_min, t_max)
			right_record = self.right.hit(ray_in, t_min, t_max)
			if left_record[0] and right_record[0]:
				if left_record[1].t < right_record[1].t:
					hit_record = left_record[1]
				else:
					hit_record = right_record[1]
				return (True, hit_record)
			elif left_record[0]:
				hit_record = left_record[1]
				return (True, hit_record)
			elif right_record[0]:
				hit_record = right_record[1]
				return (True, hit_record)
			else:
				return (False, hit_record)
		return (False, hit_record)

	def boundingBox(self, time0, time1):
		return (True, self.box)
