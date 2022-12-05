#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	stacks = dict()
	solution = ""
	
	for line in input_lines:
		if line[1] == "1":
			for char in line:
				if char != " ":				
					stacks[char] = list()
			break

	for line in input_lines:
		if line[1] == "1":
			break
		for i in range(1,len(line)+1,4):
			if line[i] != " ":
				stacks[str((i//4)+1)].append(line[i])

	for line in input_lines:
		try:
			if line[0] == "m":
				iterations = int(line.split()[1])
				from_stack = line.split()[3]
				to_stack = line.split()[5]
				for i in range(0,iterations):
					stacks[to_stack] = [stacks[from_stack].pop(0)] + stacks[to_stack]
		except IndexError:
			continue
		
    		
	for stack in stacks:
		solution += stacks[stack][0]

	return solution

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == "CMZ","Test failed, expected CMZ, result "+str(test_value)
	print(main("INPUT"))
