#!/usr/bin/python3
 
 # There are only two number types in python
def main():
	"""Number types"""
	# 42; the answer to life, the universe and anything
	x = 42
	print(type(x), x)
	# type (class = int)
	y = 44.4
	print(type(y), y)
	# type (class = float)
	other()

def other():
	"""Other useful functions"""
	y = 44.4
	z = 5
	#Actual answer
	print("Actual: ", y / z)
	#Round down while dividing
	print("Round down: ", y // z)
	#round off while dividing
	print("Round off: ", round(y / z))
	#remainder/ modulus
	print("Modulo: ", y % z)
	#forcing float to become int
	print("int to float: int(x)", int(44.4))

if __name__ == "__main__":
	main() 