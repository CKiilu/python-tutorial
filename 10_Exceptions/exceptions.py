#!/usr/bin/python3

def main():
	meth1()
	print("")
	meth2()

def meth1():
	try:
		text = open('lines.txt')
	except IOError as e:
		print("Could not open file: ", e)
	else:
		for line in text: print(line.strip())

def meth2():
	try:
		text = open('lines.txt')
		for line in text: print(line.strip())
	except IOError as e:
		print("Could not open file: ", e)
		

if __name__ == "__main__":
	main()