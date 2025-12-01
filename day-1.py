with open("example_inputs/day-1.txt", "rt") as file:
    data = file.read().splitlines()

position = 50
count = 0
for line in data:
    direction = 1 if line[0] == "R" else -1
    amount = int(line[1:])
    position = (position + (direction * amount)) % 99
    if position == 0:
        count += 1

print(count)