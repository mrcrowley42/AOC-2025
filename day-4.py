with open("inputs/day-4.txt") as file:
    rolls = [list(row) for row in file.read().splitlines()]

directions = [(0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 0), (1, 1)]
rows = len(rolls)
cols = len(rolls[0])

def can_move(r, c):
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            continue
        if rolls[nr][nc] == "@":
            count += 1
            
    return count < 4

total = 0
for r, row in enumerate(rolls):
    for c, value in enumerate(row):
        if value != "@":
            continue
        if can_move(r, c):
            total += 1

print(total)
