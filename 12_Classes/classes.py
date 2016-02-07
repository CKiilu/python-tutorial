#!/usr/bin/python3

#Basic class definition

class Duck:
	def quack(self):
		print('Quack!')

	def walk(self):
		print('Waddles.')


def main():
	donald = Duck()
	donald.quack()
	donald.walk()

if __name__ == "__main__":
	main()