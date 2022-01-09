from collections import Counter
import numpy as np
import numpy.typing as npt
from itertools import product

data = np.array([list(line) for line in open("p11b.txt").read().strip().split("\n")])

puzzle_part = 2


def print_seats(data):
    for row in data:
        print()
        for seat in row:
            print(seat, end="")
    print()


def get_occupied_seats(data: npt.ArrayLike, r: int, c: int, max_distance=None) -> int:
    occupied = 0
    for direction in [
        np.array(d) for d in product([-1, 0, 1], repeat=2) if d != (0, 0)
    ]:
        cr, cc = (r, c) + direction
        while (
            0 <= cr < np.shape(data)[0]
            and 0 <= cc < np.shape(data)[1]
            and (
                max_distance is None
                or (abs(cr - r) <= max_distance and abs(cc - c) <= max_distance)
            )
        ):
            if data[cr, cc] == "L":
                break
            if data[cr, cc] == "#":
                occupied += 1
                break
            # field is "."
            cr, cc = (cr, cc) + direction

    return occupied


def cycle(
    data: npt.ArrayLike, required_occupied_seats: int, max_distance: int = None
) -> None:
    old_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
    new_data = data.copy()
    print_seats(data)
    while not np.array_equal(old_data, new_data):
        old_data = new_data
        new_data = np.empty(shape=[len(data), len(data[0])], dtype=np.dtype("U1"))
        for r, row in enumerate(old_data):
            for c, seat in enumerate(row):
                if seat == ".":
                    new_data[r, c] = seat
                    continue

                occupied_seats = get_occupied_seats(old_data, r, c, max_distance)
                if seat == "L" and occupied_seats == 0:
                    new_data[r, c] = "#"
                elif seat == "#" and occupied_seats >= required_occupied_seats:
                    new_data[r, c] = "L"
                else:
                    new_data[r, c] = seat

        print_seats(new_data)

    unique, counts = np.unique(
        new_data,
        return_counts=True,
    )
    counter = Counter(dict(zip(unique, counts)))
    occupied_seats = counter["#"]
    print(occupied_seats)


if puzzle_part == 1:
    cycle(data, required_occupied_seats=4, max_distance=1)

if puzzle_part == 2:
    cycle(data, required_occupied_seats=5)
