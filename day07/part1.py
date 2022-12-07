#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	total = 0
	depth = list()
	check_size = lambda x: x if x <= 100000 else 0
	for line in input_lines:
		if line[0:4] == "$ cd":
			if line == "$ cd ..":
				total += check_size(depth.pop())
			else:
				depth.append(0)
		elif ord("0") <= ord(line[0]) <= ord("9"):
			depth = [i + int(line.split()[0]) for i in depth]
	for i in range(0,len(depth)):
		total += check_size(depth.pop())
	
	
	return total

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 95437,"Test failed, expected 95437, result "+str(test_value)
	print(main("INPUT"))
