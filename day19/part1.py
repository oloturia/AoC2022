#!/usr/bin/python3

blueprints = list()
max_geodes = 0
stem = dict()

def main(input_file):
	global blueprints
	global max_geodes
	global stem
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	for line in input_lines:
		blueprints.append( {"ore":(int(line.split()[6]),0,0) , "clay":(int(line.split()[12]),0,0) , "obsidian":(int(line.split()[18]),int(line.split()[21]),0) , "geode":(int(line.split()[27]),0,int(line.split()[30])) } )

	max_geodes = 0
	minutes = 0
	robots = {"ore":1,"clay":0,"obsidian":0,"geode":0}
	materials = {"ore":0,"clay":0,"obsidian":0,"geode":0}
	production = ""
	quality_level = 0
	
	for blueprint in range(len(blueprints)):
		stem = {"ore":24,"clay":24,"obsidian":24,"geode":24}
		simulation(blueprint, robots.copy(), materials.copy(), minutes, production)
		quality_level += (blueprint+1) * max_geodes
		max_geodes = 0
		
	return quality_level

def simulation(blueprint,robots,materials,minutes,production):
	global blueprints
	global max_geodes
	global stem

	while minutes < 24:
		minutes += 1

		for robot_type in ("ore","clay","obsidian"):
			if minutes > stem[robot_type] and robots[robot_type] == 0:
				return
		
		if production != "":
			if minutes < stem[production]:
				if robots[production] == 0:
					stem[production] = minutes
			robots[production] += 1
			production = ""
			

		if minutes > stem["geode"] and robots["geode"] == 0:
			return

		if materials["ore"] >= blueprints[blueprint]["geode"][0] and materials["obsidian"] >= blueprints[blueprint]["geode"][2]:
			materials["ore"] -= blueprints[blueprint]["geode"][0]
			materials["obsidian"] -= blueprints[blueprint]["geode"][2]
			production = "geode"

			if minutes < stem["geode"]:
				if robots["geode"] == 0:
					stem["geode"] = minutes
		else:
			if materials["ore"] >= blueprints[blueprint]["ore"][0]:
				new_materials = {"ore":materials["ore"] - blueprints[blueprint]["ore"][0],"clay":materials["clay"],"obsidian":materials["obsidian"],"geode":materials["geode"] }
				new_production = "ore"
				for robot_type, robot_quantity in robots.items():
					new_materials[robot_type] += robot_quantity
				simulation(blueprint,robots.copy(),new_materials,minutes,new_production)

			if materials["ore"] >= blueprints[blueprint]["clay"][0]:
				new_materials = {"ore":materials["ore"] - blueprints[blueprint]["clay"][0],"clay":materials["clay"],"obsidian":materials["obsidian"],"geode":materials["geode"] }
				new_production = "clay"
				for robot_type, robot_quantity in robots.items():
					new_materials[robot_type] += robot_quantity				
				simulation(blueprint,robots.copy(),new_materials,minutes,new_production)

			if materials["ore"] >= blueprints[blueprint]["obsidian"][0] and materials["clay"] >= blueprints[blueprint]["obsidian"][1]:
				new_materials = {"ore":materials["ore"] - blueprints[blueprint]["obsidian"][0],"clay":materials["clay"] - blueprints[blueprint]["obsidian"][1],"obsidian":materials["obsidian"],"geode":materials["geode"] }
				new_production = "obsidian"
				for robot_type, robot_quantity in robots.items():
					new_materials[robot_type] += robot_quantity				
				simulation(blueprint,robots.copy(),new_materials,minutes,new_production)
		
		for robot_type, robot_quantity in robots.items():
			materials[robot_type] += robot_quantity

			
	if materials["geode"] > max_geodes:
		max_geodes = materials["geode"]
	return

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 33,"Test failed, expected 33, result "+str(test_value)
	print("TEST OK")
	print(main("INPUT"))
