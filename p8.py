from collections import Counter

data = [
    (instruction[0], int(instruction[1]))
    for instruction in [
        line.split() for line in open("p8b.txt").read().strip().split("\n")
    ]
]

puzzle_part = 2

if puzzle_part == 1:
    counter = Counter()
    accumulator = 0
    pointer = 0
    while True:
        counter[pointer] += 1
        if counter[pointer] > 1:
            print(
                f"instruction {pointer} executed for the 2nd time, value accumulator is {accumulator}"
            )
            exit()
        command, argument = data[pointer]
        print(pointer, accumulator, command, argument, counter[pointer])
        if command == "nop":
            pointer += 1
            continue
        if command == "acc":
            accumulator += argument
            pointer += 1
            continue
        if command == "jmp":
            pointer += argument
            continue
        print("Illegal instruction")
        exit()


def run_program(data) -> int:
    counter = Counter()
    accumulator = 0
    pointer = 0
    while True:
        if pointer == len(data):
            return accumulator

        assert pointer >= 0
        assert pointer < len(data)

        command, argument = data[pointer]

        counter[pointer] += 1
        if counter[pointer] > 1:
            # looping
            return None

        # print(pointer, accumulator, command, argument, counter[pointer])

        if command == "nop":
            pointer += 1
            continue
        if command == "acc":
            accumulator += argument
            pointer += 1
            continue
        if command == "jmp":
            pointer += argument
            continue
        print("Illegal instruction")
        exit()


if puzzle_part == 2:
    changed = {"nop": "jmp", "jmp": "nop"}
    for i in range(len(data)):
        if data[i][0] in changed:
            try_data = data.copy()
            try_data[i] = (changed[data[i][0]], data[i][1])
            accumulator = run_program(try_data)
            if accumulator:
                print(
                    f"non looping program for change in instruction {i+1}, "
                    f"accumulator is {accumulator}"
                )
                break
