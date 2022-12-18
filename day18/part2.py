#!/usr/bin/python3

def check_connection(c1,c2):
	if (c1[0] == c2[0]+1 and c1[1] == c2[1] and c1[2] == c2[2]) or (c1[0] == c2[0] and c1[1]+1 == c2[1] and c1[2] == c2[2]) or (c1[0] == c2[0] and c1[1] == c2[1] and c1[2]+1 == c2[2]):
		return True
	return False
		

		
	
def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	sides = 0
	cubes = set()
	for line in input_lines:
		cubes.add((int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])))
		sides += 6


	max_z = 0
	max_y = 0
	max_x = 0
	for cube1 in cubes:
		if cube1[0] > max_x:
			max_x = cube1[0]
		if cube1[1] > max_y:
			max_y = cube1[1]
		if cube1[2] > max_z:
			max_z = cube1[2]
		for cube2 in cubes:
			if check_connection(cube1,cube2):
				sides -= 2

	ext_voids = set()
	level_matrix = dict()
	for y in range(1,max_y+1):	
		for z in range(1,max_z+1):
			for x in range(1,max_x+1):
				if (x,y,z) in cubes:
					level_matrix[(x,y,z)] = 1
				elif y == 1 or y == max_y or x == 1 or x == max_x or z == 1 or z == max_z:
					level_matrix[(x,y,z)] = -1
				else:
					level_matrix[(x,y,z)] = 0
		
	expand = True
	while expand:
		expand = False
		for x in range(1,max_x+1):
			for y in range(1,max_y+1):
				for z in range(1,max_z+1):
					if level_matrix[(x,y,z)] == 1 or level_matrix[(x,y,z)] == 0:
						continue
					else:
						if x > 1 and level_matrix[(x-1,y,z  )] == 0:
							level_matrix[(x-1,y,z)] = -1
							expand = True
						if x < max_x and level_matrix[(x+1,y,z  )] == 0:
							level_matrix[(x+1,y,z)] = -1
							expand = True
						if y > 1 and level_matrix[(x,y-1,z  )] == 0:
							level_matrix[(x,y-1,z)] = -1
							expand = True
						if y < max_y and level_matrix[(x,y+1,z  )] == 0:
							level_matrix[(x,y+1,z)] = -1
							expand = True
						if z > 1 and level_matrix[(x,y,z-1  )] == 0:
							level_matrix[(x,y,z-1)] = -1
							expand = True
						if z < max_z and level_matrix[(x,y,z+1  )] == 0:
							level_matrix[(x,y,z+1)] = -1
							expand = True

	voids = set()
	for cell in level_matrix.items():
		if cell[1] == 0:
			voids.add(cell[0])
	
	for void1 in voids:
		for void2 in cubes:
			if check_connection(void1,void2):
				sides -= 2 
	return sides 

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 58,"Test failed, expected 58, result "+str(test_value)
	
	print(main("INPUT"))
