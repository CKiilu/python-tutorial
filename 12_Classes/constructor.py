#!/usr/bin/python3

#Basic class definition

class Duck:
	#Constructor method
	def __init__(self, value):
		print('Constructor.')
		self._v = value


	
	def quack(self):
		print('Quack!', self._v)

	def walk(self):
		print('Waddles.', self._v)


def main():
	donald = Duck(42)
	donald.quack()
	donald.walk()
	frank = Duck(">9000")
	frank.quack()
	frank.walk()

if __name__ == "__main__":
	main()