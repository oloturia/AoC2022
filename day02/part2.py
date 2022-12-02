#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	score = 0
	payoffs = {("A","X"):3,("A","Y"):4,("A","Z"):8,("B","X"):1,("B","Y"):5,("B","Z"):9,("C","X"):2,("C","Y"):6,("C","Z"):7}
	for line in input_lines:
		score += payoffs[(line[0],line[2])]
			
	return score

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 12,"Test failed, expected 12, result "+str(test_value)
	print(main("INPUT"))
