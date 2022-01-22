import sys
from collections import deque
from typing import Deque

lines = open("p18b.txt").read().strip().split("\n")


def matching_index(elements: Deque) -> int:
    """Finds the matching parenthesis for the first parenthesis"""
    depth = 0
    for i, element in enumerate(elements):
        if element == "(":
            depth += 1
            continue

        if element == ")":
            depth -= 1
            if depth == 0:
                return i

    print(f"No matching parenthesis in {elements}")
    sys.exit()


def calculate(elements: Deque) -> int:
    while elements:
        if elements[0] == "(":
            close_index = matching_index(elements)
            assert close_index
            elements_in_parenthesis = elements[1:close_index]
            result = calculate(elements_in_parenthesis)
            elements = [result] + elements[close_index + 1 :]
        elif len(elements) >= 2 and elements[2] == "(":
            close_index = matching_index(elements[2:]) + 2
            assert close_index
            elements_in_parenthesis = elements[3:close_index]
            result = calculate(elements_in_parenthesis)
            elements = elements[:2] + [str(result)] + elements[close_index + 1 :]
        elif (
            len(elements) >= 3
            and elements[0].isnumeric()
            and elements[1] in "+*"
            and elements[2].isnumeric()
        ):
            result = eval(" ".join(elements[:3]))
            elements = [str(result)] + elements[3:]
        elif len(elements) == 1:
            return elements[0]

    print(f"No elements left")
    sys.exit()


print(
    sum(
        [
            int(calculate(line.replace(")", " )").replace("(", "( ").split()))
            for line in lines
        ]
    )
)
