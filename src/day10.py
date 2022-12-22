def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            arg = (parts[0], int(parts[1])) if len(parts) > 1 else (parts[0], None)
            
            values.append(arg)
    return values


def get_signal_values(command, current, default_cycle_length = 3):
    val = []
    (cmd, num) = command

    if cmd == "noop":
        val.append(current)
    elif cmd == "addx":
        for i in range(default_cycle_length):
            current = current + num if i == default_cycle_length - 1 else current
            val.append(current)

    return (val, current)


def get_signal_strength(commands, offset = 20, cycle = 40):
    values = []
    current = 1
    results = []

    for cmd in commands:
        (val, current) = get_signal_values(cmd, current)
        values += val

    for idx in range(len(values)):
        if idx % cycle == offset:
            results.append(idx * values[idx])

    return results


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    results = get_signal_strength(values)

    return sum(results)


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
