from typing import Dict
from itertools import product


rules = {}
messages = []

for line in open("p19b.txt").read().strip().split("\n"):
    if ":" in line:
        # rule_sequence
        index, rule_sequence = [p.strip() for p in line.split(":")]
        rule_unions = rule_sequence.split("|")
        rule_parts = []
        for rule in rule_unions:
            rule_parts.append(
                [rule_sequence_part.strip('"') for rule_sequence_part in rule.split()]
            )
        rules[index] = rule_parts
        continue

    if line:
        messages.append(line)

cache = dict()


def pattern_generator(rules: Dict, rule_index: str = None):
    rule_index = rule_index or "0"

    global cache
    if rule_index in cache:
        return cache[rule_index]

    results = set()
    for rule_sequence in rules[rule_index]:
        result = set()
        for rule in rule_sequence:
            if rule.isnumeric():
                patterns = pattern_generator(rules, rule)
                # append patterns to the current results for this sequence
                # or use them if there are no sequences yet
                if result:
                    result = set(
                        result_part + pattern
                        for result_part, pattern in product(result, patterns)
                    )
                    continue

                # result is empty, just use the patterns
                for pattern in patterns:
                    result.add(pattern)
                continue

            # rule is a string
            if result:
                result = {result_part + rule for result_part in result}
                continue

            # result is empty, just use the patterns
            result.add(rule)

        results |= result
    cache[rule_index] = results
    return results


patterns = pattern_generator(rules)
matches = sum([int(m in patterns) for m in messages])
print(matches)
