'''
Day 1
Sonar sweep 2
Calculate increasing numbers in sliding window of size 3
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

# print(input_array[0:3])

for i in range(0, len(input_array)-3):
	window1 = sum(input_array[i:i+3])
	window2 = sum(input_array[i+1:i+4])
	if window2 > window1:
		res += 1

print(res)