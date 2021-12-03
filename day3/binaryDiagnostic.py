'''
Day 3 of Advent of Code
Binary Diagnostic: Find the power consumption
'''

epsilon = '';
gamma = '';


file_name = "input.txt"
ip = open(file_name, 'r')
lines = ip.readlines()

numBits = len(lines[0].strip())

common_vals = {k:0 for k in range(1, numBits+1)}

for line in lines:
	for i, c in enumerate(line.strip()):
		if c == '1':
			common_vals[i+1] += 1
		else:
			common_vals[i+1] -= 1

print(common_vals)

for i in range(1, numBits+1):
	if common_vals[i] > 0:
		gamma = gamma + '1'
		epsilon = epsilon + '0'
	else:
		gamma = gamma + '0'
		epsilon = epsilon + '1'

print(int(gamma, 2) * int(epsilon,2))
