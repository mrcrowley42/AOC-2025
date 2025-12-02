with open("inputs/day-2.txt") as file:
    ranges = [list(map(int, r.split("-"))) for r in file.read().split(",")]

def is_invalid(str_num, j):
    last = None
    for i in range(0, len(str_num) + 1, j):
        sub_str = str_num[i:i+j]
        if not sub_str:
            continue
        if not last:
            last = sub_str
            continue
        if sub_str != last:
            return False
    return True


total_1, total_2 = 0, 0
for start, end in ranges:
    for num in range(start, end + 1):
        str_num = str(num)
        len_num = len(str_num)
        half = len(str_num) // 2
        if str_num[0:half] == str_num[half:]:
            total_1 += num
        for j in range(1, half + 1):
            if len_num % j != 0:
                continue      
            if is_invalid(str_num, j):
                total_2 += num
                break
print(total_1)
print(total_2)
