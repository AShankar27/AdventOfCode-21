'''
Day 2 of Advent of Code
Drive: Find final depth and position of submarine
'''

depth = 0
position = 0

file_name = "input_ex.txt"
ip = open(file_name, 'r')
lines = ip.readlines()
for line in lines:
	if "forward" in line:
		dist = int(line.split(" ")[1])
		position += dist
	elif "up" in line:
		dist = int(line.split(" ")[1])
		depth -= dist
	elif "down" in line:
		dist = int(line.split(" ")[1])
		depth += dist

print(depth*position)

