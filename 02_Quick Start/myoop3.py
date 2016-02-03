#!/usr/bin/python3


"""IMPORTANT"""
#View, Model  and Controller pattern of OOP

# VIEW

#Creating classes with inheritance
"""Animals class"""
class Animal():
	def move(self): return self.__doAction['move']
	def make_sound(self): return self.__doAction['sound']
	def sleep_time(self): return self.__doAction['time']
	def keeping_warm(self): return self.__doAction['warmth']

	# Difference
	def __doAction(self, act):
		if action in self.action:
			return self.action[act]
		else:
			return 'The {} has no {}'.format(self.animalName, action)

	def animalName(self):
		return self.__class__.__name__.lower()
# MODEL

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

# CONTROLLER

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