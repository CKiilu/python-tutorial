#!/usr/bin/python3

#Creating classes with inheritance

class Animal():
	def move(self): return self.strings['move']
	def make_sound(self): return self.strings['sound']
	def sleep_time(self): return self.strings['time']
	def keeping_warm(self): return self.strings['for warmth']

class Human(Animal):
	strings = dict(
		move = "Bipedal walking."
		make_sound = "Speaking words."
		sleep_time = "At night."
		keeping_warm = "Wearing clothes."
		)

class Cat(Animal):
	strings = dict(
		move = "Quadrupedal walking."
		make_sound = "Meow!"
		sleep_time = "All day."
		keeping_warm = "Fur."
		)
