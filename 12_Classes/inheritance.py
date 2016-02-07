#!/usr/bin/python3

class Animal:
	def talk(self):
		print("I have something to say.")
	def walk(self):
		print("I like to move it move it!")
	def warmth(self):
		print("Who ain't feelin' warm here?")

class Duck(Animal):
	def walk(self):
		super().walk()
		print("Waddles away.")

	def quack(self):
		print("Quuuack!")

class Dog(Animal):
	pass

def main():
	donald = Duck()
	spike = Dog()
	spike.warmth()
	donald.quack()
	donald.walk()
	donald.talk()
	donald.warmth()

if __name__ == "__main__":
	main()