from itertools import permutations
import sys
from typing import List, Tuple, TypeAlias, Iterable
from itertools import permutations
from math import prod
from collections import defaultdict

input_source = "p16b.txt"

Range: TypeAlias = Iterable
Ranges: TypeAlias = List[Range]
Fields: TypeAlias = Tuple[str, Ranges]
Ticket: TypeAlias = List[int]
Tickets: TypeAlias = List[Ticket]


def get_values() -> Tuple[Fields, Ticket, Tickets]:
    fields = []
    your_ticket = []
    nearby_tickets = []
    mode = 0

    for line in open(input_source).read().strip().split("\n"):
        if line == "":
            continue

        if line == "your ticket:":
            mode = 1
            continue

        if line == "nearby tickets:":
            mode = 2
            continue

        if mode == 0:
            # fields
            field_name, field_values = line.split(":")
            fields.append(
                (
                    field_name,
                    [
                        range(int(i[0]), int(i[1]) + 1)
                        for i in [
                            range.split("-") for range in field_values.split(" or ")
                        ]
                    ],
                )
            )
            continue

        if mode == 1:
            # ticket_values
            your_ticket = [int(i) for i in line.split(",")]
            continue

        if mode == 2:
            # nearby ticket
            nearby_tickets.append([int(i) for i in line.split(",")])
            continue

        print("Bad value for mode")
        sys.exit()
    return fields, your_ticket, nearby_tickets


def get_unmatching_values(ticket: Ticket, fields: Fields) -> List[int]:
    value_matches = {}
    for ticket_field_value in ticket:
        value_matches[ticket_field_value] = []
        for field_name, field_ranges in fields:
            if any(ticket_field_value in field_range for field_range in field_ranges):
                value_matches[ticket_field_value].append(field_name)

    return [k for k, v in value_matches.items() if not v]


fields, ticket, nearby_tickets = get_values()

# part 1
not_matching = [
    values
    for values in [
        get_unmatching_values(nearby_ticket, fields) for nearby_ticket in nearby_tickets
    ]
    if values
]
result = sum(sum(m) for m in not_matching)
print(result)

# part 2
valid_tickets = [t for t in nearby_tickets if not get_unmatching_values(t, fields)]

# transpose
columns = [[ticket[i] for ticket in valid_tickets] for i in range(len(ticket))]

# find fields per column
matching_columns = defaultdict(set)
for column_index, column in enumerate(columns):
    for field_name, field_ranges in fields:
        if all(
            [
                any([column_value in field_range for field_range in field_ranges])
                for column_value in column
            ]
        ):
            matching_columns[column_index].add(field_name)


# find one solution
solution = {}
while sum(len(v) for v in matching_columns.values()) > 0:
    # check for a lonely field in the matching columns
    loner_index = [k for k, v in matching_columns.items() if len(v) == 1][0]
    loner_field_name = list(matching_columns[loner_index])[0]
    solution[loner_index] = loner_field_name

    # remove field from all matching_columns to find further loners
    for field_set in matching_columns.values():
        field_set.discard(loner_field_name)

print(
    prod([tv for ti, tv in enumerate(ticket) if solution[ti].startswith("departure")])
)
