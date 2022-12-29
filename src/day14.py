def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            tmp = []
            line = line.replace("\n", "")
            parts = line.split(" -> ")
            for part in parts:
                coordinates = list(map(lambda x: int(x), part.split(",")))
                tmp.append((coordinates[0], coordinates[1]))
            values.append(tmp)
    return values


def calc_line(start, end):
    add = ()
    line = []

    if start[0] < end[0]:
        add = (1, 0)
    elif start[0] > end[0]:
        add = (-1, 0)
    elif start[1] < end[1]:
        add = (0, 1)
    else:
        add = (0, -1)

    current = (start[0], start[1])
    while not current == end:
        line.append(current)
        current = tuple(map(lambda x, y: x + y, current, add))
    line.append(current)
    return line


def calc_blocks(coordinates):
    blocks = []
    for idx in range(len(coordinates)):
        if idx == len(coordinates) - 1:
            break
        start = coordinates[idx]
        end = coordinates[idx + 1]

        for block in calc_line(start, end):
            blocks.append(block)
    return blocks


def let_sand_flow(blocks, sand, max_y, is_part_2=False, start=(500, 0)):
    down = (0, 1)
    left = (-1, 1)
    right = (1, 1)
    current = (start[0], start[1])

    while True:
        pos = tuple(map(lambda x, y: x + y, current, down))
        if pos[1] > max_y and not is_part_2:
            current = None
            break  # all sand falls into void from here
        elif pos[1] >= (max_y + 2) and is_part_2:
            break
        if pos in blocks or pos in sand:
            pos = tuple(map(lambda x, y: x + y, current, left))
            if pos in blocks or pos in sand:
                pos = tuple(map(lambda x, y: x + y, current, right))
                if pos in blocks or pos in sand:
                    break
        current = pos

    if current in blocks or current in sand:
        return None
    return current


def apply_sand_set(blocks, max_y, is_part_2=False):
    sand_set = set([])

    while True:
        new_block = let_sand_flow(blocks, sand_set, max_y, is_part_2)
        if new_block is not None:
            sand_set.add(new_block)
        else:
            break

    # visualize_blocks(blocks, sand_set)
    return sand_set


def visualize_blocks(blocks, sand):
    min_x = -1
    max_x = -1
    max_y = -1

    for b in blocks:
        if b[0] < min_x or min_x == -1:
            min_x = b[0]
        if b[0] > max_x:
            max_x = b[0]
        if b[1] > max_y:
            max_y = b[1]
    for b in sand:
        if b[0] < min_x or min_x == -1:
            min_x = b[0]
        if b[0] > max_x:
            max_x = b[0]
        if b[1] > max_y:
            max_y = b[1]
    
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x - min_x + 1):
            if (x + min_x, y) in blocks:
                line += "#"
            elif (x + min_x, y) in sand:
                line += "o"
            else:
                line += "."
        print(line)


def get_blocks(values):
    blocks = []

    for value in values:
        block = calc_blocks(value)
        for b in block:
            if not b in blocks:
                blocks.append(b)
    return blocks


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    blocks = get_blocks(values)
    max_y = max(blocks, key=lambda tup: tup[1])[1]
    result = apply_sand_set(set(blocks), max_y)

    return len(result)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    blocks = get_blocks(values)
    max_y = max(blocks, key=lambda tup: tup[1])[1]
    result = apply_sand_set(set(blocks), max_y, True)

    return len(result)
