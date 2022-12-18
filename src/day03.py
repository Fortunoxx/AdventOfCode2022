def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            mid = int(len(line) / 2)
            part1 = line[:mid]
            part2 = line[mid:]
            for ele1 in part1:
                if ele1 in part2:
                    values.append(ele1)
                    break

    return values


def convert_values(values):
    ret = []
    for val in values:
        key = ord(val)
        if key > 96:
            key -= 96
        elif key > 64:
            key -= 38
        ret.append(key)

    return ret


def get_groups(fileInfo, groupCount = 3):
    counter = 0
    groups = []
    group = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            group.append(line)
            counter += 1
            if counter >= groupCount: 
                groups.append(group)
                group = []
                counter = 0

    return groups

def get_same_character_in_all_entries(groups):
    first = groups[0]

    for char in first:
        if char in groups[1] and char in groups[2]:
            return char


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    converted = convert_values(values)
    result = sum(converted)

    return result


def solve_part2(fileInfo):
    groups = get_groups(fileInfo)
    values = []

    for group in groups:
        char = get_same_character_in_all_entries(group)
        values.append(char)

    converted = convert_values(values)
    result = sum(converted)

    return result
