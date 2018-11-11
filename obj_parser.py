from vec3 import Vec3

class Model:
	name = ""
	vertices = [] # stored as list of Vec3
	tex_coords = [] # stored as list of Vec3
	normals = [] # stored as list of Vec3 - 
	faces = [] # stored as list of list of integers - [[v1, vt1, vn1], [v2, vt2, vn2], ..... , [vn, vtn, vnn]]
	def __init__(self, name = "", vertices = [], tex_coords = [], normals = [], faces = []):
		self.name = name
		self.vertices = vertices
		self.tex_coords = tex_coords
		self.normals = normals
		self.faces = faces

	def objParse(self, path):
		with open(path, "rt") as file:
			for line in file:
				print(line, end = "")
				if line.startswith("v "):
					info = line.split()
					self.vertices.append(Vec3(float(info[1]), float(info[2]), float(info[3])))
				elif line.startswith("vt "):
					info = line.split()
					self.tex_coords.append(Vec3(float(info[1]), float(info[2]), 0.0))
				elif line.startswith("vn "):
					info = line.split()
					self.normals.append(Vec3(float(info[1]), float(info[2]), float(info[3])))
				elif line.startswith("f "):
					info = line.split()
					indices_of_vertices_of_face = []
					for i in info:
						if i != "f":
							vertex_data = []
							for j in i.split("/"):
								vertex_data.append(j)
							indices_of_vertices_of_face.append(vertex_data)
					self.faces.append(indices_of_vertices_of_face)
				elif line.startswith("o"):
					info = line.split()
					self.name = info[1]
				else:
					continue
	def writeObj(self, path):
		with open(path, "wt") as file:
			file.write("o " + self.name + "\n")
			for i in self.vertices:
				file.write("v ")
				file.write(str(i.x) + " " + str(i.y) + " " + str(i.z))
				file.write("\n")
			for i in self.tex_coords:
				file.write("vt ")
				file.write(str(i.x) + " " + str(i.y))
				file.write("\n")
			for i in self.normals:
				file.write("vn ")
				file.write(str(i.x) + " " + str(i.y) + " " + str(i.z))
				file.write("\n")
			for i in self.faces:
				file.write("f ")
				line = ""
				for vertex_data in i:
					line = line + str(vertex_data[0]) + "/" + str(vertex_data[1]) + "/" + str(vertex_data[2]) + " "
				file.write(line)
				file.write("\n")

model = Model()
model.objParse("../temp_obj.obj")
print(model.faces)
model.writeObj("../temp_obj_mine.obj")
