#!/usr/bin/python3

def main():
	# Split works using whitespace
	s = "The jester lives forever!"
	n = s.split()
	print(n)
	for w in n:
		print(w)
	# Joining strings
	# Joing with colon between
	print(':'.join(n))
	# Joining with spacing
	print(' '.join(n))

if __name__ == "__main__":
	main()