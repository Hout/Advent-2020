from collections import defaultdict

lines = open("p15a.txt").read().strip().split("\n")
for line in lines:
    numbers = [int(n) for n in line.split(",")]
    d = defaultdict(list)
    for i, n in enumerate(numbers):
        d[n].append(i)
    last_number = numbers[-1]
    # for i in range(len(numbers), 2020):
    for i in range(len(numbers), 30000000):
        new_number = (
            d[last_number][-1] - d[last_number][-2] if len(d[last_number]) >= 2 else 0
        )
        last_number = new_number
        d[new_number].append(i)
    print(line, new_number)
