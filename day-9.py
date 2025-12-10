from math import prod
from itertools import combinations

with open("inputs/day-9.txt") as file:
    data = [list(map(int, line.split(","))) for line in file.read().splitlines()]

def square_size(a, b):
    return prod([abs(p1 - p2) + 1 for p1, p2 in zip(a, b)])

print(max(square_size(a, b) for a, b in combinations(data, r=2)))