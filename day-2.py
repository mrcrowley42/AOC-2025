from time import time
def main():
    s = time()
    with open("inputs/day-2.txt") as file:
        ranges = [list(map(int, r.split("-"))) for r in file.read().split(",")]

    total_1 = 0
    total_2 = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            str_num = str(num)
            half = len(str_num) // 2
            if str_num[0:half] == str_num[half:]:
                total_1 += num
            for j in range(1, half + 1):
                if len(str_num) % j != 0:
                    continue
                if len({str_num[i:i+j] for i in range(0, len(str_num) + 1, j) if len(str_num[i:i+j])}) == 1:
                    total_2 += num
                    break
                
    print(time() - s)
    print(total_1)
    print(total_2)

main()