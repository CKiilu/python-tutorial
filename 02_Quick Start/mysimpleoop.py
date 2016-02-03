#!/usr/bin/python3

#fibonacci series
#Sum of two elements defines the next set

class Fibo():
	def __init__(self, a, b):
		self.a = b
		self.b = b

	def series(self):
		while(True):
			yield(self.b)
			self.a, self.b = self.b, self.a + self.b

fido = Fibo(0, 100)
for x in fido.series():
	if x > 1000:
	 break
	print(x)