import re
from typing import Tuple, Set, Dict, Counter

puzzle_part = 2

MainBagType = Tuple[str, str]
ContainedBagTypes = Counter[MainBagType]
Data = Dict[MainBagType, ContainedBagTypes]

data: Data = {
    tuple(re.findall(r"^(\w+ \w+)", line)[0].split()): ContainedBagTypes(
        {
            (a[1], a[2]): int(a[0])
            for a in [b.split() for b in re.findall(r"(\d+ \w+ \w+)", line)]
        }
    )
    for line in open("p7b.txt").read().strip().split("\n")
}


def bags_can_contain(t: MainBagType) -> Set[MainBagType]:
    global data

    bag_types = {
        main_bag
        for main_bag, contained_bags in data.items()
        if t in contained_bags.keys()
    }
    if bag_types == []:
        return set()

    return bag_types | {
        item for sublist in [bags_can_contain(b) for b in bag_types] for item in sublist
    }


def bag_contains(t: MainBagType) -> ContainedBagTypes:
    global data

    result = data.get(t, ContainedBagTypes())
    if len(result) == 0:
        return result

    new_result = result.copy()
    for b, n in result.items():
        new_result += {k: v * n for k, v in bag_contains(b).items()}

    return new_result


if puzzle_part == 1:
    print(len(bags_can_contain(("shiny", "gold"))))

if puzzle_part == 2:
    c = bag_contains(("shiny", "gold"))
    print(c)
    print(sum(c.values()))
