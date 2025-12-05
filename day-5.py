with open("example_inputs/day-5.txt") as file:
    ranges, ingredients = file.read().split("\n\n")

ingredients = list(map(int, ingredients.splitlines()))
ranges = [list(map(int, _range.split("-"))) for _range in ranges.splitlines()]

def is_fresh(score):
    for lower, upper in ranges:
        if score >= lower and score <= upper:
            return True
        
    return False

print(sum([is_fresh(ingredient) for ingredient in ingredients]))

