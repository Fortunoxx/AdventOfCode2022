def get_rules():
    # rock
    A = {"X": 3, "Y": 6, "Z": 0}
    # paper
    B = {"X": 0, "Y": 3, "Z": 6}
    #scissors
    C = {"X": 6, "Y": 0, "Z": 3}
    # rules
    rules = {"A": A, "B": B, "C": C}

    return rules


def get_values(fileInfo, is_part_2=False):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "\n":
                splitted = line.split(" ")
                if not is_part_2:
                    values.append({"p1": splitted[0], "p2": splitted[1]})
                else:
                    rules = get_rules()
                    value = rules[splitted[0]]
                    if splitted[1] == "X": # lose
                        values.append({"p1": splitted[0], "p2": get_item(value, 0)})
                    if splitted[1] == "Y": # draw
                        values.append({"p1": splitted[0], "p2": get_item(value, 3)})
                    if splitted[1] == "Z": # win
                        values.append({"p1": splitted[0], "p2": get_item(value, 6)})

    return values


def get_item(src, val):
    for itm in src:
        if src[itm] == val:
            return itm


def get_shape_values():
    values = {"X": 1, "Y": 2, "Z": 3}
    return values


def solve_part1(fileInfo):
    rules = get_rules()
    values = get_values(fileInfo)
    shape_values = get_shape_values()

    sum = 0
    for value in values:
        p1 = rules[value['p1']]
        p2 = p1[value['p2']]
        shape_value = shape_values[value['p2']]
        sum += (p2 + shape_value)

    return sum


def solve_part2(fileInfo):
    rules = get_rules()
    values = get_values(fileInfo, 2)
    shape_values = get_shape_values()

    sum = 0
    for value in values:
        p1 = rules[value['p1']]
        p2 = p1[value['p2']]
        shape_value = shape_values[value['p2']]
        sum += (p2 + shape_value)

    return sum
