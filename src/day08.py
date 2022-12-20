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


def calc_horizontal_and_vertical(values, x, y):
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

    return (horizontal, vertical)


def find_visible_trees(values, x, y):
    (horizontal, vertical) = calc_horizontal_and_vertical(values, x, y)

    results = []
    for arr in horizontal:
        find_visible_trees_in_line(arr, results)
    for arr in vertical:
        find_visible_trees_in_line(arr, results)

    return len(results)


def count_visibility(value, array, invers = False):
    id = value["id"]
    height = value["height"]
    counter = 0

    if invers: 
        array.reverse()
    
    for item in array:
        if not invers and item["id"] > id:
            counter += 1
            if item["height"] >= height:
                break
        elif invers and item["id"] < id:
            counter += 1
            if item["height"] >= height:
                break

    return counter


def count_visibility_range(values, x, y):
    max_view = 0
    max_item = {} # out of curiosity: which item is it?

    (horizontal, vertical) = calc_horizontal_and_vertical(values, x, y)

    for val in values:
        current_view = 1

        h_idx = int(val["id"] / x)
        v_idx = val["id"] % x

        h_arr = horizontal[h_idx][:]
        v_arr = vertical[v_idx][:]

        current_view *= count_visibility(val, h_arr)
        current_view *= count_visibility(val, h_arr, True)
        current_view *= count_visibility(val, v_arr)
        current_view *= count_visibility(val, v_arr, True)
        
        if current_view > max_view:
            max_view = current_view
            max_item = val

    return (max_view, max_item)


def solve_part1(fileInfo):
    (values, x, y) = get_values(fileInfo)
    result = find_visible_trees(values, x, y)

    return result


def solve_part2(fileInfo):
    (values, x, y) = get_values(fileInfo)
    (count, _) = count_visibility_range(values, x, y)

    return count
