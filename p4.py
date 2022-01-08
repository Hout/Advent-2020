import re

puzzle_part = 2

data = []
for lines in open("p4b.txt").read().strip().split("\n\n"):
    passport = dict()
    for fields in lines.split():
        key, value = fields.split(":")
        passport[key] = value
    data.append(passport)

if puzzle_part == 1:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    for d in data:
        fields = set(d)
        if not required_fields - fields:
            valid += 1
    print(valid)


def int4_min_max(value, min_value, max_value):
    if not re.fullmatch(r"\d{4}", value):
        return False
    return min_value <= int(value) <= max_value


if puzzle_part == 2:
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    present_valid = 0
    for d in data:
        fields = set(d)
        if required_fields - fields:
            continue

        if not int4_min_max(d["byr"], 1920, 2002):
            continue

        if not int4_min_max(d["iyr"], 2010, 2020):
            continue

        if not int4_min_max(d["eyr"], 2020, 2030):
            continue

        m = re.fullmatch(r"(\d+)(cm|in)", d["hgt"])
        if not m:
            continue
        number, measure = m.groups()
        if measure == "cm":
            if not 150 <= int(number) <= 193:
                continue
        elif measure == "in":
            if not 59 <= int(number) <= 76:
                continue
        else:
            continue

        if not re.fullmatch(r"#[a-f0-9]{6}", d["hcl"]):
            continue

        if not re.fullmatch(r"(amb|blu|brn|gry|grn|hzl|oth)", d["ecl"]):
            continue

        if not re.fullmatch(r"\d{9}", d["pid"]):
            continue

        present_valid += 1
    print(present_valid)
