from math import prod

puzzle_part = 2

lines = open("p3b.txt").read().strip().split("\n")
data = set()
for line_number, line in enumerate(lines):
    for column_number, c in enumerate(line):
        if c == "#":
            data.add((line_number, column_number))
width = len(lines[0])
height = len(lines)

if puzzle_part == 1:
    trees = 0
    step_increase_lines, step_increase_columns = (1, 3)
    line_number, column_number = (0, 0)
    while True:
        column_number += step_increase_columns
        column_number %= width
        line_number += step_increase_lines
        if line_number >= height:
            break
        if (line_number, column_number) in data:
            trees += 1
    print(trees)


if puzzle_part == 2:

    trees_lst = []
    for step_increase_lines, step_increase_columns in [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]:
        trees = 0
        line_number, column_number = (0, 0)
        while True:
            column_number += step_increase_columns
            column_number %= width
            line_number += step_increase_lines
            if line_number >= height:
                break
            if (line_number, column_number) in data:
                trees += 1
        trees_lst.append(trees)
    print(prod(trees_lst))
