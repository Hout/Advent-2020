from collections import Counter
import numpy as np
from itertools import product

data = np.array([list(line) for line in open("p11a.txt").read().strip().split("\n")])

puzzle_part = 2


def occupied_adjacent(data, r, c):
    adjacent = data[
        max(r - 1, 0) : min(r + 2, len(data)),
        max(c - 1, 0) : min(c + 2, len(row)),
    ]
    unique, counts = np.unique(
        adjacent,
        return_counts=True,
    )
    counter = Counter(dict(zip(unique, counts)))
    occupied_adjacent_seats = counter["#"]
    if seat == "#":
        occupied_adjacent_seats -= 1
    return occupied_adjacent_seats


def occupied_all_dirs(data: np.array, r, c):
    occupied = 0
    for direction in [
        np.array(d) for d in product([-1, 0, 1], repeat=2) if d != (0, 0)
    ]:
        cr, cc = (r + direction[0], c + direction[1])
        while 0 <= cr < np.shape(data)[0] and 0 <= cc < np.shape(data)[1]:
            if data[cr, cc] == "#":
                occupied += 1
                break
            cr, cc = (cr + direction[0], cc + direction[1])
    return occupied


if puzzle_part == 1:
    old_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
    new_data = data.copy()
    while not np.array_equal(old_data, new_data):
        old_data = new_data
        new_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
        print()
        for r, row in enumerate(old_data):
            for c, seat in enumerate(row):
                occupied_adjacent_seats = occupied_adjacent(old_data, r, c)

                if seat == "L" and occupied_adjacent_seats == 0:
                    new_data[r, c] = "#"
                elif seat == "#" and occupied_adjacent_seats >= 5:
                    new_data[r, c] = "L"
                else:
                    new_data[r, c] = seat
        print(new_data)

    unique, counts = np.unique(
        new_data,
        return_counts=True,
    )
    counter = Counter(dict(zip(unique, counts)))
    occupied_seats = counter["#"]
    print(occupied_seats)

if puzzle_part == 2:
    old_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
    new_data = data.copy()
    while not np.array_equal(old_data, new_data):
        old_data = new_data
        new_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
        print()
        for r, row in enumerate(old_data):
            for c, seat in enumerate(row):
                occupied_adjacent_seats = occupied_all_dirs(old_data, r, c)

                if seat == "L" and occupied_adjacent_seats == 0:
                    new_data[r, c] = "#"
                elif seat == "#" and occupied_adjacent_seats >= 4:
                    new_data[r, c] = "L"
                else:
                    new_data[r, c] = seat
        print(new_data)

    unique, counts = np.unique(
        new_data,
        return_counts=True,
    )
    counter = Counter(dict(zip(unique, counts)))
    occupied_seats = counter["#"]
    print(occupied_seats)
