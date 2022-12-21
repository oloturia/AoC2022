#!/usr/bin/python3
global vals 
global ops


def main(input_file, factor):
	global vals
	global ops
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	ops = dict()
	orig_vals = dict()
	for line in input_lines:
		if len(line.split()) == 2:
			orig_vals[line.split()[0][0:4]] = int(line.split()[1])
		else:
			ops[line.split()[0][0:4]] = {"f1":line.split()[1],"f2":line.split()[3],"op":line.split()[2]}
	humn = 3343167719440
	vals = orig_vals
	conf2 = operations(ops[ops["root"]["f2"]])
	humn= prev_humn =0
	res = 0
	if factor > 1:
		while True:
			vals = orig_vals.copy()
			vals["humn"] = humn
			conf1 = operations(ops[ops["root"]["f1"]])
			if conf1 == "error":
				humn +=factor
				continue		
			if conf1 == conf2:
				break
			if conf1 < conf2:		
				humn = prev_humn
				factor = factor//10
			else:
				prev_humn = humn
				humn += factor		

		while True:
			vals = orig_vals.copy()
			vals["humn"] = humn
			conf1 = operations(ops[ops["root"]["f1"]])
			if conf1 == "error":
				humn -= 1
				continue
			return(vals["humn"])

	else:
		while True:
			vals = orig_vals.copy()
			vals["humn"] = humn
			conf1 = operations(ops[ops["root"]["f1"]])
			if conf1 != conf2:
				humn += 1
			else:
				return humn
			


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
		if r1 == "error":
			return "error"
		vals.update({id_op["f1"]:r1}) 
	if f2 in vals:
		r2 = vals[f2]
	else:
		r2 = operations( ops[f2] )
		if r2 == "error":
			return "error"
		vals.update({id_op["f2"]:r2})
		
	if id_op["op"] == "+":
		res = r1+r2
	elif id_op["op"] == "-":
		res = r1-r2
	elif id_op["op"] == "*":
		res = r1*r2
	else:
		if r1%r2 == 0:
			res = r1//r2
		else:
			return "error"

	return res

if __name__ == "__main__":
	test_value = main("TEST",1)
	assert test_value == 301,"Test failed, expected 301, result "+str(test_value)
	print(main("INPUT",factor = 100000000))
