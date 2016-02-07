#!/usr/bin/python3
def main():
	testfunc()
	popo()
	arg(75, 34, 22)
	defaultargs(42)

def testfunc():
	print("This is a test function.")

def arg(num, ano, more):
	# Passing args
	print("This is a test func", num, ano, more)

def defaultargs(x, y = 23, k ="coyote"):
	print(x, y, k)

def popo():
	# use pass when you need a function but
	# have no data for it yet
	pass

if __name__ == "__main__":
	main()