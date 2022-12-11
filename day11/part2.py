#!/usr/bin/python3

def operation(wor,op_string):
	trm = lambda s: wor if s == 'old' else int(s)
	opr = lambda o1,o2,s: o1 + o2 if s == '+' else o1 * o2
	return opr( trm(op_string[0]), trm(op_string[2]),op_string[1] )

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	monkeys = dict()
	factor = 1
	for line_no in range(0,len(input_lines),7):
		monkey = int(input_lines[line_no].split()[1][0])
		monkeys[monkey] = {'inspected':0,'items': [ int(x) for x in input_lines[line_no+1][18:].replace(',','').split()], 'operations': input_lines[line_no+2].split()[3:], 'test': int(input_lines[line_no+3].split()[3]), 'true': int(input_lines[line_no+4].split()[5]), 'false': int(input_lines[line_no+5].split()[5])}
		factor *= monkeys[monkey]['test']
	
	for i in range (0,10000):
		for monkey in monkeys.values():
			for item in monkey['items']:
				monkey['inspected'] +=1
				worry_level = operation(item,monkey['operations'])
				if worry_level%monkey['test'] == 0:
					monkeys[monkey['true']]['items'].append(worry_level%factor)
				else:
					monkeys[monkey['false']]['items'].append(worry_level%factor)
			monkey['items'] = []
			
	inspected = list()
	for m in monkeys.values():
		inspected.append(m['inspected'])		
	inspected.sort()

	return inspected[-1]*inspected[-2]

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 2713310158,"Test failed, expected 2713310158 result "+str(test_value)
	print(main("INPUT"))
