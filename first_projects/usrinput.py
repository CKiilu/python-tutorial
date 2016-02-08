#!/usr/bin/python3

def main():
	sentence = input("Input sentence.")
	words = sentence.split()
	test = open('words.txt').readlines()
	test_file = list(map(lambda x : x.strip(), test))
	for x in words:
		if x in test_file:
				continue
		else:
			print(x)
if __name__ == "__main__":
	main()