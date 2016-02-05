#!/usr/bin/python3

def main():
	#basics
	a, b = 4, 5
	c = a + b
	d = a * b
	e = a / b
	f = a - b
	g = a % b


	# getting both quotient and remainder at once
	h = divmod(a, b)
	print("Sum", c)
	print("Product", d)
	print("Quotient", e)
	print("Difference", f)
	print("Modulus", g)
	print("Divmod", h)

	# As well as +=, -=, *=, /=, //=


if __name__ == "__main__":
	main()