#!/usr/bin/python3

#Basic class definition

class Duck:
	def __init__(self, **kwargs):
		self.variables = kwargs

	def quack(self):
		print('Quack!')

	def walk(self):
		print('Waddles.')

	def set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)


def main():
	james = Duck()
	james.set_variable('color', 'red')
	print(james.get_variable('color'))


if __name__ == "__main__":
	main()