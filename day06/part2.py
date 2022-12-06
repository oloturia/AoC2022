#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	for i in range(0,len(input_lines[0])-13):
		if len(set(input_lines[0][i:i+14])) == 14:			
			break
	return 	i+14

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 19,"Test failed, expected 19, result "+str(test_value)
	test_value = main("TEST2")
	assert test_value == 23,"Test failed, expected 23, result "+str(test_value)
	test_value = main("TEST3")
	assert test_value == 23,"Test failed, expected 23, result "+str(test_value)
	test_value = main("TEST4")
	assert test_value == 29,"Test failed, expected 29, result "+str(test_value)
	test_value = main("TEST5")
	assert test_value == 26,"Test failed, expected 26, result "+str(test_value)
	print(main("INPUT"))
