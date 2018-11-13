from vec3 import Vec3
from ray import Ray
from hit_record import Hit_Record
from ppm_writer import ppmWriter
from camera import Camera
from hitable import Hitable
from hitable_list import Hitable_List
from sphere import Sphere
from triangle import Triangle
from model import Model
from material import *

from math import sqrt
from random import random

def backgroundColour(ray):
	h = ray.getDirection().y
	h = (h + 1.0)/2.0
	white = Vec3(1.0, 1.0, 1.0)
	blue = Vec3(0.47, 0.7, 1.0)
	return blue * h + white * (1.0 - h)

def rayTrace(models, ray, depth):
	if depth == 0:
		return backgroundColour(ray)
	colour = Vec3()
	ray_info = models.hit(ray, 0.0001, 1000.0)
	if ray_info[0]:
		material_info = ray_info[1].material.scattered(ray, ray_info[1])
		if material_info[0]:
			colour = rayTrace(models, material_info[1], depth - 1)
			diffuse_colour = material_info[2]
			colour = Vec3(colour.x * diffuse_colour.x, colour.y * diffuse_colour.y, colour.z * diffuse_colour.z)
	else:
		colour = backgroundColour(ray)
	return colour

width = 1280
height = 720
no_of_samples = 20

pixels = []
triangles = [Triangle(v = [Vec3(0.0, 1.0, 2.0), Vec3(1.0, -5.0, 5.0), Vec3(-1.0, -5.0, 0.0)], material = Lambert(Vec3(0.1, 0.2, 0.8)))]
spheres = [Sphere(Vec3(0.60, 0.0, 2.0), 0.5, Lambert(Vec3(0.2, 0.9, 0.55))), Sphere(Vec3(0.5, -100.0, 2.0), 99.5, Lambert(Vec3(1.0, 1.0, 1.0))), Sphere(Vec3(-0.60, -0.2, 2.0), 0.5, Lambert(Vec3(0.89, 0.65, 0.55)))]
hitable_list = Hitable_List(spheres + triangles)
model = Model(material = Metal(Vec3(0.8, 0.8, 0.82), 0.3))
model.readObj("../temp_obj.obj")
hitable_list = Hitable_List([model])

camera_origin = Vec3(0.0, 0.0, -2.0)
camera_length = 0.8
camera = Camera(width, height, camera_origin, camera_length)

for y in range(height, 0, -1):
	for x in range(0, width):
		colour = Vec3(0, 0, 0)
		for s in range(0, no_of_samples):
			ray = camera.getRay(x, y)
			colour = colour + rayTrace(hitable_list, ray, 5)
		pixels.append(colour/no_of_samples * 255.0)

print("Actual length:", len(pixels), "Expected Length:", width * height)
ppmWriter(pixels, "temp.ppm", width, height)
