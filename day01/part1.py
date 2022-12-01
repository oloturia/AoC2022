#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	totCal = 0
	maxCal = 0
	for line in input_lines:
		if line == "":
			if maxCal < totCal:
				maxCal = totCal
			totCal = 0
		else:
			totCal += int(line) 

	return 	maxCal

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 24000,"Test failed, expected 24000, result "+str(test_value)
	print(main("INPUT"))
