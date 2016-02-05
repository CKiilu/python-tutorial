#!/usr/bin/python3

def main():
	# Looping using external file
	text = open('lines.txt')
	for line in text.readlines():
		print(line, end = "")

	# Looping containers(lists, tuples, strings)
	for x in [1,2,3,4,5]:
		print(x, end = " ")
	print()
	for y in "jump":
		print(y)


if __name__ == "__main__": main()