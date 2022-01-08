from itertools import combinations

puzzle_part = 2

data = [int(line) for line in open("p9b.txt").read().strip().split("\n")]


def check_number(number, chunk):
    for c1, c2 in combinations(chunk, 2):
        if number == c1 + c2:
            return True
    return False


def check_invalid_number(data, preambule_size):
    for chunk, number in [
        (data[i : i + preambule_size], data[i + preambule_size])
        for i in range(len(data) - preambule_size)
    ]:
        if not check_number(number, chunk):
            return number
    return None


def find_contiguous_adding_up(data, number):
    for i in range(len(data)):
        j = i + 1
        s = sum(data[i:j])
        while j < len(data) and s < number:
            s += data[j]
            j += 1
        if sum(data[i:j]) == number:
            return i, j
    return None


if puzzle_part == 1:
    print(check_invalid_number(data, 25))

if puzzle_part == 2:
    i, j = find_contiguous_adding_up(data, 20874512)
    s = sorted(data[i:j])
    print(s[0] + s[-1])
