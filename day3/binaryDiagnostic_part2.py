'''
Day 3 of Advent of Code
Binary Diagnostic: Find the power consumption
'''

file_name = "input.txt"
ip = open(file_name, 'r')
lines_org = ip.readlines()


ox = lines_org.copy()
co2 = lines_org.copy()

numBits = len(lines_org[0].strip())

lines = lines_org.copy()

for i in range(1, numBits+1):
	# print(lines)
	if len(lines) == 1:
		break
	count = 0
	for line in lines:
		line = line.strip()
		if line[i-1] == '1':
			count += 1
		else:
			count -= 1

	# print("count = ", count)
	for line in lines:
		if count >= 0:
			if line.strip()[i-1] == '0':
				# print(line)
				ox.remove(line)
		else:
			if line.strip()[i-1] == '1':
				ox.remove(line)

	lines = ox.copy()


lines = lines_org.copy()

for i in range(1, numBits+1):

	if len(lines) == 1:
		break

	count = 0
	for line in lines:
		line = line.strip()
		if line[i-1] == '1':
			count += 1
		else:
			count -= 1

	# print("count = ", count)
	for line in lines:
		if count >= 0:
			if line.strip()[i-1] == '1':
				# print(line)
				co2.remove(line)
		else:
			if line.strip()[i-1] == '0':
				co2.remove(line)

	lines = co2.copy()

print(int(ox[0].strip(),2) * int(co2[0].strip(),2))



