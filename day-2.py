with open("day-2.txt") as file:
    ranges = [line.split(",") for line in file.read().splitlines()]

ranges = [list(map(int, r.split("-"))) for r in ranges]

total = 0

for start, end in ranges:
    for num in range(start, end + 1):
        str_num = str(num)
        half = len(str_num) // 2
        if str_num[0:half] == str_num[half:]:
            total += num

print(num)