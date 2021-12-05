import numpy as np

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

nums = [int(n) for n in lines.pop(0).split(',')]

boards = []
board = []
for line in lines[1:]:
    if not line:
        boards.append(board)
        board = []
    else:
        board.append([int(n) for n in line.strip().split()])
        
boards.append(board)

# part 1
counts = np.zeros(shape=(len(boards), 5, 5))

for num in nums:
    for i, board in enumerate(boards):
        for y, row in enumerate(board):
            if num in row:
                x = row.index(num)
                counts[i][y][x] = 1
    
    for j, count in enumerate(counts):
        if any(n for n in count.sum(axis=0) == 5) or any(j for j in count.sum(axis=1) == 5):
            break
            
    else:
        continue
        
    break

part1 = int(np.sum((1 - count) * boards[j]) * num)
print(f'part 1: {part1}')

# part 2
counts = np.zeros(shape=(len(boards), 5, 5))
index_winners = []
winning_counts = []

for num in nums:
    for i, board in enumerate(boards):
        for y, row in enumerate(board):
            if num in row and i not in index_winners:
                x = row.index(num)
                counts[i][y][x] = 1
    
    for i, count in enumerate(counts):
        if i not in index_winners and (any(n for n in count.sum(axis=0) == 5) or any(j for j in count.sum(axis=1) == 5)):
            index_winners.append(i)
            winning_counts.append((i, num, np.array(count)))

idx, num, count = winning_counts[-1]

part2 = int(np.sum((1 - count) * boards[idx]) * num)
print(f'part 2: {part2}')