from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from ppm_writer import ppmWriter
from camera import Camera
from sphere import Sphere
from triangle import Triangle

from math import sqrt

width = 300
height = 200
no_of_samples = 10

pixels = []
#spheres = [Sphere(Vec3(-0.5, 0.0, 2.0), 0.5), Sphere(Vec3(0.5, 0.0, 2.0), 0.5)]
triangles = [Triangle(v = [Vec3(0.0, 1.0, 2.0), Vec3(1.0, -1.0, 2.0), Vec3(-1.0, -1.0, 2.0)])]

camera_origin = Vec3(0.0, 0.0, 0.0)
camera_length = 1.0
camera = Camera(width, height, camera_origin, camera_length)

for y in range(height, 0, -1):
	for x in range(0, width):
		colour = Vec3(0, 0, 0)
		for s in range(0, no_of_samples):
			ray = camera.getRay(x, y)
			for triangle in triangles:
				temp = triangle.hit(ray, 0.0, 1000.0)
				if temp[0]:
					colour = colour + ((temp[1].normal + Vec3(1.0, 1.0, 1.0)) / 2.0) * 255.0
					break
				else:
					colour = colour + Vec3(0, 0, 0)
		pixels.append(colour/no_of_samples)

print("Actual length:", len(pixels), "Expected Length:", width * height)
ppmWriter(pixels, "temp.ppm", width, height)
