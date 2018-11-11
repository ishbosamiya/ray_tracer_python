from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from ppm_writer import ppmWriter
from math import sqrt

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

pixels = []
spheres = [Sphere(Vec3(-0.5, 0.0, 2.0), 0.5), Sphere(Vec3(0.5, 0.0, 2.0), 0.5)]

aspect_ratio = float(width / height)
lower_left_corner = Vec3(-1.0 * aspect_ratio, -1.0, 1.0)
horizontal = Vec3(2.0 * aspect_ratio, 0.0, 0.0)
vertical = Vec3(0.0, 2.0, 0.0)

for y in range(height, 0, -1):
	for x in range(0, width):
		u = float(x / width)
		v = float(y / height)
		ray = Ray(Vec3(0.0, 0.0, 0.0), lower_left_corner + horizontal * u + vertical * v)
		colour = Vec3(0, 0, 0)
		for sphere in spheres:
			temp = sphere.hit(ray)
			if temp[0]:
				colour = ((temp[1].normal + Vec3(1.0, 1.0, 1.0)) / 2.0) * 255.0
				break
			else:
				colour = Vec3(0, 0, 0)
		pixels.append(colour)

print("Actual length:", len(pixels), "Expected Length:", width * height)
ppmWriter(pixels, "temp.ppm", width, height)
