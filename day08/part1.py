#!/usr/bin/python3

grid = dict()

def check_visibility(pos,edges):
	start_pos = pos
	directions = ((0,1),(0,-1),(1,0),(-1,0))
	for direct in directions:
		pos = (start_pos[0]+direct[0], start_pos[1]+direct[1])
		blocked = False	
		while not( pos[0] < 0 or pos[0] > edges[0] or pos[1] < 0 or pos[1] > edges[1]):
			if grid[pos] >= grid[start_pos]:
				blocked = True
				break
			pos = ( pos[0]+direct[0], pos[1]+direct[1] )
		if not blocked:
			return 1
	return 0

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	for r_ind,row in enumerate(input_lines):
		for c_ind,cell in enumerate(row):
			grid[r_ind,c_ind] = cell
	
	count_trees = 0
	for x in range(1,r_ind):
		for y in range(1,c_ind):
			count_trees += check_visibility((x,y),(r_ind,c_ind))

	count_trees += (r_ind * 2 + c_ind * 2) 
	return count_trees

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 21,"Test failed, expected 21, result "+str(test_value)
	print(main("INPUT"))
