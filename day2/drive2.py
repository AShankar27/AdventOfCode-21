'''
Day 2 of Advent of Code
Drive: Find final depth and position of submarine
based on aim and position
'''

depth = 0
position = 0
aim = 0

file_name = "input.txt"
ip = open(file_name, 'r')
lines = ip.readlines()
for line in lines:

	dist = int(line.split(" ")[1])

	if "forward" in line:
		position += dist
		depth += aim*dist
	elif "up" in line:
		aim -= dist
	elif "down" in line:	
		aim += dist
	else:
		continue

print(depth*position)