#!/usr/bin/python3
valves = dict()
distances = dict()
path = list()

def shortest_path(graph, n1, n2):
	path_list = [[n1]]
	path_index = 0
	prev_nodes = {n1}
	if n1 == n2:
		return path_list[0]
		
	while path_index < len(path_list):
		cur_path = path_list[path_index]
		last_node = cur_path[-1]
		next_nodes = graph[last_node]
		if n2 in next_nodes:
			cur_path.append(n2)
			return cur_path
		
		for node in next_nodes:
			if not node in prev_nodes:
				new_path = cur_path[:]
				new_path.append(node)
				path_list.append(new_path)
				prev_nodes.add(node)
		path_index += 1
	return []
	
def main(input_file):
	global valves
	global distances
	global path

	valves = {}
	distances = {}
	path = []
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	for line in input_lines:
		valves[line.split()[1]] = {'fl':int(line.split()[4].split("=")[1].replace(";","")),'tn':line.replace(",","").split()[9:]}
	
	graph = dict()
	for valve_name,valve_value in valves.items():
		graph[valve_name] = valve_value['tn']
	
	for valve_name,valve_value in valves.items():
		if valve_value['fl'] > 0 or valve_name == 'AA':
			distances[valve_name] = dict()
	
	for d1 in distances:
		for d2 in distances:
			if d1 == d2 or d2 == 'AA':
				continue 
			else:
				distances[d1].update({d2:len(shortest_path(graph,d1,d2))-1})

	max_value = 0
	elements = list()

	for dist in distances['AA'].keys():
			elements.append(dist)		
	
	complete = len(elements)

	pos = "AA"
	minutes = 30
	while len(path) < len(elements):		
		best_value = -1
		best_valve = ""
		for valve in elements:
			if valve in path:
				continue
			dist = distances[pos][valve]
			if minutes - (dist+1) >= 0:
				value = calc_valve(valve,elements,dist,minutes)

			if value > best_value:
				best_value = value
				best_valve = valve
		path.append(best_valve)
		
		minutes = calc_route("AA",path)[1]
		pos = best_valve

	max_value = calc_route("AA",path)
	return max_value[0]

def calc_route(start,route):
	global valves
	global distances
	pos = start
	flow = 0
	minutes = 30
	for element in route:
		minutes -= distances[pos][element] +1
		if minutes <= 0:
			minutes = 0
			break
		flow += valves[element]['fl'] * minutes
		pos = element
	return flow,minutes
	
def calc_valve(valve,elements,dist,minutes):
	global valves
	global distances
	local_elements = elements.copy()
	local_elements.pop(elements.index(valve))
	minutes -= dist +1

	best_value = 0
	best_valve = ""
	local_value = minutes * valves[valve]['fl']

	
	for valve_to in local_elements:
		if valve_to in path:
			continue
		dist = distances[valve][valve_to]
		if minutes - (dist+1) <= 0:
			return local_value
			
		value = calc_valve(valve_to,local_elements,dist, minutes)

		if value > best_value:
			best_value = value

	return best_value + local_value
	
if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 1651,"Test failed, expected 1651, result "+str(test_value)
	print(main("INPUT"))
