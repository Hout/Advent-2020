puzzle_part = 2

if puzzle_part == 1:
    highest_id = None
    for line in open("p5b.txt").read().strip().split("\n"):
        row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        id = row * 8 + column

        if not highest_id or highest_id < id:
            highest_id = id

    print(highest_id)

if puzzle_part == 2:
    ids = set()
    for line in open("p5b.txt").read().strip().split("\n"):
        row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        id = row * 8 + column
        if row > 0 and row < 127:
            ids.add(id)

    for id in range(min(ids), max(ids)):
        if id not in ids and id - 1 in ids and id + 1 in ids:
            print(id)
