#!/usr/bin/python3

#Creating classes with inheritance
"""Animals class"""
class Animal():
	def move(self): return self.action['move']
	def make_sound(self): return self.action['sound']
	def sleep_time(self): return self.action['time']
	def keeping_warm(self): return self.action['for warmth']
"""Humans class"""
class Human(Animal):
	action = dict(
		move = "Bipedal walking.",
		make_sound = "Speaking words.",
		sleep_time = "At night.",
		keeping_warm = "Wearing clothes."
		)
"""Cat class"""
class Cat(Animal):
	action = dict(
		move = "Quadrupedal walking.",
		make_sound = "Meow!",
		sleep_time = "All day.",
		keeping_warm = "Fur."
		)
"""Lion class"""
class Lion(Animal):
	action = dict(
		move = "Quadrupedal walking.",
		make_sound = "Roar!",
		sleep_time = "All day.",
		keeping_warm = "Fur."
		)
"""Things happening in the savanna"""
def savanna(Lion):
	print(Lion.make_sound())
	print(Lion.sleep_time())
"""Things happening in the house"""
def house(Human):
	print(Human.make_sound())
	print(Human.sleep_time())
	print(Cat.make_sound())
	print(Cat.sleep_time())
"""Calling the funtions"""