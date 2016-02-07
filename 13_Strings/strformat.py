#!/usr/bin/python3

def main():
	s = "The {} jesters return {} days from now."
	a, b, c = 4, 42, 16 
	print(s.format(a, b))
	print("{0} x {0} is {2} not {1}.".format(a, b, c))
	print("Why do you {a} all the {b}?".format(a = "play", b = "time"))
	d = dict(
			a = "play",
			b = "time"
		)
	print("Why do you {a} all the {b}?".format(**d))

if __name__ == "__main__":
	main()