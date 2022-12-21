#!/usr/bin/python3
global vals 
global ops

def main(input_file):
	global vals
	global ops
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	ops = dict()
	vals = dict()
	for line in input_lines:
		if len(line.split()) == 2:
			vals[line.split()[0][0:4]] = int(line.split()[1])
		else:
			ops[line.split()[0][0:4]] = {"f1":line.split()[1],"f2":line.split()[3],"op":line.split()[2]}
				

	return 	operations(ops["root"])


def operations(id_op):
	global vals 
	global ops
	f1 = id_op["f1"]
	f2 = id_op["f2"]
	r1 = r2 = 0
	if f1 in vals:
		r1 = vals[f1]
	else:
		r1 = operations( ops[f1] )
		vals.update({id_op["f1"]:r1}) 
	if f2 in vals:
		r2 = vals[f2]
	else:
		r2 = operations( ops[f2] )
		vals.update({id_op["f2"]:r2})
		
	if id_op["op"] == "+":
		res = r1+r2
	elif id_op["op"] == "-":
		res = r1-r2
	elif id_op["op"] == "*":
		res = r1*r2
	else:
		res = r1//r2

	return res

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 152,"Test failed, expected 152, result "+str(test_value)
	print(main("INPUT"))
