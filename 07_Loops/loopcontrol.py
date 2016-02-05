 #!/usr/bin/python3

def main():
 	s = "This is my dog."
 	for c in s:
 		if c == "i": continue
 		print(c, end="")
 	print()

 	for w in s:
 		if w == "i": break
 		print(w, end="")
 	print()

 	for j in s:
 		print(j)
 	else:
 		print()

if __name__ == "__main__":
 	main()