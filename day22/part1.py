#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	tiles = dict()
	directs = ""
	start = None
	bounds = {"y":0,"x":0}
	for y,line in enumerate(input_lines):
		if len(line) == 0:
			continue
		elif ord("1") <= ord(line[0]) <= ord("9"):
			directs = line+"X"
		else:
			bounds["x"] = max(bounds["x"], len(line))
			bounds["y"] +=1
			for x,space in enumerate(line):
				if start is None and space != " ":
					start = {"y":y,"x":x}
				tiles[(y,x)] = space
	
	pos = start
	facing = 0
	f_list = [{"y":0,"x":1},{"y":1,"x":0},{"y":0,"x":-1},{"y":-1,"x":0}]
	moves_str = ""
	for d in directs:
		if ord("0") <= ord(d) <= ord("9"):
			moves_str += d
		else:
			next_facing = d
			moves = int(moves_str)
			moves_str = ""
			for i in range(moves):
				
				next_tile = {"y": pos["y"] + f_list[facing]["y"], "x": pos["x"] + f_list[facing]["x"]}
				
				if (tuple(next_tile.values()) not in tiles) or (tiles[tuple(next_tile.values())] == " "):
					if facing == 0:
						next_tile["x"] = 0
					elif facing == 1:
						next_tile["y"] = 0
					elif facing == 2:
						next_tile["x"] = bounds["x"]
					elif facing == 3:
						next_tile["y"] = bounds["y"]
					while (tuple(next_tile.values()) not in tiles) or tiles[tuple(next_tile.values())] == " ":
						next_tile["x"] += f_list[facing]["x"]
						next_tile["y"] += f_list[facing]["y"]						
						
				if tiles[tuple(next_tile.values())] == "#":
					break
				else:
					pos = next_tile

				old_facing = "↑"
			
			if next_facing == "R":
				facing = (facing +1)%4
			elif next_facing == "L":
				facing = (facing -1)%4

	return 	1000 * (pos['y']+1) + 4 * (pos['x']+1) + facing



if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 6032,"Test failed, expected 6032, result "+str(test_value)
	print(main("INPUT"))
