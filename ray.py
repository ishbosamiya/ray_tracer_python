from vec3 import Vec3

class Ray:
	def __init__(self, origin = Vec3(0, 0, 0), direction = Vec3(0, 0, 0)):
		self.origin = origin
		self.direction = direction

	def __str__(self):
		return "(" + str(self.origin) + ", " + str(self.direction) + ")"

	def getOrigin(self):
		return self.origin
	def getDirection(self):
		return self.direction
	def pointAtParameter(self, t):
		return self.origin + self.direction * t

