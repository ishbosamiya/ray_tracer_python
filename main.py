from vec3 import Vec3
from ray import Ray
from ppm_writer import ppmWriter

width = 300
height = 200

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
spheres = [Sphere(Vec3(-0.5, 0.0, 2.0), 0.5), Sphere(Vec3(0.5, 0.0, 2.0), 0.5)]

aspect_ratio = float(width / height)
lower_left_corner = Vec3(-1.0 * aspect_ratio, -1.0, 1.0)
horizontal = Vec3(2.0 * aspect_ratio, 0.0, 0.0)
vertical = Vec3(0.0, 2.0, 0.0)

for y in range(0, height):
	for x in range(0, width):
		u = float(x / width)
		v = float(y / height)
		ray = Ray(Vec3(0.0, 0.0, 0.0), lower_left_corner + horizontal * u + vertical * v)
		colour = Vec3(0, 0, 0)
		for sphere in spheres:
			if sphere.hit(ray):
				colour = Vec3(255, 0, 0)
				break
			else:
				colour = Vec3(0, 0, 0)
		pixels.append(colour)

print("Actual length:", len(pixels), "Expected Length:", width * height)
ppmWriter(pixels, "temp.ppm", width, height)
