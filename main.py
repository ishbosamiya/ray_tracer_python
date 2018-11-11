from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from ppm_writer import ppmWriter
from math import sqrt

width = 300
height = 200

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
