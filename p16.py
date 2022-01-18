from itertools import permutations
import numbers
import sys
from typing import List, Tuple, TypeAlias
from itertools import permutations

input_source = "p16b.txt"

Interval: TypeAlias = Tuple[int, int]
Intervals: TypeAlias = List[Interval]
FieldIntervals: TypeAlias = Tuple[str, Intervals]
Ticket: TypeAlias = List[int]
Tickets: TypeAlias = List[Ticket]


def get_values() -> Tuple[FieldIntervals, Ticket, Tickets]:
    field_intervals = []
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
            field_intervals.append(
                (
                    field_name,
                    [
                        (int(i[0]), int(i[1]))
                        for i in [
                            interval.split("-")
                            for interval in field_values.split(" or ")
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
    return field_intervals, your_ticket, nearby_tickets


def get_ticket_not_matching_values(
    ticket_values: Ticket, field_intervals: Intervals, max_not_matching: int = None
) -> List[int]:
    if not max_not_matching:
        max_not_matching = len(ticket_values)
    not_matching = []
    fields_intervals = [f[1] for f in field_intervals]
    for field_value, field_intervals in zip(ticket_values, fields_intervals):
        field_matching = False
        for intv_low, intv_high in field_intervals:
            if intv_low <= field_value <= intv_high:
                field_matching = True
                break
        if not field_matching:
            not_matching.append(field_value)
            if len(not_matching) >= max_not_matching:
                break
    return not_matching


def get_unmatching_values(ticket: Ticket, field_intervals: FieldIntervals) -> List[int]:
    not_matching_values = ticket
    for ticket_values in permutations(ticket):
        these_not_matching_values = get_ticket_not_matching_values(
            ticket_values, field_intervals, max_not_matching=len(not_matching_values)
        )
        if len(these_not_matching_values) < len(not_matching_values):
            not_matching_values = these_not_matching_values
            if not not_matching_values:
                # empty, no need to check further
                return []
    return not_matching_values


field_intervals, ticket, nearby_tickets = get_values()
not_matching = []
for nearby_ticket in nearby_tickets:
    unmatching_values = get_unmatching_values(nearby_ticket, field_intervals)
    if unmatching_values:
        not_matching.append(unmatching_values)

result = sum(sum(m) for m in not_matching)
print(result)
