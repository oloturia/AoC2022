#!/usr/bin/python3
land = dict()
moves = dict()
moves_check = list()
moves_prevented = list()

def main(input_file):
	global land
	global moves
	global moves_check
	global moves_prevented
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	land = dict()
	n_elves = 0
	for row,line in enumerate(input_lines):
		for col,cell in enumerate(line):
			if cell == "#":
				land[(row,col)] = cell
				n_elves +=1
			
	moves = dict()
	moves_check = list()
	directions = ["N","S","W","E"]
	tot_moves = 0
	while True:
		for coord,cell in land.items():
			if cell == "#":
				if radar(coord):
					for d in directions:
						if check_free(d,coord):
							break
		
		for from_cell,to_cell in moves.items():
			if not( to_cell in moves_prevented):
				del(land[from_cell])
				land[to_cell] = "#"
		directions.append(directions.pop(0))	
		if len(moves) == 0:
			return tot_moves+1
		moves = {}
		moves_check = []
		moves_prevented = []
		tot_moves +=1


def radar(coord):
	global land
	check_space = lambda x: land[x] if x in land else "."
	for i in range(-1,2):
		for j in range(-1,2):
			if i == j == 0:
				continue
			if check_space( (i+coord[0],j+coord[1]) ) == "#":
				
				return True
	return False
	

def check_free(direction,coord):
	global land
	global moves
	global moves_check
	global moves_prevented
	
	moved = False	
	check_space = lambda x: land[x] if x in land else "."
	dir_factor = {"N":((-1,-1),(-1,0),(-1,1)),"E":((-1,1),(0,1),(1,1)),"S":((1,-1),(1,0),(1,1)),"W":((-1,-1),(0,-1),(1,-1))}
	coord1 =  (coord[0]+dir_factor[direction][0][0],coord[1]+dir_factor[direction][0][1]) 
	coord2 =  (coord[0]+dir_factor[direction][1][0],coord[1]+dir_factor[direction][1][1])  
	coord3 =  (coord[0]+dir_factor[direction][2][0],coord[1]+dir_factor[direction][2][1]) 
	
	if check_space(coord1) == "." and check_space(coord2) == "." and check_space(coord3) == ".":
		moved = True
		if coord2 in moves_check:
			moves_prevented.append(coord2)
		else:
			moves[coord] = coord2
			moves_check.append(coord2)
	
	return moved

def remove_move(to_cell):
	global land
	global moves
	for coord,cell in moves:
		if cell == to_cell:
			return coord

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 20,"Test failed, expected 20, result "+str(test_value)
	print(main("INPUT"))
