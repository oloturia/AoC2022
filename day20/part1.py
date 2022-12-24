#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	code_raw = list()
	code = list()
	for i,line in enumerate(input_lines):			
		code.append( {"seq":i, "num": int(line) } )
	
	for seq in range(len(code)):
		for ind,signal in enumerate(code):
			if seq == signal["seq"]:
				move = signal["num"]
				break
		if move == 0:
			continue
		code.remove(signal)
		code.insert((ind+move)%(len(code)),signal)

	for ind,signal in enumerate(code):
		if signal["num"] == 0:
			zero = ind
			break
	
	res =  code[(1000+zero)%len(code)]["num"] + code[(2000+zero)%len(code)]["num"] + code[(3000+zero)%len(code)]["num"]
	
	return res
	


if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 3,"Test failed, expected 3, result "+str(test_value)
	print(main("INPUT"))
