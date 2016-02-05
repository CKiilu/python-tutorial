#!/usr/bin/python3

def main():
	lst()

def lst():
	listc = [1,2,3,4,5,6,7,8,9,10]
	print(listc[9])
	# Slice
	print(listc[0:5])
	# Ranges in python are non-inclusive
	# That is, last number is not included
	for i in range(0,10):
		print(i)

	# Shorthand to add values to list c
	listc[:] = range(100)
	print(listc)
	print(listc[42])
	# Slice index 27 to 43
	print(listc[27:43])
	# Slice index 27 to 43
	# in slices of three
	print(listc[27:43:3])

	# Reassigning list values
	listc[27:43:3] = (99,99,99,99,99,99)
	print(listc)


if __name__ == "__main__":
	main()