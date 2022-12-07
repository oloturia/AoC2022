#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	check_file = lambda sz: int(sz) if ord("0") <= ord(sz[0]) <= ord("9") else 0
	used_space = 0
	for line in input_lines:
		used_space += check_file(line.split()[0])
		
	size_to_delete = 30000000 - (70000000 - used_space)
	smallest = used_space
	depth = list()
	check_size = lambda x: x if x >= size_to_delete and x < smallest else smallest
	for line in input_lines:
		if line[0:4] == "$ cd":
			if line == "$ cd ..":
				smallest = check_size(depth.pop())
			else:
				depth.append(0)
		depth = [i + check_file(line.split()[0]) for i in depth]
	
	for i in range(0,len(depth)):
		smallest = check_size(depth.pop())
	
	return smallest

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 24933642,"Test failed, expected 24933642, result "+str(test_value)
	print(main("INPUT"))
