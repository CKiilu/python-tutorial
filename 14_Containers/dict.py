#!/usr/bin/python3

def main():
	# Dictionary = hashlist
	# Tedious dictionary
	d = {'one': 1, 'two' : 2, 'three' : 3}
	print(d)
	# Easy dictionary
	t = dict(four = 4, five = 5, six = 6)
	print(t)
	# Merging dictionaries
	x = dict(d, **t)
	print(x)
	# Presence and absence
	print('ten' in d)
	print('one' in d)
	# Printing keys and values
	for k, v in x.items():
		print(k)
		print(v)
		print(k, v)

	# Get methods
	print('Four', x.get('four'))
	# Get method with default value
	print('Ten', x.get('ten', 'Not Found'))

if __name__ == "__main__":
	main() 