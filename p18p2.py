import sys
from collections import deque
from typing import Deque

lines = open("p18b.txt").read().strip().split("\n")


def calculate(elements: Deque) -> int:

    # first resolve all parenthesis
    while "(" in elements:
        parenthesis_stack = deque()
        for i, element in enumerate(elements):
            if element == "(":
                parenthesis_stack.append(i)
            elif element == ")":
                opening_parenthesis_index = parenthesis_stack.pop()
                closing_parenthesis_index = i
                elements_in_parenthesis = elements[
                    opening_parenthesis_index + 1 : closing_parenthesis_index
                ]
                result = calculate(elements_in_parenthesis)
                elements = (
                    elements[:opening_parenthesis_index]
                    + [str(result)]
                    + elements[closing_parenthesis_index + 1 :]
                )
                break

    # then all plus operations
    while "+" in elements:
        for i, element3 in enumerate(
            [elements[i : i + 3] for i in range(len(elements) - 2)]
        ):
            if (
                element3[0].isnumeric()
                and element3[1] == "+"
                and element3[2].isnumeric()
            ):
                result = eval(" ".join(element3))
                elements = elements[:i] + [str(result)] + elements[i + 3 :]
                break

    # then all multiply operations
    while "*" in elements:
        for i, element3 in enumerate(
            [elements[i : i + 3] for i in range(len(elements) - 2)]
        ):
            if (
                element3[0].isnumeric()
                and element3[1] == "*"
                and element3[2].isnumeric()
            ):
                result = eval(" ".join(element3))
                elements = elements[:i] + [str(result)] + elements[i + 3 :]
                break

    # and if only one left, return
    if len(elements) == 1:
        return elements[0]

    print(f"No elements left")
    sys.exit()


s = 0
for line in lines:
    result = int(calculate(line.replace(")", " )").replace("(", "( ").split()))
    print(f">{result}")
    s += result

print(f"sum - {s}")
