#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	pos = list()
	for i in range(0,10):
		pos.append({'x':0,'y':0})
	
	visited = {(0,0)}
	dirs = {'U':{'x':1,'y':0},'D':{'x':-1,'y':0},'L':{'x':0,'y':-1},'R':{'x':0,'y':1}}
	for line in input_lines:
		for i in range(0,int(line.split()[1])):
			pos[0]['x'] = pos[0]['x'] + dirs[line.split()[0]]['x']
			pos[0]['y'] = pos[0]['y'] + dirs[line.split()[0]]['y']
			for i in range(1,len(pos)):
				if  abs(pos[i-1]['x'] - pos[i]['x']) > 1 or abs(pos[i-1]['y'] - pos[i]['y']) > 1:
					if pos[i-1]['x'] - pos[i]['x'] >= 1:
						pos[i]['x'] +=1
					elif pos[i-1]['x'] - pos[i]['x'] <= -1:
						pos[i]['x'] -=1
					if pos[i-1]['y'] - pos[i]['y'] >= 1:
						pos[i]['y'] +=1
					elif pos[i-1]['y'] - pos[i]['y'] <= -1:
						pos[i]['y'] -=1
			visited.add((pos[9]['x'],pos[9]['y']))
	return len(visited)

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 1,"Test failed, expected 1, result "+str(test_value)
	test_value = main("TEST2")
	assert test_value == 36,"Test failed, expected 36, result "+str(test_value)
	print(main("INPUT"))
