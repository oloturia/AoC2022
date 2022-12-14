#!/usr/bin/python3

def render_cave(cave):
	xmin = 494
	ymin = 0
	xmax = 503
	ymax = 9
	for y in range(ymin,ymax+1):
		for x in range(xmin,xmax+1):
			if (x,y) in cave:
				print("#",end="")
			else:
				print(".",end="")
		print("")

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	cave = set()
	bottom = 0
	for line in input_lines:
		coords = [li.split(",") for li in line.split(" -> ")]
		coords = [[int(c[0]),int(c[1])] for c in coords]
		cursor = {'x':coords[0][0],'y':coords[0][1]}
		direction = lambda a: -1 if a < 0 else 1
		for coord in coords:			
			cave.add((coord[0],coord[1]))
			for x in range(min(coord[0],cursor['x']), max(coord[0],cursor['x'])):
				cave.add((x,cursor['y']))
			for y in range(min(coord[1],cursor['y']), max(coord[1],cursor['y'])):
				cave.add((cursor['x'],y))
			cursor = {'x':coord[0],'y':coord[1]}
			if cursor['y'] > bottom:
				bottom = cursor['y']
	
	bottom += 2
	cycles = 0
	while True:
		if ((500,0)) in cave:
			return cycles
		sand_pos = {'x':500,'y':0}
		falling = True
		while falling:
			if ((sand_pos['x'],sand_pos['y']+1) in cave):
				if ((sand_pos['x']-1,sand_pos['y']+1) in cave):
					if ((sand_pos['x']+1,sand_pos['y']+1) in cave):
						cave.add((sand_pos['x'],sand_pos['y']))
						falling = False
					else:
						sand_pos = {'x':sand_pos['x']+1,'y':sand_pos['y']+1}
				else:
					sand_pos = {'x':sand_pos['x']-1,'y':sand_pos['y']+1}
			else:
				if sand_pos['y']+1 < bottom:
					sand_pos = {'x':sand_pos['x'],'y':sand_pos['y']+1}
				else:
					cave.add((sand_pos['x'],sand_pos['y']))
					falling = False
		cycles += 1
	

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 93,"Test failed, expected 93, result "+str(test_value)
	print(main("INPUT"))
