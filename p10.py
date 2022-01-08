from collections import Counter
from itertools import product
from typing import Dict, List, Tuple

data = [int(line) for line in open("p10c.txt").read().strip().split("\n")]
data.append(0)
data.sort()
data.append(data[-1] + 3)

c = Counter()
for i in range(len(data) - 1):
    c[data[i + 1] - data[i]] += 1

# part 1
print(c, c[1] * c[3])

# part 2

Dag = Dict[int, Tuple[int, List[int]]]

cache = dict()


def count_paths(dag: Dag, from_index: int = None, to_index: int = None) -> int:
    if not from_index:
        from_index = min(dag.keys())
    if not to_index:
        to_index = max(dag.keys())

    if from_index == to_index:
        return 1

    if (from_index, to_index) in cache:
        return cache[(from_index, to_index)]

    _, next_lst = dag[from_index]
    paths = 0
    for next in next_lst:
        paths += count_paths(dag, next, to_index)
    cache[(from_index, to_index)] = paths
    return paths


def get_possibilities(data):
    # create dag
    dag = dict([(i, (data[i], [i + 1])) for i in range(len(data) - 1)])
    dag[len(data) - 1] = (data[-1], [])
    for i, (value, next_lst) in dag.items():
        next_lst += [
            j for j in range(i + 2, min(i + 4, len(data))) if data[j] - data[i] <= 3
        ]

    # count number of paths
    return count_paths(dag)


def get_possibilities2(data):
    possibilities = 0
    print("data")
    print(data)
    for c in product([True, False], repeat=len(data) - 2):
        dd = [True] + list(c) + [True]
        this_data = [d for d, b in zip(data, dd) if b]
        series_contains_differences_greater_than_3 = False
        for i in range(len(this_data) - 1):
            if this_data[i + 1] - this_data[i] > 3:
                series_contains_differences_greater_than_3 = True
                break
        if not series_contains_differences_greater_than_3:
            possibilities += 1
            print(
                f"possibility: {this_data}, missing {[d for d, b in zip(data, dd) if not b]}"
            )
    return possibilities


# testp = get_possibilities
# assert testp([0, 3]) == 1
# assert testp([0, 1, 4]) == 1
# assert testp([0, 3, 4, 7]) == 1
# assert testp([0, 3, 6, 9]) == 1
# assert testp([0, 3, 4, 5, 8]) == 2
# assert testp([0, 3, 5, 6, 9]) == 2
# assert testp([0, 3, 4, 6, 9]) == 2
# assert testp([0, 3, 4, 5, 6, 9]) == 4
# assert testp([0, 3, 4, 5, 6, 7, 10]) == 7
# assert testp([0, 3, 4, 5, 6, 7, 8, 11]) == 13
# assert testp([0, 3, 5, 6, 8, 11]) == 3
# assert testp([0, 3, 4, 5, 6, 8, 11]) == 6

print(get_possibilities(data))
