#!/usr/bin/python3
from itertools import combinations
from itertools import permutations

valves = dict()
distances = dict()
cache = dict()

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
	global cache
	
	valves = {}
	distances = {}
	cache = dict()
	
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

	elements = list()
	for dist in distances['AA'].keys():
			elements.append(dist)		
	
	poss_combinations = list()
	for i in range(len(elements)+1):
		poss_combinations += list(combinations(elements,i))
	
	best_value = 0
	best_choice = tuple()

	if len(elements) < 10:
		factor = 0
	else:
		factor = 5

	for human_unsorted in poss_combinations:
		
		if human_unsorted == () or len(human_unsorted) >= len(elements)-factor:
			continue

		human = tuple(sorted(human_unsorted))					
		if human in cache:
			value_human = cache[human][0]
		else:
			value_human = best_path(human)
		for elephant_unsorted in poss_combinations:
			
			elephant = tuple(sorted(elephant_unsorted))
			if len(set(human).intersection(set(elephant))) == 0:
				if elephant == () or len(elephant) >= len(elements)-factor:
					continue
				if elephant in cache:
					value_elephant = cache[elephant][0]
				else:
					cached_value = 0
					cached_minutes = 0
					cached_path = tuple()
					
					for v_index in range(len(elephant),1,-1):
						if elephant[:v_index] in cache:
							cached_value = cache[elephant[:v_index]][0]
							cached_minutes = cache[elephant[:v_index]][1]
							cached_path = elephant[:v_index]
							uncached_path = elephant[v_index:]
							break
							
					if cached_value == 0:
						value_elephant = best_path(elephant)
					else:
						value_elephant = best_path(uncached_path,minutes_orig=cached_minutes,partial=cached_path,orig_value=cached_value)

				if (value_human + value_elephant) > best_value:
					best_value = value_human + value_elephant
	return best_value					

	
def best_path(orig_path,minutes_orig=26,partial=tuple(),orig_value=0):
	global distances
	global cache
	global min_cache_len
	
	best_value = orig_value
	best_value = 0
	perma_path = permutations(orig_path)	

	for path in perma_path:
		value = 0
		curr_pos = "AA"	
		minutes = minutes_orig
		minutes = 26
		for i,step in enumerate(path):
			minutes -= distances[curr_pos][step]+1
			if minutes < 0:
				break
			curr_pos = step
			value += valves[step]['fl']*minutes
		if value > best_value:
			best_value = value
			
	cache.update({orig_path:(best_value,minutes)})
	return best_value

	
if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 1707,"Test failed, expected 1707, result "+str(test_value)
	print(main("INPUT"))
