#!/usr/bin/python3

def main():
	test = open('words.txt')
	sentence = input("Input sentence.")
	words = sentence.split()
	for x in test.readlines():
		for y in words:
			if x == y:
				continue
			else:
				print y

if __name__ == "__main__":
	main()