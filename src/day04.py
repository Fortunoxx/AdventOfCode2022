def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            splitted = line.split(",")
            part1 = splitted[0].split("-")
            part2 = splitted[1].split("-")
            range1 = {"lower": int(part1[0]), "upper": int(part1[1])}
            range2 = {"lower": int(part2[0]), "upper": int(part2[1])}
            values.append({"A": range1, "B": range2})
    return values


def count_overlapping(values):
    overlapping = 0
    for entry in values:
        if (
            entry["A"]["lower"] <= entry["B"]["lower"]
            and entry["A"]["upper"] >= entry["B"]["upper"]
        ):
            overlapping += 1
        elif (
            entry["B"]["lower"] <= entry["A"]["lower"]
            and entry["B"]["upper"] >= entry["A"]["upper"]
        ):
            overlapping += 1

    return overlapping


def count_overlapping_partly(values):
    overlapping = 0
    for entry in values:
        if (entry["A"]["lower"] <= entry["B"]["lower"] and entry["A"]["upper"] >= entry["B"]["lower"]):
            overlapping += 1
        elif (entry["B"]["lower"] <= entry["A"]["lower"] and entry["B"]["upper"] >= entry["A"]["lower"]        ):
            overlapping += 1

    return overlapping


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    result = count_overlapping(values)

    return result


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    result = count_overlapping_partly(values)

    return result
