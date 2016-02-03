#!/usr/bin/python3

def main():
	#tuple, it's immutable
	x = (1, 2, 3)
	print(type(x), x)
	#list, it's mutable
	y = [4, 5, 6]
	print("Initial: ", type(y), y)
	# add something to end
	y.append(1)
	print("Add to end: ", type(y), y)
	#add something at beginning
	y.insert(2, 7)
	print("Add to beginning: ", type(y), y)


	string()

	charprint()


def string():
	z = "scurrae"
	# Slicing strings
	print("Slice of scurrae (z[1:4]): ",z[1: 4])

def charprint():
	"""Printing all elements in a list or string"""
	a = (1, 3, 4 , 5, 6)
	for c in a:
		print(c)

# String on multi-line
	b = "blaze up the fire"
	for c in b:
		print(c)
	

if __name__ == "__main__":
	main()