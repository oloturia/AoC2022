#!/usr/bin/python3
import time
import part1
import part2

if __name__ == "__main__":
	startTime = time.time()
	res = part1.main("INPUT")
	exTime1 = (time.time() - startTime)
	print("Part 1: "+str(exTime1))
	
	startTime = time.time()
	res = part2.main("INPUT")
	exTime2 = (time.time() - startTime)
	print("Part 2: "+str(exTime2))
	print("Total : "+str(exTime1+exTime2))
