class Completion_Bar:
	current_value = 1
	def __init__(self, max_value):
		self.max_value = max_value
	def update(self):
		width = 60
		d = self.current_value/self.max_value
		print("\r", end = "")
		for i in range(0, int(d * width)):
			print("#", end = "")
		for i in range(int(d * width), width):
			print("-", end = "")
		if self.current_value >= self.max_value:
			print()
		self.current_value += 1
