import copy


def get_values(fileInfo):
    values = {}
    start = ()
    end = ()
    y = 0
    positions = []

    with open(fileInfo["file"]) as file:
        for line in file:
            x = 0
            line = line.replace("\n", "")
            for c in line:
                dist = -1
                if c == "S":
                    start = (x, y)
                    c = "a"
                elif c == "E":
                    end = (x, y)
                    c = "z"

                if c == "a":
                    positions.append((x, y))  # for part 2

                val = ord(c) - 96 if ord(c) > 96 else 0

                values[(x, y)] = {"height": val, "dist": dist}
                x += 1
            y += 1

    return (values, start, end, positions)


def dijkstra(start, end, unvisited, step=1, max_height=1):
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)
    directions = [up, down, left, right]

    current = unvisited[start]
    current["dist"] = 0
    key = start
    while len(unvisited) > 0:
        for dir in directions:
            pos = tuple(map(lambda x, y: x + y, key, dir))
            if pos in unvisited and unvisited[pos]["height"] <= (current["height"] + max_height):
                unvisited[pos]["dist"] = current["dist"] + step
                if pos == end:
                    return unvisited[pos]["dist"]
        del unvisited[key]

        min_item = -1
        for idx in unvisited:
            if unvisited[idx]["dist"] > 0 and (unvisited[idx]["dist"] < min_item or min_item == -1):
                (current, min_item, key) = (
                    unvisited[idx], unvisited[idx]["dist"], idx)
        if min_item == -1:
            break  # no solution for this start position

    return -1


def solve_part1(fileInfo):
    (values, start, end, _) = get_values(fileInfo)
    steps = dijkstra(start, end, values)
    return steps


def solve_part2(fileInfo):
    (values, _, end, positions) = get_values(fileInfo)

    best_position = ()
    min_steps = -1

    for start in positions:
        steps = dijkstra(start, end, copy.deepcopy(values))
        if steps > 0 and (steps < min_steps or min_steps == -1):
            min_steps = steps
            best_position = start

    return min_steps
