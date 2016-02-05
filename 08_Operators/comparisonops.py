#!/usr/bin/python3

def main():
	x, y = 5, 6
	print("x: ", id(x),"y: ", id(y))
	print("x is y: ", x is y)
	print("x is not y: ", x is not y)

	# Elements with same value in different
	# lists have different ids

if __name__ == "__main__":
	main()