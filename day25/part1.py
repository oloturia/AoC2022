#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	sum_snafu = 0
	snafu_num = 0
	for line in input_lines:
		exp = 0
		for c in range(len(line)-1,-1,-1):
			if line[c] == "=":
				snafu_num += -2*(5**exp)
			elif line[c] == "-":
				snafu_num += -1*(5**exp)
			elif line[c] == "1":
				snafu_num += 1*(5**exp)
			elif line[c] == "2":
				snafu_num += 2*(5**exp)
			exp +=1

		sum_snafu += snafu_num
		snafu_num = 0
	

	base5 = list()
	while sum_snafu > 5:
		base5.append(sum_snafu % 5)
		sum_snafu = sum_snafu//5
	base5.append(sum_snafu % 5)

	
	rep = ""
	p_rep = ""
	final_num = ""
	last_c = ""
	
	for c_i in base5:
		c = str(c_i)
		
		if c == "0" and p_rep != "":
			last_c = p_rep
		elif (c == "0" or c == "1" or c == "2") and p_rep == "":
			last_c = c
		elif c == "3" and p_rep == "":
			last_c = "="
			rep = "1"
		elif c == "4" and p_rep == "":
			last_c = "-"
			rep = "1"
		elif c == "1" and p_rep == "1":
			last_c = "2"
		elif c == "2" and p_rep == "1":
			last_c = "="
			rep = "1"
		elif c == "3" and p_rep == "1":
			last_c = "-"
			rep = "1"
		elif c == "4" and p_rep == "1":
			last_c = "0"
			rep = "1"
		
		
		final_num = last_c +final_num
		p_rep = rep
		rep = ""

	
	return 	final_num

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == "2=-1=0","Test failed, expected 2=-1=0, result "+str(test_value)
	print(main("INPUT"))
