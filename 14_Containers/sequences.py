#!/usr/bin/python3

def main():
	# tuple - immutable
	# Created with commas
	# Parentheses are for format
	t = 1, 2, 3, 4, 5
	s = (6, 7, 8, 9, 10)
	a = (1,)
	b = tuple(range(10))
	for c in t:
		print(c)
	print("Length", len(t))
	print("Minimum", min(t), min(s))
	print("Maximum", max(t), max(s))

	# list - mutable(Can be changed)
	# Created with brackets
	# Uses same functions as lists
	q = [2,3,7,5,3,5,9]
	r = list(range(10))

if __name__ == "__main__":
	main()