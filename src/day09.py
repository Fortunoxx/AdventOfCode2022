def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            values.append({"direction": parts[0], "count": int(parts[1])})
    return values


def calc_pos(pos_h, pos_t, max_distance=1):
    # calc distance
    distX = abs(pos_h["x"] - pos_t["x"])
    distY = abs(pos_h["y"] - pos_t["y"])

    pos = {"x": pos_t["x"], "y": pos_t["y"]}

    fac_x = 1 if pos_h["x"] > pos_t["x"] else -1
    fac_y = 1 if pos_h["y"] > pos_t["y"] else -1

    if distY > max_distance or distY + distX > 2:
        pos["y"] = pos["y"] + (1 * fac_y)

    if distX > max_distance or distY + distX > 2:
        pos["x"] = pos["x"] + (1 * fac_x)

    return pos


def move_one(direction, pos_h, pos_t, visited, has_tail=False, move_part_two_only=False):
    if not move_part_two_only:
        if direction == "R":
            pos_h = {"x": pos_h["x"] + 1, "y": pos_h["y"]}
        elif direction == "L":
            pos_h = {"x": pos_h["x"] - 1, "y": pos_h["y"]}
        elif direction == "U":
            pos_h = {"x": pos_h["x"], "y": pos_h["y"] + 1}
        elif direction == "D":
            pos_h = {"x": pos_h["x"], "y": pos_h["y"] - 1}

    new_pos = calc_pos(pos_h, pos_t)
    pos = (new_pos["x"], new_pos["y"])
    if not pos in visited and has_tail:
        visited.append(pos)
    return (pos_h, new_pos)


def solve_part1(fileInfo):
    directions = get_values(fileInfo)

    positions = [{"x": 0, "y": 0}] * 2
    visited = []

    for d in directions:
        for _ in range(d["count"]):
            for idx in range(len(positions)):
                if idx < len(positions) - 1:
                    (positions[idx], positions[idx + 1]) = move_one(d["direction"],
                                                                    positions[idx], positions[idx + 1], visited, True)

    return len(visited)


def solve_part2(fileInfo):
    directions = get_values(fileInfo)

    positions = [{"x": 0, "y": 0}] * 10
    visited = []

    for d in directions:
        for _ in range(d["count"]):
            for idx in range(len(positions)):
                has_tail = False
                move_part_two_only = False
                if idx < len(positions) - 1:
                    if idx == len(positions) - 2:
                        has_tail = True
                    if idx > 0:
                        move_part_two_only = True

                    (positions[idx], positions[idx + 1]) = move_one(d["direction"],
                                                                    positions[idx], positions[idx + 1], visited, has_tail, move_part_two_only)

    return len(visited)  # 2555 too low
