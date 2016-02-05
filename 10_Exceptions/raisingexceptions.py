#!/usr/bin/python3

def main():
	try:
		for line in readfile('lines.txt'):
			print(line.strip())
	except IOError as e:
		print('Cannot read file', e)
	except ValueError as e:
		print('Bad file name', e)

def readfile(filename):
	if filename.endswith('.txt'):
		text = open(filename)
		return text.readlines()
	else: raise ValueError('Filename must end with .txt')

if __name__ == "__main__":
	main()