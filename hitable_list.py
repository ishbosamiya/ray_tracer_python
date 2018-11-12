from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from hitable import Hitable

class Hitable_List(Hitable):
	list_of_objects = []
	def __init__(self, list_of_objects):
		self.list_of_objects = list_of_objects

	def hit(self, ray_in, t_min, t_max):
		record = Hit_Record()
		hit_anything = False;
		closest_so_far = t_max;
		for i in self.list_of_objects:
			temp = i.hit(ray_in, t_min, closest_so_far)
			if temp[0]:
				hit_anything = True;
				closest_so_far = temp[1].t;
				record = temp[1];
		return (hit_anything, record)
