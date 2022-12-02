#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	score = 0
	tot= 0
	for line in input_lines:
		if line[2] == "X": 
			score += 1
			if line[0] == "A": 
				score += 3
			elif line[0] == "C":
				score += 6
		elif line[2] == "Y": #carta
			score += 2
			if line[0] == "B":
				score += 3
			elif line[0] == "A":
				score += 6
		elif line[2] == "Z": 
			score += 3
			if line[0] == "B":
				score += 6
			elif line[0] == "C":
				score += 3

	return score

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 15,"Test failed, expected 15, result "+str(test_value)
	print(main("INPUT"))
