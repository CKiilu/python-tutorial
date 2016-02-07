#!/usr/bin/python3

#Basic class definition

class Duck:
	def __init__(self, **kwargs):
		self.variables = kwargs

	def quack(self):
		print('Quack!')

	def walk(self):
		print('Waddles.')

	def set_color(self, color):
		self.variables['color']  = color

	def get_color(self):
		return self.variables.get('color', None)
		
def main():
	donald = Duck(color = 'blue')
	james = Duck()
	print(donald.get_color())
	print(james.get_color())


if __name__ == "__main__":
	main()