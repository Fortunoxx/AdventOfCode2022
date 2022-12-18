def get_values(fileInfo, is_part_2=False):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if line != "\n":
                mid = int(len(line) / 2)
                part1 = line[:mid]
                part2 = line[mid:]
                for ele1 in part1:
                    # for ele2 in part2:
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


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    converted = convert_values(values)
    result = sum(converted)

    return result


def solve_part2(fileInfo):
    return 0
