#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	hmap = dict()
	bounds = dict()
	for x_cell,line in enumerate(input_lines):
		for y_cell,char in enumerate(line):
			hmap[(x_cell,y_cell)] = char
			if char == 'S':
				start = (x_cell,y_cell)
				hmap[x_cell,y_cell] = 'a'
			elif char == 'E':
				end = (x_cell,y_cell)
				hmap[x_cell,y_cell] = 'z'
		bounds['y'] = y_cell +1
	bounds['x'] = x_cell+1
	
	wmap = dict()
	directions = [{'x':0,'y':1},{'x':0,'y':-1},{'x':1,'y':0},{'x':-1,'y':0}]

	for x in range(0,bounds['x']):
		for y in range(0,bounds['y']):	
			wmap[(x,y)] = dict()
			for d in directions:
				if not( x+d['x'] == -1 or x+d['x'] == bounds['x'] or y+d['y'] == -1 or y+d['y'] == bounds['y'] ):
					if ord(hmap[(x+d['x'],y+d['y'])]) -1 <= ord(hmap[(x,y)]):# <= ord(hmap[(x+d['x'],y+d['y'])]):
						wmap[(x,y)][ (x+d['x'], y+d['y']) ] = 1
					else:
						wmap[(x,y)][ (x+d['x'], y+d['y']) ] = float("inf")
	
	

	path = {}
	adj_node = {}
	queue = []
	
	for node in wmap:
		path[node] = float("inf")
		adj_node[node] = None
		queue.append(node)
	path[start] = 0
	while queue:
		key_min = queue[0]
		min_val = path[key_min]
		for n in range(1, len(queue)):
			if path[queue[n]] < min_val:
				key_min = queue[n]
				min_val = path[key_min]
		cur = key_min
		queue.remove(cur)
		for i in wmap[cur]:
			alternate = wmap[cur][i] + path[cur]
			if path[i] > alternate:
				path[i] = alternate
				adj_node[i] = cur
	path_dim = 0
	while True:
		end = adj_node[end]
		
		if end is None:
			break
		path_dim +=1
	
		
	return path_dim

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 31,"Test failed, expected 31, result "+str(test_value)
	print(main("INPUT"))
