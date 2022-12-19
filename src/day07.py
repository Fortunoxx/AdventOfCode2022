def get_values(fileInfo):
    current = {"name": "/", "files": [], "directories": [], "parent": None, "size": 0} # this will be the current working directory
    is_first = True
    first = {}

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            current = parse_directory(line, current)
            if is_first:
                is_first = False
                first = current
            
    return first


def parse_directory(line, current):
    if line[0:1] == "$": # we have a command
        if line[2:4] == "cd":
            dir = line[5:]

            if dir == "..":
                current = current["parent"]

            elif not dir == "/" and not dir in current["directories"]:
                new = {"name": dir, "files": [], "directories": [], "parent": current, "size": 0}
                current["directories"].append(new)
                current = new
    else:
        if not line[:3] == "dir":
            parts = line.split(" ")
            current["files"].append({"size": int(parts[0]), "name": parts[1]})

    return current


def calc_sizes(directory_structure):
    sub = 0
    for dir in directory_structure["directories"]:
        sub += calc_sizes(dir)
    for file in directory_structure["files"]:
        sub += file["size"]
    directory_structure["size"] = sub
    return sub


def get_directories_by_size(directories, result = [], max_size = 100000):
    for dir in directories["directories"]:
        if dir["size"] <= max_size:
            result.append(dir)
        if len(dir["directories"]) > 0:
            get_directories_by_size(dir, result)

    return result


def solve_part1(fileInfo):
    directory_structure = get_values(fileInfo)
    calc_sizes(directory_structure)
    sum = 0
    for dir in get_directories_by_size(directory_structure):
        sum += dir["size"]

    return sum


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
