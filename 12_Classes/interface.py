#!/usr/bin/python3

#Basic class definition

class Duck:
	def quack(self):
		print('Quack!')
	def walk(self):
		print('Waddles.')
	def bark(self):
		print("The duck cannot bark.")
	def fur(self):
		print("The duck has feathers.")

class Dog:
	def bark(self):
		print("woof!")
	def fur(self):
		print("The dog has brown and white fur.")
	def walk(self):
		print("Walks like a dog.")
	def quack(self):
		print("The dog does not quack.")


def main():
	donald = Duck()
	spike = Dog()
	in_the_forest(donald)
	in_the_pond(spike)

def in_the_forest(dog):
	# Interface
	dog.bark()
	dog.walk()

def in_the_pond(duck):
	# Interface
	duck.bark()
	duck.walk()

if __name__ == "__main__":
	main()