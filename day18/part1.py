#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	sides = 0
	cubes = set()
	for line in input_lines:
		cubes.add((int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])))
		sides += 6
	
	for cube1 in cubes:
		for cube2 in cubes:
			if (cube1[0] == cube2[0]+1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]) or (cube1[0] == cube2[0] and cube1[1]+1 == cube2[1] and cube1[2] == cube2[2]) or (cube1[0] == cube2[0] and cube1[1] == cube2[1] and cube1[2]+1 == cube2[2]):
				sides -=2
	
	return 	sides

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 64,"Test failed, expected 64, result "+str(test_value)
	print(main("INPUT"))
