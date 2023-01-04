import ast


def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        temp = []
        for line in file:
            line = line.replace("\n", "")
            if not line:
                continue
            arr = ast.literal_eval(line)
            temp.append(arr)

            if len(temp) == 2:
                values.append(temp)
                temp = []
    return values


def is_valid(left, right):
    valid = True

    for idx in range(len(left)):
        is_array = False
        tmp_left = left[idx]
        tmp_right = []

        if idx >= len(right):
            valid = False
            break
        else:
            tmp_right = right[idx]

        if isinstance(tmp_left, list) and not isinstance(tmp_right, list):
            tmp_right = [tmp_right]
            is_array = True
        elif not isinstance(tmp_left, list) and isinstance(tmp_right, list):
            tmp_left = [tmp_left]
            is_array = True
        elif isinstance(tmp_left, list) and isinstance(tmp_right, list):
            is_array = True
        elif isinstance(tmp_left, int) and isinstance(tmp_right, int):
            if tmp_left < tmp_right:
                break
            elif tmp_left > tmp_right:
                valid = False
                break
        elif idx >= len(tmp_right) and len(tmp_left) > len(tmp_right):
            break
        elif idx == len(tmp_left) - 1 and len(tmp_left) < len(tmp_right):
            valid = False
            break

        if is_array and not is_valid(tmp_left, tmp_right):
            valid = False
            break
    return valid


def find_correct_order(values):
    indexes = []
    for idx in range(len(values)):
        if is_valid(values[idx][0], values[idx][1]):
            indexes.append(idx + 1)
            # indexes.append((idx, is_valid(values[idx][0], values[idx][1])))
    return indexes


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    results = find_correct_order(values)
    return sum(results)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    return 0
