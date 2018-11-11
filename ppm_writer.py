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
			f.write(str(temp.x) + " " + str(temp.y) + " " + str(temp.z) + " ")
		f.write("\n")
	f.close()

pixels = [Vec3(255, 0, 0), Vec3(0, 255, 0), Vec3(0, 0, 255), Vec3(255, 255, 0), Vec3(255, 255, 255), Vec3(0, 0, 0)]

ppmWriter(pixels, "temp.ppm", 3, 2)
