import numpy as np

puzzle_part = 2

data = [
    (line[0], int(line[1:])) for line in open("p12b.txt").read().strip().split("\n")
]


def direction_turn(direction, degrees):
    degrees %= 360
    dir = list(direction)
    for _ in range(0, degrees, 90):
        if np.array_equal(dir, [-1, 0]):
            dir = [0, 1]
        elif np.array_equal(dir, [0, 1]):
            dir = [1, 0]
        elif np.array_equal(dir, [1, 0]):
            dir = [0, -1]
        elif np.array_equal(dir, [0, -1]):
            dir = [-1, 0]
        else:
            assert False

    return np.array(dir)


def manhattan_distance(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])


if puzzle_part == 1:
    position = np.array([0, 0])
    direction = np.array([1, 0])

    for command, argument in data:
        if command == "F":
            position = position + (direction * argument)
        elif command == "N":
            wp_position = wp_position + [0, argument]
        elif command == "S":
            position = position - [0, argument]
        elif command == "W":
            position = position - [argument, 0]
        elif command == "E":
            position = position + [argument, 0]
        elif command == "R":
            direction = direction_turn(direction, argument)
        elif command == "L":
            direction = direction_turn(direction, -argument)
        else:
            assert False
    print(manhattan_distance([0, 0], position))


def around_boat_turn(wp_position, degrees):
    x, y = wp_position
    degrees %= 360
    for _ in range(0, degrees, 90):
        x, y = y, -x

    return np.array([x, y])


# little test
assert np.array_equal(around_boat_turn(np.array([1, 2]), 90), [2, -1])
assert np.array_equal(around_boat_turn([1, 2], 180), [-1, -2])
assert np.array_equal(around_boat_turn([1, 2], -90), [-2, 1])
assert np.array_equal(around_boat_turn([1, 2], 360), [1, 2])

if puzzle_part == 2:
    boat_position = np.array([0, 0])
    wp_position = np.array([10, 1])
    for command, argument in data:
        if command == "F":
            boat_position += wp_position * argument
        elif command == "N":
            wp_position = wp_position + [0, argument]
        elif command == "S":
            wp_position = wp_position - [0, argument]
        elif command == "W":
            wp_position = wp_position - [argument, 0]
        elif command == "E":
            wp_position = wp_position + [argument, 0]
        elif command == "R":
            wp_position = around_boat_turn(wp_position, argument)
        elif command == "L":
            wp_position = around_boat_turn(wp_position, -argument)
        else:
            assert False
    print(manhattan_distance([0, 0], boat_position))
