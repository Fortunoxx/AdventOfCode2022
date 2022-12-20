def get_values(fileInfo):
    values = []
    y = 0
    x = 0
    id = 0

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            y += 1

            if y == 1:
                x = len(line)

            for char in line:
                values.append({"id": id, "height": int(char)})
                id += 1

    return (values, x, y)


def iterate(values, results):
    current_max = -1

    for val in values:
        if val["height"] > current_max:
            current_max = val["height"]

            if not val["id"] in results:
                results.append(val["id"])


def find_visible_trees_in_line(values, results):
    iterate(values, results)
    values.reverse()
    iterate(values, results)


def find_visible_trees(values, x, y):
    horizontal = []
    vertical = []

    # make horizontal and vertical arrays
    for val in values:
        if val["id"] % x > 0:
            horizontal[int(val["id"] / x)].append(val)
        else:
            new = [val]
            horizontal.append(new)

        if int(val["id"] / x) == 0:
            new = [val]
            vertical.append(new)
        else:
            vertical[val["id"] % x].append(val)

    results = []
    for arr in horizontal:
        find_visible_trees_in_line(arr, results)
    for arr in vertical:
        find_visible_trees_in_line(arr, results)

    return len(results)


def solve_part1(fileInfo):
    (values, x, y) = get_values(fileInfo)
    result = find_visible_trees(values, x, y)

    return result


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
