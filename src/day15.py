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
            return True
    return False


def calc_valid(sensors, beacons, meta, y):
    (x1, x2, _, _) = meta
    valid = 0
    for x in range(x1, x2):
        if (x, y) not in beacons and is_valid(sensors, x, y):
            valid += 1
    return valid


def check_distress_beacon_position(x, y, sensors, beacons):
    if (x, y) not in beacons and not is_valid(sensors, x, y):
        return True
    return False


def check_range(x, y, max_x, max_y):
    if x > max_x:
        return False
    elif x < 0:
        return False
    elif y > max_y:
        return False
    elif y < 0:
        return False
    return True


# there is only one possible spot where the beacon can hide, namely on d+1
def find_distress_beacon(max_x, max_y, sensors, beacons):
    d1 = (1, 1)
    d2 = (-1, 1)
    d3 = (-1, -1)
    d4 = (1, -1)

    for (sx, sy, d) in sensors:
        current = (sx, sy - d - 1)  # 12 o'clock over senson
        # move down right
        while current[1] <= sy:
            if not check_range(current[0], current[1], max_x, max_y):
                current = tuple(map(lambda x, y: x + y, current, d1))
                continue
            elif check_distress_beacon_position(current[0], current[1], sensors, beacons):
                return current
            current = tuple(map(lambda x, y: x + y, current, d1))
        # move down left
        while current[0] >= sx:
            if not check_range(current[0], current[1], max_x, max_y):
                current = tuple(map(lambda x, y: x + y, current, d2))
                continue
            elif check_distress_beacon_position(current[0], current[1], sensors, beacons):
                return current
            current = tuple(map(lambda x, y: x + y, current, d2))
        # move up left
        while current[1] >= sy:
            if not check_range(current[0], current[1], max_x, max_y):
                current = tuple(map(lambda x, y: x + y, current, d3))
                continue
            elif check_distress_beacon_position(current[0], current[1], sensors, beacons):
                return current
            current = tuple(map(lambda x, y: x + y, current, d3))
        # move up right
        while current[0] <= sx:
            if not check_range(current[0], current[1], max_x, max_y):
                current = tuple(map(lambda x, y: x + y, current, d4))
                continue
            elif check_distress_beacon_position(current[0], current[1], sensors, beacons):
                return current
            current = tuple(map(lambda x, y: x + y, current, d4))


def solve_part1(fileInfo, y=int(2e6)):
    (sensors, beacons, meta) = get_values(fileInfo)
    return calc_valid(sensors, beacons, meta, y)


def solve_part2(fileInfo, max_x=int(4e6), max_y=int(4e6)):
    (sensors, beacons, _) = get_values(fileInfo)
    (x, y) = find_distress_beacon(max_x, max_y, sensors, beacons)
    result = x * int(4e6) + y

    return result
