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

<<<<<<< HEAD
r = Ray(Vec3(0, 1, 5), Vec3(1,2,3))
print(r)
=======
v1 = Vec3(1, 2, 3)
v2 = Vec3(4, 5, 6)
print(v1.normalized())
print(v2.normalized())
print(v1.length())
print(v2.length())
print(v1.dot(v2))
print(v1.cross(v2))
print(v1 + v2)
print(v1 - v2)
print(v1 * 5)
print(v1 / 5)
>>>>>>> origin/master
