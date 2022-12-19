def get_values(fileInfo):
    is_instructions = False
    is_first = True
    stacks = []
    instructions = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")

            if is_first:
                for i in range(0, get_stack_counter(line)):
                    stacks.append([])
                is_first = False

            if line == "":
                is_instructions = True
                continue

            if not is_instructions and not "[" in line:
                continue

            if is_instructions:
                instructions.append(parse_instructions(line))

            else:
                parts = split_crates(line)
                for i in range(0, len(stacks)):
                    part = parts[i]
                    if len(part.strip()) > 0:
                        stacks[i].append(part)

        for stack in stacks:
            stack.reverse()
    return (stacks, instructions)


def get_stack_counter(line):
    size = int(len(line) / 4) + 1
    return size


def parse_instructions(line):
    parts = line.split(" ")
    return {"count": int(parts[1]), "src": int(parts[3]), "dest": int(parts[5])}


def split_crates(line, delimiter=" "):
    values = []
    block_size = 3
    idx1 = 0
    idx2 = idx1 + block_size
    while len(line) >= idx2:
        part = line[idx1:idx2]
        if len(part) > 0:
            values.append(part[1:2])

        idx1 = idx2 + len(delimiter)
        idx2 = idx1 + block_size

    return values


def move_crates(stacks, instructions):
    for i in instructions:
        for c in range(i["count"]):
            stacks[i["dest"] - 1].append(stacks[i["src"] - 1].pop())

    return stacks


def move_crates_9001(stacks, instructions):
    for i in instructions:
        temp = []
        for _ in range(i["count"]):
            temp.append(stacks[i["src"] - 1].pop())
        temp.reverse()
        for item in temp:
            stacks[i["dest"] - 1].append(item)

    return stacks


def solve_part1(fileInfo):
    (stacks, instructions) = get_values(fileInfo)
    stacks = move_crates(stacks, instructions)
    result = ""
    for s in stacks:
        result += s.pop()

    return result


def solve_part2(fileInfo):
    (stacks, instructions) = get_values(fileInfo)
    stacks = move_crates_9001(stacks, instructions)
    result = ""
    for s in stacks:
        result += s.pop()

    return result
