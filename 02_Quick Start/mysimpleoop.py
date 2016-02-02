#!/usr/bin/python3

#fibonacci series
#Sum of two elements defines the next set

class Fibo():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def process(self):
		while(True):
			yield(self.b)
			self.a, self.b = self.b, self.a + self.b

obj = Fibo(0, 100)
for j in obj.process():
	if j > 1000:
	 break
	print(j)