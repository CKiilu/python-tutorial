#!/usr/bin/python3

def main():
	if1(1, 1)
	if2(1, 3)
	if3(3, 1)
	if4(4, 9)

def if1(a, b):
	if a == b:
		print('{} is equal to {}.'.format(a, b))

def if2(a, b):
	if a < b:
		print('{} is less than {}.'.format(a, b))
	else:
		print("{} is greater than {}. ".format(a, b))

def if3(a, b):
	if a == b:
		print('{} is equal to {}.'.format(a, b))
	elif a < b:
		print('{} is less than {}.'.format(a, b))
	else:
		print("{} is greater than {}.".format(a, b))

def if4(a, b):
	s = "less than" if a < b else "greater than"
	print("{} is {} {}.".format(a, s, b))

if __name__ == "__main__":
	main()