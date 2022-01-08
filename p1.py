from itertools import combinations

puzzle_part = 2


def product(lst):
    if lst == []:
        return 0
    result = 1
    for i in lst:
        result *= i
    return result


data = [int(line) for line in open("p1b.txt").read().strip().split("\n")]

for c in combinations(data, 2 if puzzle_part == 1 else 3):
    if sum(c) == 2020:
        print(product(c))
        continue
