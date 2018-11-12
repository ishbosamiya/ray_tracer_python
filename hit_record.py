from vec3 import Vec3
from ray import Ray
from material import Material, Lambert

class Hit_Record:
	ray_in = Ray()
	point = Vec3()
	normal = Vec3()
	t = 0.0
	material = Lambert()
