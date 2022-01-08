import re
from collections import Counter

puzzle_part = 2

regex = re.compile(r"(\d+)-(\d+)\s+([a-z]):\s+([a-z]+)")
data = [
    (int(d[0]), int(d[1]), d[2], d[3])
    for d in [
        regex.match(line).groups()
        for line in open("p2a.txt").read().strip().split("\n")
    ]
]

if puzzle_part == 1:
    valid = sum([1 if d[0] <= Counter(d[3])[d[2]] <= d[1] else 0 for d in data])
    print(valid)

if puzzle_part == 2:
    valid = sum(
        [1 if Counter(d[3][d[0] - 1] + d[3][d[1] - 1])[d[2]] == 1 else 0 for d in data]
    )
    print(valid)
