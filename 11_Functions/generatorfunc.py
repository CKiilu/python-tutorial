#!/usr/bin/python3

def main():
	print("This is the generator file.")
	for i in inclusive_range(0, 25, 1):
		print(i, end = " ")
	print()

	for x in rng(42, 48, 2, 3):
		print(x, end = " ")
	print()

def inclusive_range(start, stop, step):
	"""Creating a generator"""
	i = start
	while i <= stop:
		yield i
		i += step

def rng(*args):
	"""Generator func exactly like range but inclusive"""
	numargs = len(args)
	if numargs < 1: raise TypeError("Requires at least one argument.")
	elif numargs == 1:
		start = 0
		step = 1
		stop = args[0]
	elif numargs == 2:
		step = 1
		(start, stop) = args
	elif numargs == 3:
		(start, stop, step) = args
	else: raise TypeError("Inclusive range epected three arguments at most, got {}.".format(numargs))

	x = start
	while x <= stop:
		yield x
		x += step


if __name__ == "__main__":
	main()