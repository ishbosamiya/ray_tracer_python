from vec3 import Vec3
from triangle import Triangle
from hitable import Hitable
from hitable_list import Hitable_List
from material import *

class Model(Hitable):
	name = ""
	vertices = [] # stored as list of Vec3
	tex_coords = [] # stored as list of Vec3
	normals = [] # stored as list of Vec3 - 
	faces = [] # stored as list of list of integers - [[v1, vt1, vn1], [v2, vt2, vn2], ..... , [vn, vtn, vnn]]
	material = Lambert()
	has_tex_coords = False
	has_normals = False
	def __init__(self, name = "", vertices = [], tex_coords = [], normals = [], faces = [], material = Lambert()):
		self.name = name
		self.vertices = vertices
		self.tex_coords = tex_coords
		self.normals = normals
		self.faces = faces
		self.material = material

	def readObj(self, path):
		with open(path, "rt") as file:
			for line in file:
				if line.startswith("v "):
					info = line.split()
					self.vertices.append(Vec3(float(info[1]), float(info[2]), float(info[3])))
				elif line.startswith("vt "):
					info = line.split()
					self.tex_coords.append(Vec3(float(info[1]), float(info[2]), 0.0))
					self.has_tex_coords = True
				elif line.startswith("vn "):
					info = line.split()
					self.normals.append(Vec3(float(info[1]), float(info[2]), float(info[3])))
					self.has_normals = True
				elif line.startswith("f "):
					info = line.split()
					indices_of_vertices_of_face = []
					for i in info:
						if i != "f":
							vertex_data = []
							for j in i.split("/"):
								if j == '':
									vertex_data.append('')
								else:
									vertex_data.append(int(j) - 1)
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
			if self.has_tex_coords:
				for i in self.tex_coords:
					file.write("vt ")
					file.write(str(i.x) + " " + str(i.y))
					file.write("\n")
			if self.has_normals:
				for i in self.normals:
					file.write("vn ")
					file.write(str(i.x) + " " + str(i.y) + " " + str(i.z))
					file.write("\n")
			for i in self.faces:
				file.write("f ")
				line = ""
				for vertex_data in i:
					if vertex_data[0] == '':
						line += str('') + "/"
					else:
						line += str(vertex_data[0] + 1) + "/"
					if vertex_data[1] == '':
						line += str('') + "/"
					else:
						line += str(vertex_data[1] + 1) + "/"
					if vertex_data[2] == '':
						line += str('') + "/"
					else:
						line += str(vertex_data[2] + 1) + " "
				file.write(line)
				file.write("\n")

	def getFaceData(self, index, data_type = "v"):
		if data_type == "v":
			data = []
			for i in self.faces[index]:
				data.append(self.vertices[i[0]])
			return data
		elif data_type == "vt" and self.has_tex_coords:
			data = []
			for i in self.faces[index]:
				data.append(self.tex_coords[i[1]])
			return data
		elif data_type == "vn" and self.has_normals:
			data = []
			for i in self.faces[index]:
				data.append(self.normals[i[2]])
			return data

	def hit(self, ray_in, t_min, t_max):
		list_of_triangles = []
		for face in self.faces:
			vertices = self.getFaceData(self.faces.index(face))
			for triangle_no in range(0, len(vertices) - 2):
				list_of_triangles.append(Triangle(v = [vertices[0], vertices[triangle_no + 1], vertices[triangle_no + 2]], material = self.material))
		hitable_list = Hitable_List(list_of_triangles)
		return hitable_list.hit(ray_in, t_min, t_max)
