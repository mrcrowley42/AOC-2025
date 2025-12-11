with open("inputs/day-11.txt") as file:
    data = [line.replace(":", "").split() for line in file.read().splitlines()]

devices = {line[0]: line[1:] for line in data}

# queue = [("you",)]
# paths = 0
# while queue:
#     path = queue.pop()
#     current = path[-1]
#     if current == "out":
#         paths += 1
#         continue
#     for child in devices[current]:
#         queue.append((path) + (child,))

# print(paths)

queue = [("svr",)]
paths = 0
while queue:
    path = queue.pop()
    current = path[-1]
    if current == "out":
        paths += 1
        if "fft" in path and "dac" in path:
            print("done")
            paths += 1
        continue
    for child in devices[current]:
        queue.append((path) + (child,))

print(paths)