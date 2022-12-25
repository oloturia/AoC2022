#!/usr/bin/python3
global cave
global bounds
global empty_space

def main(input_file):
	global cave
	global bounds
	global empty_space

	best_row = best_col = 0
	
	found = False
	bounds = {"row":0,"col":0}
	cave = list()
	empty_space = [set()]
	min_minutes = 1
	
	cave.append( list() )
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	for row,line in enumerate(input_lines):
		bounds["row"]+=1
		for col,cell in enumerate(line):
			
			if cell == "^":
				cave[0].append({"orient":(-1,0),"row":row,"col":col})
			elif cell == "<":
				cave[0].append({"orient":(0,-1),"row":row,"col":col})
			elif cell == ">":
				cave[0].append({"orient":(0,1),"row":row,"col":col})
			elif cell == "v":
				cave[0].append({"orient":(1,0),"row":row,"col":col})
			else:
				empty_space[0].add((row,col))

	bounds["row"] -=1
	bounds["col"] = len(line)-1

	cycle = lcm(bounds["row"]-1,bounds["col"]-1)
	cycle +=1
	
	for x in range(cycle):
		gen_blizz()

	graph = dict()

	for i in range(cycle):
		graph[(i,0,1)] = list()
		graph[(i,0,1)].append( ((i+1) % cycle,0,1) )
		if (1,1) in empty_space[(i+1) % cycle]:
			graph[(i,0,1)].append( ((i+1) % cycle,1,1) )
		for r in range(1,bounds["row"]):
			for c in range(1,bounds["col"]):
				up = dn = rw = lw = np = False
				if r-1 > 0:
					up = (r-1,c) in empty_space[(i+1) % cycle]
				if r+1 < bounds["row"]:
					dn = (r+1,c) in empty_space[(i+1) % cycle]
				if c+1 < bounds["col"]:
					rw = (r,c+1) in empty_space[(i+1) % cycle]
				if c-1 > 0:
					lw = (r,c-1) in empty_space[(i+1) % cycle]
				np = (r,c) in empty_space[(i+1) % cycle]
				graph[(i,r,c)] = list()
				if up:
					graph[(i,r,c)].append( ((i+1)% cycle,r-1,c) )
				if dn:
					graph[(i,r,c)].append( ((i+1)% cycle,r+1,c) )
				if rw:
					graph[(i,r,c)].append( ((i+1)% cycle,r,c+1) )
				if lw:
					graph[(i,r,c)].append( ((i+1)% cycle,r,c-1) )
				if np:
					graph[(i,r,c)].append( ((i+1)% cycle,r,c) )

	
	path_list = [ [(0,0,1)] ]
	path_index = 0
	previous_nodes = { (0,0,1) }
	end = set()
	for i in range(cycle):
		end.add( (i,bounds["row"]-1,bounds["col"]-1) )
	
	while path_index < len(path_list):
		current_path = path_list[path_index]
		last_node = current_path[-1]
		next_nodes = graph[last_node]
		for e in end:
			if e in next_nodes:
				current_path.append(e)
				return len(current_path)
		for next_node in next_nodes:
			if not next_node in previous_nodes:
				new_path = current_path.copy()
				new_path.append(next_node)
				path_list.append(new_path)
				previous_nodes.add(next_node)
		path_index += 1
		


def gen_blizz():
	global cave
	global bounds
	global empty_space
	
	empty_space.append(set())
	for r in range(1,bounds["row"]):
		for c in range(1,bounds["col"]):
			empty_space[-1].add((r,c))
	
	cave.append( list() )
	for blizz in cave[-2]:
		new_row = blizz["row"] + blizz["orient"][0]
		new_col = blizz["col"] + blizz["orient"][1]
		if new_row == 0:
			new_row = bounds["row"]-1
		elif new_row == bounds["row"]:
			new_row = 1
		if new_col == 0:
			new_col = bounds["col"]-1
		elif new_col == bounds["col"]:
			new_col = 1
		cave[-1].append({"orient":blizz["orient"],"row":new_row,"col":new_col})
		
		if (new_row,new_col) in empty_space[-1]:
			empty_space[-1].remove((new_row,new_col))
	

def lcm(a,b):
	if a > b:
		g = a
	else:
		g = b
	while True:
		if g%a == 0 and g%b == 0:
			return g
		g +=1


if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 18,"Test failed, expected 18, result "+str(test_value)
	print(main("INPUT"))
