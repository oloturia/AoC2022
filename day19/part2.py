#!/usr/bin/python3

blueprints = list()
max_geodes = list()
cache = set()

def main(input_file):
	global blueprints
	global max_geodes
	global cache

	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	del(blueprints)
	blueprints = list()
	
	for line in input_lines:
		blueprints.append( {"ore":(int(line.split()[6]),0,0) , "clay":(int(line.split()[12]),0,0) , "obsidian":(int(line.split()[18]),int(line.split()[21]),0) , "geode":(int(line.split()[27]),0,int(line.split()[30])) } )
		if (len(blueprints) == 3):
			break

	max_geodes = []
	max_geodes = [1]*len(blueprints)
	minutes = 0
	robots = {"ore":1,"clay":0,"obsidian":0,"geode":0}
	materials = {"ore":0,"clay":0,"obsidian":0,"geode":0}
	production = ""
	
	for blueprint in range(len(blueprints)):
		cache = set()		
		simulation(blueprint, robots.copy(), materials.copy(), minutes, production)
	
	res = 1
	for best_results in max_geodes:	
		res = res*best_results
	return res

def simulation(blueprint,robots,materials,minutes,production):
	global blueprints
	global max_geodes
	global cache

	while minutes < 32:
		minutes += 1
		
		if production != "":
			robots[production] += 1
			production = ""
			
		if (robots["ore"],robots["clay"],robots["obsidian"],materials["ore"],materials["clay"],materials["obsidian"],minutes) in cache:
			return
		else:
			cache.add((robots["ore"],robots["clay"],robots["obsidian"],materials["ore"],materials["clay"],materials["obsidian"],minutes))

		if materials["ore"] >= blueprints[blueprint]["geode"][0] and materials["obsidian"] >= blueprints[blueprint]["geode"][2]:
			new_materials = {"ore":materials["ore"] - blueprints[blueprint]["geode"][0],"clay":materials["clay"],"obsidian":materials["obsidian"] - blueprints[blueprint]["geode"][2],"geode":materials["geode"] }
			new_production = "geode"
			for robot_type, robot_quantity in robots.items():
				new_materials[robot_type] += robot_quantity
			simulation(blueprint,robots.copy(),new_materials,minutes,new_production)

		if materials["ore"] >= blueprints[blueprint]["ore"][0] and max(blueprints[blueprint]["geode"][0],blueprints[blueprint]["obsidian"][0]) > robots["ore"]:
			new_materials = {"ore":materials["ore"] - blueprints[blueprint]["ore"][0],"clay":materials["clay"],"obsidian":materials["obsidian"],"geode":materials["geode"] }
			new_production = "ore"
			for robot_type, robot_quantity in robots.items():
				new_materials[robot_type] += robot_quantity
			simulation(blueprint,robots.copy(),new_materials,minutes,new_production)

		if materials["ore"] >= blueprints[blueprint]["clay"][0] and blueprints[blueprint]["obsidian"][1] > robots["clay"]:
			new_materials = {"ore":materials["ore"] - blueprints[blueprint]["clay"][0],"clay":materials["clay"],"obsidian":materials["obsidian"],"geode":materials["geode"] }
			new_production = "clay"
			for robot_type, robot_quantity in robots.items():
				new_materials[robot_type] += robot_quantity				
			simulation(blueprint,robots.copy(),new_materials,minutes,new_production)

		if materials["ore"] >= blueprints[blueprint]["obsidian"][0] and materials["clay"] >= blueprints[blueprint]["obsidian"][1] and blueprints[blueprint]["geode"][2] > robots["obsidian"]:
			new_materials = {"ore":materials["ore"] - blueprints[blueprint]["obsidian"][0],"clay":materials["clay"] - blueprints[blueprint]["obsidian"][1],"obsidian":materials["obsidian"],"geode":materials["geode"] }
			new_production = "obsidian"
			for robot_type, robot_quantity in robots.items():
				new_materials[robot_type] += robot_quantity				
			simulation(blueprint,robots.copy(),new_materials,minutes,new_production)
		
		for robot_type, robot_quantity in robots.items():
			materials[robot_type] += robot_quantity

			
	if materials["geode"] > max_geodes[blueprint]:
		max_geodes[blueprint] = materials["geode"]

	return

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 3472,"Test failed, expected 3472, result "+str(test_value)
	
	print(main("INPUT"))
