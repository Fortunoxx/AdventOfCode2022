def get_values(fileInfo):
    beacons = set()
    sensors = set()

    with open(fileInfo["file"]) as file:
        min_x = 0
        min_y = 0
        max_x = 0
        max_y = 0

        for line in file:
            parts = line.split()
            sx, sy = parts[2], parts[3]
            bx, by = parts[8], parts[9]
            sx = int(sx[2:-1])
            sy = int(sy[2:-1])
            bx = int(bx[2:-1])
            by = int(by[2:])
            taxi = abs(sx - bx) + abs(sy - by)

            sensors.add((sx, sy, taxi))
            beacons.add((bx, by))

            if sx - taxi < min_x:
                min_x = sx - taxi
            if sy - taxi < min_y:
                min_y = sy - taxi
            if sx + taxi > max_x:
                max_x = sx + taxi
            if sy + taxi > max_y:
                max_y = sy + taxi

    return (sensors, beacons, (min_x, max_x, min_y, max_y))


def is_valid(sensors, x, y):
    for (sx, sy, d) in sensors:
        if abs(x - sx) + abs(y - sy) <= d:
            return False
    return True


def calc_valid(sensors, beacons, meta, y):
    (x1, x2, _, _) = meta
    valid = 0
    for x in range(x1, x2):
        if (x, y) not in beacons and not is_valid(sensors, x, y):
            valid += 1
    return valid


def solve_part1(fileInfo, y=20000):
    (sensors, beacons, meta) = get_values(fileInfo)
    return calc_valid(sensors, beacons, meta, y)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    return 0
