#!/usr/bin/python3

def compare(left,right):
	if type(left) == int and type(right) == int:
		if left > right:
			return -1
		elif right > left:
			return 1
		else:
			return 0
	if type(left) == list and type(right) == int:
		res = compare(left,[right])
		return res
	elif type(left) == int and type(right) == list:
		res = compare([left],right)
		return res
	else:
		for i in range(0,max(len(left),len(right))):
			if i == len(left):
				return 1
			elif i == len(right):
				return -1
			else:
				res = compare(left[i],right[i])
			if res != 0:
				return res
		return 0

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	right_index = 0
	index = 0
	for iline in range(0,len(input_lines),3):
		index +=1
		left = eval(input_lines[iline].replace("[]","list()"))
		right = eval(input_lines[iline+1].replace("[]","list()"))
		if compare(left,right) == 1:
			right_index += index
	return right_index	

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 13,"Test failed, expected 13, result "+str(test_value)
	print(main("INPUT"))
