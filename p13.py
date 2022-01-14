puzzle_part = 2

if puzzle_part == 1:
    lines = open("p13b.txt").read().strip().split("\n")
    time = int(lines[0])
    busses = [int(b) for b in [bus.strip() for bus in lines[1].split(",")] if b != "x"]

    waiting_time = None
    bus = None
    for this_bus in busses:
        this_waiting_time = this_bus - (time % this_bus)
        if not waiting_time or waiting_time > this_waiting_time:
            waiting_time = this_waiting_time
            bus = this_bus

    print(bus * waiting_time)

if puzzle_part == 2:
    lines = open("p13b.txt").read().strip().split("\n")
    busses = [
        None if b == "x" else int(b)
        for b in [bus.strip() for bus in lines[1].split(",")]
    ]

    busses_d = {busses[i]: i for i in range(len(busses)) if busses[i]}
    increment = max(busses_d)
    n = increment - busses_d[increment]
    del busses_d[increment]
    zipper = busses_d.items()
    while True:
        for bus, index in zipper:
            if (n + index) % bus != 0:
                break
        if (n + index) % bus == 0:
            break

        n += increment

    print(n)

    for i, b in enumerate(busses):
        if not b:
            print(f"Bus X arrives at {n + i}")
            continue

        print(f"Bus {b} arrives at {n + i}, divided = {(n+i) // b}, rest = {(n+i) % b}")
