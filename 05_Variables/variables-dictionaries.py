#!/usr/bin/python3

def main():
	tion = {"one": 1, "two": 2, "three": 3, "four": 4}
	for k in sorted(tion.keys()):
		print(k, tion[k])
	print()

	d = dict(
			one = 1, two = 2, three = 3, four = 4, five = 5, six = 6
		)
	for k in sorted(d.keys()):
		print(k, d[k])
	print()
	
	d["seven"] = 7
	for k in sorted(d.keys()):
		print(k, d[k])

if __name__ == "__main__":
	main()