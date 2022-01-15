from collections import defaultdict
import re
from itertools import product

puzzle_part = 2

if puzzle_part == 1:

    mem = defaultdict(int)
    mask_0 = 2 ^ 37 - 1
    mask_1 = 0

    for line in open("p14b.txt").read().strip().split("\n"):
        mask_match = re.match(r"mask = ([X10]+)", line)
        if mask_match:
            mask = mask_match.group(1)
            mask_1 = int("".join(["1" if c == "1" else "0" for c in mask]), 2)
            mask_0 = int("".join(["0" if c == "0" else "1" for c in mask]), 2)
            continue

        mem_match = re.match(r"mem\[(\d+)\] = (\d+)", line)
        if mem_match:
            address = int(mem_match.group(1))
            value = int(mem_match.group(2))

            value |= mask_1
            value &= mask_0
            mem[address] = value
            continue

        assert False, "No mask or mem input"

    print(sum(mem.values()))

if puzzle_part == 2:

    mem = defaultdict(int)
    mask = ""

    for line in open("p14b.txt").read().strip().split("\n"):
        mask_match = re.match(r"mask = ([X10]+)", line)
        if mask_match:
            mask = mask_match.group(1)
            continue

        mem_match = re.match(r"mem\[(\d+)\] = (\d+)", line)
        if mem_match:
            address = int(mem_match.group(1))
            value = int(mem_match.group(2))

            address_str = bin(address)[2:].rjust(len(mask), "0")

            for combination in product("01", repeat=mask.count("X")):
                combination_index = 0
                generated_address_str = ""
                for ch, m in zip(address_str, mask):
                    if m == "0":
                        generated_address_str += ch
                        continue
                    if m == "1":
                        generated_address_str += "1"
                        continue
                    generated_address_str += combination[combination_index]
                    combination_index += 1

                generated_address = int(generated_address_str, 2)
                mem[generated_address] = value

            continue

        assert False, "No mask or mem input"

    print(sum(mem.values()))
