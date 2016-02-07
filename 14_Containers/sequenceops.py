#!/usr/bin/python3

def main():
	t = tuple(range(10))
	print(type(t), t)
	print("Presence of 5", 5 in t)
	print("Presence of 10", 10 in t)
	print("Unpresent number (not)", 50 not in t)

	x = list(range(10))
	print(x)
	x[7] = 42
	print(x)
	print("Count 5", x.count(5))
	print("Index of 4", x.index(4))
	# Add an element to beginning of list
	x.append("@Scurrae")
	print(x)
	# Add a number of elements to list
	x.extend(range(2))
	print(x)
	# Insert element at position
	x.insert(4, 44)
	print(x)
	# Remove specific element
	x.remove(0)
	# Delete element at index
	del x[11]
	# Remove item at end of list
	x.pop()
	# Remove itme from beginning
	x.pop(0)
	print(x)


if __name__ == "__main__":
	 main()