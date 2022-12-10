#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	regX = 1
	cycle = 0
	signal_strenght = 0
	for line in input_lines:
		if line == "noop":
			cycle +=1
			if (cycle-20)%40 == 0: signal_strenght += cycle * regX
		else:
			cycle +=1
			if (cycle-20)%40 == 0: signal_strenght += cycle * regX
			cycle +=1
			if (cycle-20)%40 == 0: signal_strenght += cycle * regX
			regX += int(line.split()[1])
			
	return signal_strenght

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 13140,"Test failed, expected 13140, result "+str(test_value)
	print(main("INPUT"))
