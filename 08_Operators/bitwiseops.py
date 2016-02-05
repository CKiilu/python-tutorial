#!/usr/bin/python3

def main():
	b(34)
	prod()
# Print n in 8-bit 
def b(n):
	print('{:08b}'.format(n))

def prod():
	x, y = 0x55, 0xaa
	print(x, y)
	x, y = b(0x55), b(0xaa) 
	print(x, y)

def ops():
	# or
	b(x | y)
	# and
	b(x & y)
	# exclusive or
	b(x ^ y)
	# shift 4 bits left
	b(x << 4)
	# shift 4 bits right
	b(x >> 4)
	# one's complement
	b(~ x)


if __name__ == "__main__":
	main()