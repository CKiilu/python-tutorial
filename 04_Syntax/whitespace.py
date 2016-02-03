#!/usr/bin/python3

def main():
	print("Normal indent.")
  #print("Bad indent")
  #Code won't run due to error
  	print("Correct indentation.")
  	other()

def other(): print("Just a line of text.")

if __name__ == "__main__":
	main()