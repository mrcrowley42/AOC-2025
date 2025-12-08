from itertools import combinations
import networkx as nx
import math

with open("inputs/day-8.txt") as file:
    data = [list(map(int, line.split(","))) for line in file.read().splitlines()]

def distance(a, b):
    diffs = [(p1 - p2) ** 2 for p1, p2 in zip(a, b)]
    return sum(diffs) ** 0.5
        
distances = sorted([(distance(a, b), tuple(a), tuple(b)) for a, b in combinations(data, r=2)])

g = nx.Graph()
for v, p1, p2 in distances[:1000]:
    g.add_edge(p1, p2)
components = [len(c) for c in nx.connected_components(g)]
components.sort(reverse=True)
print(math.prod(components[:3]))