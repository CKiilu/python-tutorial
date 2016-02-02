#!/usr/bin/python3

def isprime(n):
	if n == 1:
		print("1 is special.")
		return False
	for x in range (2, n):
		if n % x == 0:
			print("{} equals {} x {}".format(n, x, n // x))
			return False

	else:
		print('{} is a prime number.'.format(n))
		return True

for x in range(0, 100):
	isprime(x)