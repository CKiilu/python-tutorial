#!/usr/bin/python3

def main():
	print(testfunc())
	for n in testfunc():
		print(n)

def testfunc():
	return range(10,25)

if __name__ == "__main__":
	main()