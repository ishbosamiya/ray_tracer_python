from vec3 import Vec3

class Ray:
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction

	def __str__(self):
		return "(" + str(self.origin) + ", " + str(self.direction) + ")"

	def getOrigin(self):
		return self.origin
	def getDirection(self):
		return self.direction
	def pointAtParameter(self, t):
		return self.origin + t * self.direction

r = Ray(Vec3(0, 1, 5), Vec3(1,2,3))
print(r)
