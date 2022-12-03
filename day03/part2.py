#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [set(line.rstrip()) for line in f.readlines()]

	priorities = 0
	calcprior = lambda p: ord(p) - 96 if ord(p) >= 97 else ord(p) - 38
	for i in range(0,len(input_lines),3):
		badge = str(input_lines[i].intersection(input_lines[i+1]).intersection(input_lines[i+2]))[2]
		priorities += calcprior(badge)
	return priorities

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 70,"Test failed, expected 70, result "+str(test_value)
	print(main("INPUT"))
