#!/usr/bin/python3
CRT = dict()

def draw_pixel(cycle, cursor):
	row = (cycle//40)%6
	col = cycle%40
	if cursor == col or cursor +1 == col or cursor -1 == col:
		CRT[row][col] = 1
	return 1

def render():
	bitmap = ""
	for row in CRT.values():
		for col in row:
			if col == 1:
				bitmap += "#"
			else:
				bitmap += "."
		bitmap += "\n"
	return bitmap
	
def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	regX = 1
	cycle = 0
	for row in range(0,6):
		CRT[row] = [0,]*40
		
	for line in input_lines:
		if line == "noop":
			cycle += draw_pixel(cycle,regX)
		else:
			cycle += draw_pixel(cycle,regX)
			cycle += draw_pixel(cycle,regX)
			regX += int(line.split()[1])
	return render()

if __name__ == "__main__":
	test_value = main("TEST")
	test_result = """##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....\n"""
	assert test_value == test_result,"Test failed, expected\n"+test_result+"\nresult \n"+str(test_value)
	print(main("INPUT"))
