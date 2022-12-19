def get_values(fileInfo):
    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            break  # we expect only 1 line

        return line


def get_index_of_first_different_packet(line, packet_length=4):
    idx = 0
    while idx + packet_length < len(line):
        temp = line[idx : idx + packet_length]
        s = set(temp)
        if len(s) == packet_length:
            break
        idx += 1

    return idx + packet_length


def solve_part1(fileInfo):
    line = get_values(fileInfo)
    return get_index_of_first_different_packet(line)


def solve_part2(fileInfo):
    line = get_values(fileInfo)
    return get_index_of_first_different_packet(line, 14)
