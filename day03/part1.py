#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	priorities = 0
	calcprior = lambda p: ord(p) - 96 if ord(p) >= 97 else ord(p) - 38
	for line in input_lines:
		compart1 = set(line[:len(line)//2])
		compart2 = set(line[len(line)//2:])
		priorities += calcprior( str(compart1 & compart2)[2] )
		
	return priorities

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 157,"Test failed, expected 157, result "+str(test_value)
	print(main("INPUT"))
