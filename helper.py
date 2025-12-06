
for i in range(1, 13):
    # with open(f"example_inputs/day-{i}.txt", "x") as file:
    #     pass
    # with open(f"inputs/day-{i}.txt", "x") as file:
    #     pass
    with open(f"day-{i}.py", "wt") as file:
        file.write(f"""with open("example_inputs/day-{i}.txt") as file:
    data = file.read().splitlines()

print(data)
""")