with open("inputs/day-1.txt", "rt") as file:
    data = [((1 if line[0] == "R" else -1) , int(line[1:])) for line in file.read().splitlines()]

total_1, total_2 = 0, 0
position = 50
for delta, turns in data:
    for _ in range(turns):
        position = (position + delta) % 100
        if position == 0:
            total_2 += 1
    if position == 0:
        total_1 += 1

print(total_1)
print(total_2)