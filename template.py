#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	return 	

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 0,"Test failed, expected X, result "+str(test_value)
	print(main("INPUT"))
