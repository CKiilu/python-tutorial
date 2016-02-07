#!/usr/bin/python3

def main():
	testfunc(5, 7, 9, 42, 43, 55, one = 1, two = 2, three = 3)
	namedargs(1,2,3,4,5,6, seven = 7, eight = 8, nine = 9)

def testfunc(x, y, z, *args, **kwargs):
	print("This is a test function.", x, y, z, args, kwargs['one'], kwargs['two'], kwargs['three'])
def namedargs(x, y, z, *args, **kwargs):
	for k in kwargs: print(k, kwargs[k])
	for n in args: print(n)


if __name__ == "__main__":
	main() 