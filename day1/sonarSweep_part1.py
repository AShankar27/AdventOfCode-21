'''
Day 1
Sonar sweep
Calculate increasing numbers
'''

def readInputFile(file_name):
	ip_array = []
	ip = open(file_name, 'r')
	lines = ip.readlines()

	for line in lines:
		ip_array.append(int(line.strip()))

	return ip_array


input_array = readInputFile("input.txt")
res = 0
for i in range(1, len(input_array)):
	if input_array[i] > input_array[i-1]:
		res += 1

print(res, len(input_array))


