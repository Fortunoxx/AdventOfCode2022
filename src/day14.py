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


def let_sand_flow(blocks, sand, max_y, start=(500, 0)):
    down = (0, 1)
    left = (-1, 1)
    right = (1, 1)
    current = (start[0], start[1])

    while True:
        pos = tuple(map(lambda x, y: x + y, current, down))
        if pos[1] > max_y:
            current = None
            break # all sand falls into void from here
        if pos in blocks or pos in sand:
            pos = tuple(map(lambda x, y: x + y, current, left))
            if pos in blocks or pos in sand:
                pos = tuple(map(lambda x, y: x + y, current, right))
                if pos in blocks or pos in sand:
                    break
        current = pos

    return current


def apply_sand(blocks):
    sand = []
    max_y = max(blocks, key=lambda tup: tup[1])[1]

    while True:
        new_block = let_sand_flow(blocks, sand, max_y)
        if new_block is not None:
            sand.append(new_block)
            # visualize_blocks(blocks, sand)
        else: 
            break

    return sand


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


def solve_part1(fileInfo, visualize=False): # activate to see beautiful diagram
    values = get_values(fileInfo)
    blocks = []

    for value in values:
        block = calc_blocks(value)
        for b in block:
            if not b in blocks:
                blocks.append(b)

    if visualize:
        visualize_blocks(blocks, [])
    
    result = apply_sand(blocks)
    
    if visualize:
        visualize_blocks(blocks, result)
   
    return len(result)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    return 0
