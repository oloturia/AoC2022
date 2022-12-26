#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	line = input_lines[0]
	
	rocks = [ [(0,0),(1,0),(2,0),(3,0)], [(1,0),(0,1),(1,1),(2,1),(1,2)], [(2,0),(2,1),(0,0),(1,0),(2,2)], [ (0,0),(0,1),(0,2),(0,3) ], [(0,0),(0,1),(1,0),(1,1)] ]


	spawn_point = 0
	turn = 0
	blocks_fell = set()
	iteration = 0
	turn = 0
	for _ in range(0,2022):
		rock = rocks[turn]
		turn +=1
		turn = turn%5
		x_offset = 2
		y_offset = spawn_point+3
		rock_falling = True
		while rock_falling:
			if line[iteration] == "<":
				new_offset = -1
			else:
				new_offset = 1
			iteration += 1
			iteration = iteration%len(line)

			possible_move = True
			for block in rock:
				if (block[0] + x_offset + new_offset < 0) or (block[0] + x_offset + new_offset >= 7):
					possible_move = False
				elif (block[0] + x_offset + new_offset,block[1]+y_offset) in blocks_fell:
					possible_move = False
			if possible_move:
				x_offset += new_offset

			y_offset -=1
			for block in rock:
				if block[1] + y_offset < 0:
					y_offset +=1
					rock_falling = False
				elif (block[0]+x_offset,(block[1])+y_offset) in blocks_fell:
					rock_falling = False
					y_offset +=1
	
		for block in rock:
			blocks_fell.add(( block[0] + x_offset, block[1] + y_offset))
			
		new_spawn = 0
		for block in blocks_fell:
			if block[1]+1 > new_spawn:
				new_spawn = block[1]+1
			
		if new_spawn > spawn_point:
			spawn_point = new_spawn

	max_quota = 0
	for block in blocks_fell:
		if block[1] > max_quota:
			max_quota = block[1]
	return 	max_quota+1

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 3068,"Test failed, expected 3068, result "+str(test_value)
	print(main("INPUT"))
