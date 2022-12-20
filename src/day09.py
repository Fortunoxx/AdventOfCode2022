def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            values.append({"direction": parts[0], "count": int(parts[1])})
    return values


def calc_pos(pos_h, pos_t, max_distance = 1):
    # calc distance
    distX = abs(pos_h["x"] - pos_t["x"])
    distY = abs(pos_h["y"] - pos_t["y"])

    # if too far away: 
    if distY > max_distance:
        pos_t["x"] = pos_h["x"]
        if pos_h["y"] > pos_t["y"]:
            pos_t["y"] = pos_h["y"] - 1
        else:
            pos_t["y"] = pos_h["y"] + 1

    if distX > max_distance:
        pos_t["y"] = pos_h["y"]
        if pos_h["x"] > pos_t["x"]:
            pos_t["x"] = pos_h["x"] - 1
        else:
            pos_t["x"] = pos_h["x"] + 1

    return pos_t


def move_one(direction, pos_h, pos_t, visited):
    if direction == "R":
        pos_h["x"] += 1
    elif direction == "L":
        pos_h["x"] -= 1
    elif direction == "U":
        pos_h["y"] += 1
    elif direction == "D":
        pos_h["y"] -= 1

    pos_t = calc_pos(pos_h, pos_t)
    pos = (pos_t["x"], pos_t["y"])
    if not pos in visited:
        visited.append(pos)


def solve_part1(fileInfo):
    directions = get_values(fileInfo)
    pos_h = {"x": 0, "y": 0}
    pos_t = {"x": 0, "y": 0}
    visited = []

    for d in directions:
        for _ in range(d["count"]):
            move_one(d["direction"], pos_h, pos_t, visited)

    return len(visited)


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
