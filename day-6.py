from math import prod


with open("inputs/day-6.txt") as file:
# with open("example_inputs/day-6.txt") as file:
    data = file.read().splitlines()
    
vert = (list(zip(*[list(line) for line in data[:-1]])))
new_nums = (",".join(["".join(x).strip() for x in vert]).split(",,"))
new_equations = [list(map(int, e.split(","))) for e in new_nums]
ops = data[-1].split()
data = list(zip(*[line.split() for line in data[:-1]]))

t1, t2 = 0, 0 
for a, b, op in zip(data, new_equations, ops):
    a = list(map(int, a))
    t1 +=  sum(a) if op == "+" else prod(a)
    t2 +=  sum(b) if op == "+" else prod(b)

print(t1)
print(t2)
