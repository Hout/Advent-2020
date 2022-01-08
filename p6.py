from collections import Counter
from itertools import combinations
from functools import reduce

puzzle_part = 2

data = [g.split("\n") for g in open("p6b.txt").read().strip().split("\n\n")]

if puzzle_part == 1:
    result = 0
    for d in data:
        s = "".join(d)
        c = Counter(s)
        i = len(c)
        result += i

    print(result)

if puzzle_part == 2:
    print(sum([len(reduce(lambda p, c: p & set(c), d, set(d[0]))) for d in data]))
