#!/usr/bin/python3

import re

def main():
	meth1()
	meth2()
	meth3()

def meth1():
	print("\nMethod one\n")
	text = open('raven.txt')
	for line in text:
		if re.search('(Len|Neverm)ore', line):
			print(line, end="")

def meth2():
	print("\nMethod two\n")

def meth3():
	print("\nBest practice\n")


if __name__ == "__main__":
	main()