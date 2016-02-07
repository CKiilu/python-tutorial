#!/usr/bin/python3

def main():
	testfunc(1,2,3,4,5,6,7,8,9,10)

def testfunc(x, y, z, *args):
	"""Optional args"""
	print("This is a test func.")
	print( x, y, z, args)
	for n in args:
		print(n, end = " ")
	print("")	
if __name__ == "__main__":
	main()