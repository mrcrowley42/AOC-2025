from collections import deque
from functools import cache

with open("inputs/day-7.txt") as file:
    data = file.read().splitlines()

start = (0, data[0].index("S"))
splits = 0
visited = {start}
queue = deque([start])
rows = len(data)
while queue:
    r, c = queue.popleft()
    nr = r + 1
    if nr >= rows: continue
    if data[nr][c] == ".":
        if (nr, c) in visited: continue
        visited.add((nr, c))
        queue.append((nr, c))
        continue
    splits += 1
    for offset in [-1, 1]:
        pos = (nr, c + offset)
        if pos in visited: continue
        visited.add(pos)
        queue.append(pos)

print(splits)


@cache
def solve(r, c):
    if r >= rows:
        return 1

    if data[r][c] == "^":
        return solve(r + 1, c + 1) + solve(r + 1, c - 1)
    
    return solve(r + 1, c)

print(solve(*start))