from time import time

class Completion_Bar:
	current_value = 1
	def __init__(self, max_value, width):
		self.max_value = max_value
		self.width = width
	def update(self):
		width = self.width
		d = self.current_value/self.max_value
		print("\r", end = "")
		for i in range(0, int(d * width)):
			print("#", end = "")
		for i in range(int(d * width), width):
			print("-", end = "")
		print(" %01f" % (Completion_Bar.time_lapse(d)/100000000.0), end = " ")
		if self.current_value >= self.max_value:
			print()
		self.current_value += 1
	def time_lapse(d):
		start_time=time()
		current_time=time()
		end_time=(1*current_time)/d
		time_remaining=end_time-current_time
		return time_remaining
