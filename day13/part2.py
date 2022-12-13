#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	signals = list()
	for line in input_lines:
		if len(line) != 0:
			signals.append(line.replace('[','').replace(']','').replace('10','a'))
	signals.append('2')
	signals.append('6')
	signals.sort()
	key = (signals.index('2') +1)*(signals.index('6')+1)
	return key

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 140,"Test failed, expected 140, result "+str(test_value)
	print(main("INPUT"))
