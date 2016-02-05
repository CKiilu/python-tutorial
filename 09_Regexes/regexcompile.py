#!/usr/bin/python3

import re

def main():
	text = open('raven.txt')
	match = re.compile('(Len|Never)ore', re.IGNORECASE)
	for line in text:
		if re.search(match, line):
			print(match.sub("jester", line), end="")

if __name__ == "__main__":
	main()