from vec3 import Vec3
from ray import Ray
from ppm_writer import ppmWriter

width = 100
height = 100

class Sphere:
	def __init__(self, center = Vec3(0, 0, 0), radius = 0):
		self.center = center
		self.radius = radius
	
	def hit(self, ray_in):
		a = ray_in.getDirection().dot(ray_in.getDirection())
		b = 2.0 * ray_in.getDirection().dot(ray_in.getOrigin() - self.center)
		c = (ray_in.getOrigin() - self.center).dot(ray_in.getOrigin() - self.center) - (self.radius * self.radius)

		d = b * b - (4.0 * a * c)
		if d < 0:
			return False
		else:
			return True

pixels = []
sphere = Sphere(Vec3(width/2.0, height/2.0, 100.0), 50.0)
for y in range(0, height):
	for x in range(0, width):
		ray = Ray(Vec3(x, y, 0), Vec3(x, y, 1))
		if sphere.hit(ray):
			pixels.append(Vec3(255, 0, 0))
		else:
			pixels.append(Vec3(0, 0, 0))

ppmWriter(pixels, "temp.ppm", width, height)
