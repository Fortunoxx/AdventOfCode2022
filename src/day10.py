def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(" ")
            arg = (parts[0], int(parts[1])) if len(parts) > 1 else (parts[0], None)
            
            values.append(arg)
    return values


def get_signal_values(command, current, default_cycle_length = 2):
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
    values = [1]
    current = 1
    results = []

    for cmd in commands:
        (val, current) = get_signal_values(cmd, current)
        values += val

    for idx in range(len(values)):
        if (idx + 1) % cycle == offset:
            results.append((idx + 1) * values[idx])

    return results


def calc_sprites(commands, sprite = 3, cycle = 40):
    values = [0]
    current = 0
    lines = []

    for cmd in commands:
        (val, current) = get_signal_values(cmd, current)
        values += val

    line = []
    offset = 0

    for idx in range(len(values)):
        if idx - offset in range(values[idx], values[idx] + sprite):
            line.append("#")
        else:
            line.append(".")

        if (idx + 1) % cycle == 0:
            lines.append(line)
            line = []
            offset += cycle

    return lines


def print_sprites(lines):
    for line in lines:
        for i in range(len(line)):
            print(line[i], end = "")
        print()


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    results = get_signal_strength(values)

    return sum(results)


def solve_part2(fileInfo):
    values = get_values(fileInfo)
    line_values = calc_sprites(values)
    print_sprites(line_values)
    
    result = ""
    for line in line_values:
        for char in line:
            result += char

    return result
