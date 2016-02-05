#!/usr/bin/python3

# Enumeration of values in a for loop

def main():
	text = open('lines.txt')
	for index, x in enumerate(text.readlines()):
		print(index, x, end="")

	for v, k in enumerate("I'm going to swing on the chandelier!"):
		print(v, k)

	# Finding number of a letter in a string
	q = "Everywhere I go I'm just..."
	z = q.lower()
	count = 0
	for i, c  in enumerate(z):
		if c == "e":
			print("Index {} is an e.".format(i))
			count += 1
	print(count)

if __name__ == "__main__":
	main() 