#!/usr/bin/python

def main():
	choices = dict(
			one = "first",
			two = "second",
			three = "third",
			four = "fourth",
			five = "fifth",
			six = "sixth",
			seven = "seventh",
			eight = "eighth",
			nine = "ninth",
			ten = "tenth "
		)
	v = "four"
	print(choices.get(v, "other"))

if __name__ == "__main__":
	main()
