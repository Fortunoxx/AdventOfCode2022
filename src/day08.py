def get_values(fileInfo):
    horizontal_values = []
    vertical_values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            temp = []
            for char in line:
                temp.append(int(char))
            horizontal_values.append(temp)

    is_first = True
    for arr in horizontal_values:
        idx = 0
        for a in arr:
            if is_first:
                vertical_values.append([a])
            else:
                vertical_values[idx].append(a)
            idx += 1

        if is_first:
            is_first = False

    return (horizontal_values, vertical_values)


def iterate(values):
    counter = 0
    current_max = 0
    idx = 0
    for val in values:
        if current_max > 0 and idx < (len(values)-1):
            if val > current_max:
                counter += 1
                current_max = val
        else:
            current_max = val
        idx += 1

    # previous = []

    # for val in values:
    #     visible = True
    #     if len(previous) > 0 and len(previous) < (max_length - 1):
    #         for p in previous:
    #             if p >= val:
    #                 visible = False
    #         if visible:
    #             counter += 1
    #     previous.append(val)

    return counter # 1832 too high


def find_visible_trees_in_line(values):
    counter = iterate(values)
    values.reverse()
    counter += iterate(values)

    return counter


def find_visible_trees(horizontal_values, vertical_values):
    counter = 0
    for i in range(len(horizontal_values)):
        arr = horizontal_values[i]
        if i == 0 or i == (len(horizontal_values) - 1):  # add all outmost from horizontal
            counter += len(arr)
        else:
            counter += find_visible_trees_in_line(arr)

    for i in range(len(vertical_values)):
        arr = vertical_values[i]
        if i == 0 or i == (len(vertical_values) - 1):  # add all outmost from vertical
            counter += (
                len(arr) - 2
            )  # remove edge cases that were already part of horizontal
        else:
            counter += find_visible_trees_in_line(arr)

    return counter


def solve_part1(fileInfo):
    (horizontal_values, vertical_values) = get_values(fileInfo)
    result = find_visible_trees(horizontal_values, vertical_values)

    return result


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
