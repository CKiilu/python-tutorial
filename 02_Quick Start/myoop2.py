#!/usr/bin/python3

#Creating classes with inheritance
"""Animals class"""
class Animal():
	def move(self): return self.action['move']
	def make_sound(self): return self.action['sound']
	def sleep_time(self): return self.action['time']
	def keeping_warm(self): return self.action['warmth']
"""Humans class"""
class Human(Animal):
	action = dict(
		move = "Bipedal walking.",
		sound = "Speaking words.",
		time = "At night.",
		warmth = "Wearing clothes."
		)
"""Cat class"""
class Cat(Animal):
	action = dict(
		move = "Quadrupedal walking.",
		sound = "Meow!",
		time = "All day.",
		warmth = "Fur."
		)
"""Lion class"""
class Lion(Animal):
	action = dict(
		move = "Quadrupedal walking.",
		sound = "Roar!",
		time = "All day.",
		warmth = "Fur."
		)
"""Things happening in the savanna"""
def savanna(lion):
	print(lion.make_sound())
	print(lion.sleep_time())
"""Things happening in the house"""
def house(human):
	print(human.make_sound())
	print(human.sleep_time())
"""Calling the funtions"""
def main():
	Juma = Human()
	Maria = Human()
	Fluffy = Lion()
	white_cat = Cat()

	print("In the savanna: ")
	for x in (Fluffy, Maria):
		savanna(x)

	print("In the house: ")
	for y in (Maria, white_cat):
		house(y)

if __name__ == '__main__':	main()