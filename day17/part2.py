#!/usr/bin/python3



def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	line = input_lines[0]
	
	rocks = [ [(0,0),(1,0),(2,0),(3,0)], [(1,0),(0,1),(1,1),(2,1),(1,2)], [(2,0),(2,1),(0,0),(1,0),(2,2)], [ (0,0),(0,1),(0,2),(0,3) ], [(0,0),(0,1),(1,0),(1,1)] ]

	objective = 1000000000000
	spawn_point = 0
	turn = 0
	blocks_fallen = set()
	iteration = 0
	max_quota = 0
	turn = 0 
	check_repeat = list()
	
	last_turn = 0
	last_quota = 0
	
	fast_forward = False
	
	last_index = lambda a,b : len(a) - a[::-1].index(b) -1
	last_iteration = 0
	
	depth = 10 if len(input_lines[0]) < 100 else 3
	
	while turn < objective:
		rock = rocks[turn%5]
		turn += 1
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
				elif (block[0] + x_offset + new_offset,block[1]+y_offset) in blocks_fallen:
					possible_move = False
			if possible_move:
				x_offset += new_offset

			y_offset -=1

			for block in rock:
				if block[1] + y_offset < 0:
					y_offset +=1
					rock_falling = False
				elif (block[0]+x_offset,(block[1])+y_offset) in blocks_fallen:
					rock_falling = False
					y_offset +=1
		
		if iteration-last_iteration < 0 and not fast_forward:
			to_append = (turn%5,turn-last_turn,max_quota-last_quota)
			
			if len(check_repeat) > 0:
				if to_append in check_repeat and (len(check_repeat) > depth):
					start_repeat = last_index(check_repeat,to_append)
					ff_rocks = 0
					ff_quota = 0
					for a_h in range(start_repeat,len(check_repeat)):
						ff_rocks += check_repeat[a_h][1]
						ff_quota += check_repeat[a_h][2]
					objective -= turn
					off_quota = (objective // ff_rocks) * ff_quota
					objective = (objective % ff_rocks) + turn +1
					fast_forward = True
				else:
					last_quota = max_quota
					last_turn = turn
					check_repeat.append(to_append)
			
			else:
				last_quota = max_quota
				last_turn = turn
				check_repeat.append(to_append)
	
		last_iteration = iteration

		for block in rock:
			blocks_fallen.add(( block[0] + x_offset, block[1] + y_offset))
			
		new_spawn = 0
		for block in blocks_fallen:
			if block[1]+1 > new_spawn:
				new_spawn = block[1]+1

		if new_spawn > spawn_point:
			spawn_point = new_spawn
	
		prev_quota = max_quota
		max_quota = 0
		for block in blocks_fallen:
			if block[1] > max_quota:
				max_quota = block[1]
	
	return max_quota+off_quota

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 1514285714288,"Test failed, expected 1514285714288, result "+str(test_value)
	print(main("INPUT"))
