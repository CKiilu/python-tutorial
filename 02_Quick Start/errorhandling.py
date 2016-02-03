#! /usr/bin/python3

#testing readin the 'lines.txt' file
#filename is misspelt
try:
	text = open('hflines.txt')
	for line in text.readlines():
		print (line, end="")
except IOError as e:
	print("Error!\t{}".format(e))

print("Catch block passed.")