#!/usr/bin/python3

def main(input_file,side):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	tiles = dict()
	directs = ""

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
				tiles[(y,x)] = space


	face_1 = dict()
	face_2 = dict()
	face_3 = dict()
	face_4 = dict()
	face_5 = dict()
	face_6 = dict()
	
	if side == 4:
		for tile in tiles:
			y = tile[0]
			x = tile[1]
			if y < side and x >= side*2:
				face_1[(y,x - side*2)] = tiles[(y,x)]
			if side*2 > y >= side and  x < side:
				face_2[(y-side,x)] = tiles[(y,x)]
			if side*2 > y >= side and side <= x < side*2:
				face_3[(y-side,x-side)] = tiles[(y,x)]
			if side*2 > y >= side and side*2 <= x < side*3:
				face_4[(y-side,x-side*2)] = tiles[(y,x)]
			if side*3 > y >= side*2 and side*2 <= x < side*3:
				face_5[(y-side*2,x-side*2)] = tiles[(y,x)]
			if side*3 > y >= side*2 and side*3 <= x:
				face_6[(y-side*2,x-side*3)] = tiles[(y,x)]
			
	elif side == 50:
		for tile in tiles:
			y = tile[0]
			x = tile[1]

			if y < side and side <= x < side*2:	
				face_1[(y,x-side)] = tiles[(y,x)]
			if y < side and side*2 <= x < side*3:
				face_2[(y,x-side*2)] = tiles[(y,x)]
			if side <= y < side*2 and side <= x < side*2:
				face_3[(y-side,x-side)] = tiles[(y,x)]
			if side*2 <= y < side*3 and x < side:
				face_4[(y-side*2,x)] = tiles[(y,x)]
			if side*2 <= y < side*3 and side <= x < side*2:
				face_5[(y-side*2,x-side)] = tiles[(y,x)]
			if side*3 <= y < side*4 and x < side:
				face_6[(y-side*3,x)] = tiles[(y,x)]
			
		
		cube = {1:face_1,2:face_2,3:face_3,4:face_4,5:face_5,6:face_6}			
		

		
	cube = {1:face_1,2:face_2,3:face_3,4:face_4,5:face_5,6:face_6}			
	pos = {"y":0,"x":0,"face":1}
	facing = next_facing = 0
	f_list = [{"y":0,"x":1},{"y":1,"x":0},{"y":0,"x":-1},{"y":-1,"x":0}]
	moves_str = ""

	for d in directs: 
		if ord("0") <= ord(d) <= ord("9"):
			moves_str += d
		else:
			next_facing = facing
			prev_facing = next_facing
			moves = int(moves_str)
			moves_str = ""
			for i in range(moves):
				next_tile = {"y": pos["y"] + f_list[facing]["y"], "x": pos["x"] + f_list[facing]["x"],"face":pos["face"]}
				new_face = False
				if side == 4:
					if next_tile["x"] < 0:
						new_face = True
						if pos["face"] == 1:
							next_facing -=1
							next_tile = {"y":0,"x":pos["y"], "face": 3}
						elif pos["face"] == 2:
							next_facing +=1
							next_tile = {"y":(side-1),"x":(side-1)-pos["y"], "face": 6}
						elif pos["face"] == 3:
							next_tile = {"y":pos["y"],"x":(side-1), "face": 2}
						elif pos["face"] == 4:
							next_tile = {"y":pos["y"],"x":(side-1), "face": 3}
						elif pos["face"] == 5:
							next_facing +=1
							next_tile = {"y":(side-1) ,"x":(side-1)-pos["y"], "face": 3}
						elif pos["face"] == 6:
							next_tile = {"y":pos["y"],"x":(side-1), "face": 5}
					
					elif next_tile["x"] >= side:		
						new_face = True
						if pos["face"] == 1:
							next_facing +=2
							next_tile = {"y":(side-1)-pos["y"],"x":(side-1), "face": 6}
						elif pos["face"] == 2:
							next_tile = {"y":pos["y"],"x":0, "face": 3}
						elif pos["face"] == 3:
							next_tile = {"y":pos["y"],"x":0, "face": 4}
						elif pos["face"] == 4:
							next_facing +=1
							next_tile = {"y":0,"x":(side-1)-pos["y"], "face": 6}
						elif pos["face"] == 5:
							next_tile = {"y":pos["y"],"x":0, "face": 6}
						elif pos["face"] == 6:
							next_facing +=2
							next_tile = {"y":(side-1)-pos["y"],"x":(side-1), "face": 1}
							
					elif next_tile["y"] < 0:
						new_face = True
						if pos["face"] == 1:
							next_facing +=2
							next_tile = {"y":0,"x":(side-1)-pos["x"], "face": 2}
						elif pos["face"] == 2:
							next_facing +=2
							next_tile = {"y":0,"x":(side-1)-pos["x"], "face": 1}
						elif pos["face"] == 3:
							next_facing +=1
							next_tile = {"y":pos["x"],"x":0, "face": 1}
						elif pos["face"] == 4:
							next_tile = {"y":(side-1),"x":pos["x"], "face": 1}
						elif pos["face"] == 5:
							next_tile = {"y":(side-1),"x":pos["x"], "face": 4}
						elif pos["face"] == 6:
							next_facing -=1
							next_tile = {"y":(side-1)-pos["x"],"x":side-1, "face": 4}
					
					elif next_tile["y"] >= side:		
						new_face = True
						if pos["face"] == 1:
							next_tile = {"y":0,"x":pos["x"], "face":4 }
						elif pos["face"] == 2:
							next_facing +=2
							next_tile = {"y":(side-1),"x":(side-1)-pos["x"], "face": 5}
						elif pos["face"] == 3:
							next_facing -=1
							next_tile = {"y":(side-1)-pos["x"],"x":0, "face": 5}
						elif pos["face"] == 4:
							next_tile = {"y":0,"x":pos["x"], "face": 5}
						elif pos["face"] == 5:
							next_facing +=2
							next_tile = {"y":(side-1) ,"x":(side-1)-pos["x"], "face": 2}
						elif pos["face"] == 6:
							next_facing -=1
							next_tile = {"y":(side-1)-pos["x"] ,"x":0, "face": 2}
				elif side == 50:
					if next_tile["x"] < 0:
						new_face = True
						if pos["face"] == 1:
							next_facing +=2
							next_tile = {"y":(side-1)-pos["y"] ,"x":0,"face":4}							
						elif pos["face"] == 2:
							next_tile = {"y":pos["y"],"x":(side-1),"face":1}
						elif pos["face"] == 3:
							next_facing -=1
							next_tile = {"y":0,"x":pos["y"],"face":4}							
						elif pos["face"] == 4:
							next_facing +=2
							next_tile = {"y":(side-1)-pos["y"],"x":0,"face":1}
						elif pos["face"] == 5:
							next_tile = {"y":pos["y"],"x":(side-1),"face":4}
						elif pos["face"] == 6:
							next_facing -=1
							next_tile = {"y":0,"x":pos["y"],"face":1}
					
					elif next_tile["x"] >= side:		
						new_face = True						
						if pos["face"] == 1:
							next_tile = {"y":pos["y"],"x":0,"face":2}
						elif pos["face"] == 2:
							next_facing += 2 
							next_tile = {"y":(side-1)-pos["y"],"x":(side-1),"face":5}
						elif pos["face"] == 3:
							next_facing -=1
							next_tile = {"y":(side-1),"x":pos["y"],"face":2}
						elif pos["face"] == 4:
							next_tile = {"y":pos["y"],"x":0,"face":5}
						elif pos["face"] == 5:
							next_facing +=2
							next_tile = {"y":(side-1)-pos["y"],"x":(side-1),"face":2}
						elif pos["face"] == 6:
							next_facing -=1
							next_tile = {"y":(side-1),"x":pos["y"],"face":5}
							
					elif next_tile["y"] < 0:
						new_face = True
						if pos["face"] == 1:
							next_facing +=1
							next_tile = {"y":pos["x"],"x":0,"face":6}
						elif pos["face"] == 2:
							next_tile = {"y":(side-1),"x":pos["x"],"face":6}
						elif pos["face"] == 3:
							next_tile = {"y":(side-1),"x":pos["x"],"face":1}
						elif pos["face"] == 4:
							next_facing +=1
							next_tile = {"y":pos["x"],"x":0,"face":3}
						elif pos["face"] == 5:
							next_tile = {"y":(side-1),"x":pos["x"],"face":3}
						elif pos["face"] == 6:
							next_tile = {"y":(side-1),"x":pos["x"],"face":4}
					
					elif next_tile["y"] >= side:		
						new_face = True
						if pos["face"] == 1:
							next_tile = {"y":0,"x":pos["x"],"face":3}
						elif pos["face"] == 2:
							next_facing +=1
							next_tile = {"y":pos["x"],"x":(side-1),"face":3}
						elif pos["face"] == 3:
							next_tile = {"y":0,"x":pos["x"],"face":5}
						elif pos["face"] == 4:
							next_tile = {"y":0,"x":pos["x"],"face":6}
						elif pos["face"] == 5:
							next_facing +=1
							next_tile = {"y":pos["x"] ,"x":(side-1),"face":6}
						elif pos["face"] == 6:
							next_tile = {"y":0,"x":pos["x"],"face":2}
				if cube[next_tile["face"]][(next_tile["y"],next_tile["x"])] == "#":
					if new_face:
						next_facing = prev_facing
					break
				else:
					if new_face:
						facing = next_facing % 4
					pos = next_tile
					if facing == 0:
						old_facing = "→"
					elif facing == 1:
						old_facing = "↓"
					elif facing == 2:
						old_facing = "←"
					else:
						old_facing = "↑"
					cube[next_tile['face']][(next_tile['y'],next_tile['x'])] = old_facing
			if d == "R":
				facing = (facing +1)%4
			elif d == "L":
				facing = (facing -1)%4
	if side == 4:
		if pos["face"] == 1:
			abs_x = pos["x"]+side*2
			abs_y = pos["y"]
		if pos["face"] == 2:
			abs_x = pos["x"]
			abs_y = pos["y"]+side
		if pos["face"] == 3:
			abs_x = pos["x"]+side
			abs_y = pos["y"]+side						
		if pos["face"] == 4:
			abs_x = pos["x"]+side*2
			abs_y = pos["y"]+side
		if pos["face"] == 5:
			abs_x = pos["x"]+side*2
			abs_y = pos["y"]+side*2
		if pos["face"] == 6:			
			abs_x = pos["x"]+side*3
			abs_y = pos["y"]+side*2
	elif side == 50:
		if pos["face"] == 1:
			abs_x = pos["x"]+side
			abs_y = pos["y"]
		if pos["face"] == 2:
			abs_x = pos["x"]+side*2
			abs_y = pos["y"]
		if pos["face"] == 3:
			abs_x = pos["x"]+side
			abs_y = pos["y"]+side
		if pos["face"] == 4:
			abs_x = pos["x"]
			abs_y = pos["y"]+side*2
		if pos["face"] == 5:
			abs_x = pos["x"]+side
			abs_y = pos["y"]+side*2
		if pos["face"] == 6:
			abs_x = pos["x"]
			abs_y = pos["y"]+side*3

	return 	1000 * (abs_y+1) + 4 * (abs_x+1) + facing





if __name__ == "__main__":
	test_value = main("TEST",4)
	assert test_value == 5031,"Test failed, expected 5031, result "+str(test_value)
	print(main("INPUT",50))
