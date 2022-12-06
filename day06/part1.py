#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	for i in range(0,len(input_lines[0])-3):
		if len(set(input_lines[0][i:i+4])) == 4:			
			break
	return 	i+4

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 7,"Test failed, expected 7, result "+str(test_value)
	test_value = main("TEST2")
	assert test_value == 5,"Test failed, expected 5, result "+str(test_value)
	test_value = main("TEST3")
	assert test_value == 6,"Test failed, expected 6, result "+str(test_value)
	test_value = main("TEST4")
	assert test_value == 10,"Test failed, expected 10, result "+str(test_value)
	test_value = main("TEST5")
	assert test_value == 11,"Test failed, expected 11, result "+str(test_value)
	print(main("INPUT"))
