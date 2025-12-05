with open("inputs/day-5.txt") as file:
    ranges, ingredients = file.read().split("\n\n")

ingredients = list(map(int, ingredients.splitlines()))
ranges = [list(map(int, _range.split("-"))) for _range in ranges.splitlines()]

def is_fresh(score):
    for lower, upper in ranges:
        if score >= lower and score <= upper:
            return True
        
    return False

print(sum([is_fresh(ingredient) for ingredient in ingredients]))

sorted_ranges = sorted(ranges, key=lambda _range: _range[0])
output = [sorted_ranges[0]]

for lower, upper in sorted_ranges[1:]:
    last = output[-1]
    if lower <= last[1]:
        output[-1] = (last[0], max(upper, last[1]))
    else:
        output.append((lower, upper))

print(sum([(upper + 1 - lower) for lower, upper in output]))
