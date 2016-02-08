#!/usr/bin/python3

import re

def main():
	print("Do you wish to store or search for a file?")
	choice = input("Type 'search' or 'store' to perform a function.")
	if (choice == "search"):
		search()
	elif(choice == "store"):
		store()
	else:
		raise IOError('Input either store or search')

def store():
	storage = input('What do you wish to save?')
def search():
	searching = input('What do you wish to find?')



if __name__ == "__main__":
	main()