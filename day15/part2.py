#!/usr/bin/python3

	
def main(input_file,pos):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	sensors = list()
	for line in input_lines:
		sensors.append( {'x':int(line.split()[2][2:-1]), 'y':int(line.split()[3][2:-1]), 'd': abs( int( line.split()[8][2:-1] ) - int( line.split()[2][2:-1] ) ) + abs( int( line.split()[9][2:] ) - int( line.split()[3][2:-1] )  ) } )

	for i,sensor in enumerate(sensors):
		
		xdist = 0
		ydist = sensor['d']+1
		while ydist >= 0:
			if (0 <= sensor['x']+xdist <= pos) and (0<= sensor['y']+ydist <= pos):
					if check(i,sensor['x']+xdist, sensor['y']+ydist,sensors ):						
						return (sensor['x']+xdist)*4000000 + sensor['y']+ydist
						
			if (0 <= sensor['x']-xdist <= pos) and (0<= sensor['y']+ydist <= pos):
					if check(i,sensor['x']-xdist, sensor['y']+ydist,sensors ):
						return (sensor['x']-xdist)*4000000 + sensor['y']+ydist
						
			if (0 <= sensor['x']+xdist <= pos) and (0<= sensor['y']-ydist <= pos):
					if check(i,sensor['x']+xdist, sensor['y']-ydist,sensors ):
						return (sensor['x']+xdist)*4000000 + sensor['y']-ydist
						
			if (0 <= sensor['x']-xdist <= pos) and (0<= sensor['y']-ydist <= pos):
					if check(i,sensor['x']-xdist, sensor['y']-ydist,sensors ):
						return (sensor['x']-xdist)*4000000 + sensor['y']-ydist
						
			ydist -=1
			xdist +=1

	return 0


def check(ind,x,y,sensors):
	for j,sensor in enumerate(sensors):
		if ind == j:
			continue
		if abs(x - sensor['x'] ) + abs(y - sensor['y']) <= sensor['d']:
			return False
	return True
	
if __name__ == "__main__":
	test_value = main("TEST",20)
	assert test_value == 56000011,"Test failed, expected 56000011, result "+str(test_value)
	print(main("INPUT",4000000))
