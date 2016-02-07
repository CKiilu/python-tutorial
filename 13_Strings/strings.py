#!/usr/bin/python3

def main():
	# Strings can be manipulated directly since 
	# they're objects
	print("jump".upper())
	# String methods 
	s = "Long live Scurrae, The Jester!"
	print(s.capitalize())
	print(s.upper())
	print(s.lower())
	print("JumP".swapcase())
	print(s.find('iv'))
	print(s.replace('Long live', 'Vivat et'))
	# Remove whitespace
	print('    jump      '.strip())
	# Remove whitespace at end of line only
	print('     jump     '.rstrip())
	# Remove \n only
	print('jump\n'.rstrip('\n'))
	# Test for alphanumeric characters only
	print(s.isalnum())
	# Test for alphabetic characters only
	print(s.isalpha())
	# Test for numbers only
	print(s.isdigit())
	# Test for printable characters only
	print(s.isprintable())



if __name__ == "__main__":
	main()