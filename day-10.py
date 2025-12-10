from collections import deque
from time import time
from heapq import heappush, heappop

s = time()

with open("inputs/day-10.txt") as file:
    data = [line.split() for line in file.read().splitlines()]


def get_presses(line):
    lights, buttons, jolts = line[0], line[1:-1], line[-1]
    buttons = [list(map(int, group[1:-1].split(','))) for group in buttons]
    lights = lights[1:-1]
    start = "".join(['.' for _ in range(len(lights))])
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        state, pressed = queue.popleft()
        if state == lights:
            return pressed
        for button in buttons:
            new_state = list(state)
            for index in button:
                current = state[index]
                new_state[index] = "." if current == "#" else "#"
            new_state = "".join(new_state)
            if new_state in visited: continue
            queue.append((new_state, pressed + 1))
            visited.add(new_state)
    
total = sum([get_presses(line) for line in data])
print(total)

def get_presses_jolts(line):
    print("done")
    lights, buttons, jolts = line[0], line[1:-1], line[-1]
    buttons = [list(map(int, group[1:-1].split(','))) for group in buttons]
    jolts_required = tuple(map(int, jolts[1:-1].split(",")))
    total_jolts = sum(jolts_required)
    start = tuple([0 for _ in range(len(jolts_required))])
    queue = [(0, start, 0)]
    fewest_presses = {start: 0}
    # visited = {start}
    while queue:
        weight, state, pressed = heappop(queue)
        # print(weight, state, pressed)
        for button in buttons:
            new_state = list(state)
            for index in button:
                new_state[index] += 1
            new_state = tuple(new_state)
            
            if new_state == jolts_required:
                return pressed + 1
            
            if any([new_state[i] > jolts_required[i] for i in range(len(jolts_required))]):
                continue
            
            if new_state in fewest_presses.keys():
                if pressed + 1 >= fewest_presses[new_state]:
                    continue
            
            fewest_presses[new_state] = pressed + 1
            new_weight = (total_jolts - sum(new_state))
            heappush(queue, (new_weight + pressed + 1 , new_state, pressed + 1))
    
# total = sum([get_presses_jolts(line) for line in data])

print(total)
print(time() - s)