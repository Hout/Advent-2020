from typing import Set, Tuple, List, Sequence
from itertools import product


class Space:
    def __init__(self, dimensions: int) -> None:
        if dimensions <= 0:
            raise Exception(f"Bad number of dimensions ({dimensions})")

        self.s = set()
        self.dimensions = dimensions

    def __iter__(self):
        for e in self.s:
            yield e

    def __contains__(self, t: Tuple[int]):
        return t in self.s

    def neighbours(self, t: Tuple[int]):
        neighbours = 0
        for offset in product([-1, 0, 1], repeat=self.dimensions):
            if all([o == 0 for o in offset]):
                continue
            coords = tuple(t[d] + offset[d] for d in range(self.dimensions))
            if coords in self.s:
                neighbours += 1
        return neighbours

    def active_count(self):
        return len(self.s)

    def __getitem__(self, key: Tuple | List[Sequence]):
        if isinstance(key, Tuple):
            return key in self.s

        indices = range(*key.indices(self.dimensions))
        return [self.list[i] for i in indices]

    def __setitem__(self, key: Tuple | List[Sequence], value: bool):
        if isinstance(key, Tuple):
            self.__set__(key, value)
        else:
            indices = range(*key.indices(self.dimensions))
            for t in indices:
                self.__set__(t, value)

    def __set__(self, t: Tuple[int], value: bool):
        if len(t) != self.dimensions:
            raise Exception(f"Tuple should contain {self.dimensions} elements")
        for e in t:
            if type(e) != int:
                raise Exception(f"Tuple contains {e} which should be integer")
        if value:
            self.s.add(t)
        else:
            self.s.discard(t)

    def index_ranges(self, padding=None):
        if not padding:
            padding = 0
        mins = [
            min([coord[d] for coord in self.s]) - padding
            for d in range(self.dimensions)
        ]
        maxs = [
            max([coord[d] for coord in self.s]) + padding
            for d in range(self.dimensions)
        ]
        return [range(mins[d], maxs[d] + 1) for d in range(self.dimensions)]

    def indices(self, padding=None):
        ranges = self.index_ranges(padding=padding)
        lists = [list(r) for r in ranges]
        indices = list(product(*lists))
        for index in indices:
            yield index

    def __str__(self) -> str:
        result = ""
        ranges = self.index_ranges()
        beyond_xy_ranges = ranges[2:]
        beyond_xy_lists = [list(r) for r in beyond_xy_ranges]
        beyond_xy_indices = list(product(*beyond_xy_lists))
        for beyond_xy_index in beyond_xy_indices:
            result += f"{beyond_xy_index}:\n"
            for y in ranges[1]:
                for x in ranges[0]:
                    coord = (x, y) + beyond_xy_index
                    if coord in self.s:
                        result += "#"
                    else:
                        result += "."
                result += "\n"
        return result


lines = open("p17b.txt").read().strip().split("\n")
space = Space(3)
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch == "#":
            space[row, col, 0] = True
print(space)

for cycle in range(6):
    new_space = Space(3)
    for coords in space.indices(padding=1):
        neighbours = space.neighbours(coords)
        if space[coords]:
            if neighbours in {2, 3}:
                new_space[coords] = True
        else:
            if neighbours == 3:
                new_space[coords] = True
    space = new_space
    print(space, end="\n\n")

print(space.active_count())
