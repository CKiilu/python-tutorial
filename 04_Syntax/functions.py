#!/usr/bin/python3

def main():
	action()
	action(4)
	action(5)
	action(15)

def action(c = 10):
	for c in range(c, 20):
		print(c, end=" ")
	print()

if __name__ == "__main__":
	main()