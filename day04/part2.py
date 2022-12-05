#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	pairs = 0
	for line in input_lines:
		groupA = { x for x in range(int (line.split(",")[0].split("-")[0] ), int( line.split(",")[0].split("-")[1] ) +1) }
		groupB = { x for x in range(int (line.split(",")[1].split("-")[0] ), int( line.split(",")[1].split("-")[1] ) +1) }
		if groupA & groupB != set():
			pairs += 1
		
	return 	pairs

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 4,"Test failed, expected 4, result "+str(test_value)
	print(main("INPUT"))
