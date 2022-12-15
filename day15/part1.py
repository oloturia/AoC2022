#!/usr/bin/python3

def main(input_file,pos):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	nosens = list()
	sensors = list()
	bounds={'l':0,'r':0}
	beacons = set()
	for line in input_lines:
		sensors.append( {'sx':int(line.split()[2][2:-1]), 'sy':int(line.split()[3][2:-1]), 'bx':int(line.split()[8][2:-1]), 'by':int(line.split()[9][2:])} )
		if sensors[-1]['by'] == pos:
			beacons.add(sensors[-1]['bx'])
	
	for i,sensor in enumerate(sensors):
		dist = abs( sensor['sx'] - sensor['bx'] ) + abs( sensor['sy'] - sensor['by'] )
		dist_nosense_line = abs(sensor['sy'] - pos)
		
		dist_y = abs(sensor['sy'] - pos)
		dist_x = dist - dist_y
		if dist_x >= 0:
			nosens.append((sensor['sx']-dist_x,sensor['sx']+dist_x))
			if bounds['l'] > nosens[-1][0]: bounds['l'] = nosens[-1][0]
			if bounds['r'] < nosens[-1][1]: bounds['r'] = nosens[-1][1]
		
	check_val = 0
	for i in range(bounds['l'],bounds['r']+1):
		for nosensor in nosens:
			if i >= nosensor[0] and i <= nosensor[1]:
				if i not in beacons:
					check_val += 1
				break

	return 	check_val

if __name__ == "__main__":
	test_value = main("TEST",10)
	assert test_value == 26,"Test failed, expected 26, result "+str(test_value)
	print(main("INPUT",2000000))
