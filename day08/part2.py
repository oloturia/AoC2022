#!/usr/bin/python3

grid = dict()

def check_scenic(pos,edges):
	start_pos = pos
	directions = ((0,1),(0,-1),(1,0),(-1,0))
	scenic_score = 1
	for direct in directions:
		seen_trees = 0
		pos = (start_pos[0]+direct[0], start_pos[1]+direct[1])
		while not( pos[0] < 0 or pos[0] > edges[0] or pos[1] < 0 or pos[1] > edges[1]):
			if grid[start_pos] > grid[pos]:
				seen_trees +=1
			else:
				seen_trees +=1
				break
			pos = ( pos[0]+direct[0], pos[1]+direct[1] )
		scenic_score = seen_trees*scenic_score
	return scenic_score

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	for r_ind,row in enumerate(input_lines):
		for c_ind,cell in enumerate(row):
			grid[r_ind,c_ind] = cell
				
	scenic_score = 0
	max_scenic_score = 0
	for x in range(1,r_ind):
		for y in range(1,c_ind):
			scenic_score = check_scenic((x,y),(r_ind,c_ind))
			if scenic_score > max_scenic_score:
				max_scenic_score = scenic_score

	return max_scenic_score

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 8,"Test failed, expected 8, result "+str(test_value)
	print(main("INPUT"))
