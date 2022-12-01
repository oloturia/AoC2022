#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	elves = list()
	totCal = 0
	for line in input_lines:
		if line == "":
			elves.append(totCal)
			totCal = 0
		else:
			totCal += int(line) 
	elves.append(totCal)
	
	elves.sort(reverse=True)
	maxCal = 0
	
	for i in range(0,3):
		maxCal += elves[i]
	
	return 	maxCal

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 45000,"Test failed, expected 45000, result "+str(test_value)
	print(main("INPUT"))
