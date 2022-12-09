#!/usr/bin/python3



def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	posH = {'x':0,'y':0}
	posT = {'x':0,'y':0}
	visited = {(0,0)}
	dirs = {'U':{'x':1,'y':0},'D':{'x':-1,'y':0},'L':{'x':0,'y':-1},'R':{'x':0,'y':1}}

	for line in input_lines:
		for i in range(0,int(line.split()[1])):
			posH['x'] = posH['x'] + dirs[line.split()[0]]['x']
			posH['y'] = posH['y'] + dirs[line.split()[0]]['y']
			if  abs(posH['x'] - posT['x']) > 1 or abs(posH['y'] - posT['y']) > 1:
				if posH['x'] - posT['x'] >= 1:
					posT['x'] +=1
				elif posH['x'] - posT['x'] <= -1:
					posT['x'] -=1
				if posH['y'] - posT['y'] >= 1:
					posT['y'] +=1
				elif posH['y'] - posT['y'] <= -1:
					posT['y'] -=1
			visited.add((posT['x'],posT['y']))

	return len(visited)

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 13,"Test failed, expected 13, result "+str(test_value)
	print(main("INPUT"))
