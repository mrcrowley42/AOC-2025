with open("inputs/day-3.txt") as file:
    data = [list(map(int, list(line))) for line in file.read().splitlines()]


def get_total_jolts(n):
    """Check for the first highest number, keeping enough room to end up with ``n`` batteries."""
    total = 0
    for bank in data:
        batteries = []
        for i in range((-1 * n) + 1, 0, 1):
            highest = max(bank[:i])
            batteries.append(highest)
            bank = bank[bank.index(highest)+1:]
        batteries.append(max(bank))
        total += int("".join(map(str, batteries)))
        
    return total

print(get_total_jolts(2))
print(get_total_jolts(12))
