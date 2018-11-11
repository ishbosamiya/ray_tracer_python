from vec3 import Vec3

def getIndex(x, y, width):
	return (x + y * width)

def ppmWriter(pixels, path, width, height):
	f = open(path, "wt")
	f.write("P3\n")
	f.write(str(width) + " " + str(height) + "\n")
	f.write("255\n")
	for y in range(0, height):
		for x in range(0, width):
			temp = pixels[getIndex(x, y, width)]
			if temp.x < 0:
				temp.x = 0
			if temp.y < 0:
				temp.y = 0
			if temp.z < 0:
				temp.z = 0
			f.write(str(int(temp.x)) + " " + str(int(temp.y)) + " " + str(int(temp.z)) + " ")
		f.write("\n")
	f.close()
