#!/usr/bin/python3
import re

def main():
	meth1()
	meth2()

def meth1():
	text = open('raven.txt')
	for line in text:
		print(re.sub("(Len|Neverm)ore", "jester", line), end="")

def meth2():
	text = open('raven.txt')
	for line in text:
		match = re.search("(Len|Neverm)ore", line)
		if match:
			print(line.replace(match.group(), "jester"), end="")

if __name__ == "__main__":
	main()