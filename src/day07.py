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


def get_directories_by_size(directories, max_size = 100000, result = []):
    for dir in directories["directories"]:
        if dir["size"] <= max_size:
            result.append(dir)
        if len(dir["directories"]) > 0:
            get_directories_by_size(dir, max_size, result)

    return result


def get_directories_by_min_size(directories, min_size, result = []):
    for dir in directories["directories"]:
        if dir["size"] >= min_size:
            result.append(dir)
        if len(dir["directories"]) > 0:
            get_directories_by_min_size(dir, min_size, result)

    return result


def delete_directories_for_update(directories, max_space = 70000000, space_needed = 30000000):
    total_space_used = directories["size"]
    space_left = max_space - total_space_used
    space_to_be_deleted = space_needed - space_left

    results = get_directories_by_min_size(directories, space_to_be_deleted)
    smallest_item = {}
    for item in results:
        if smallest_item == {} or item["size"] < smallest_item["size"]:
            smallest_item = item

    return smallest_item


def solve_part1(fileInfo):
    directory_structure = get_values(fileInfo)
    calc_sizes(directory_structure)
    sum = 0
    for dir in get_directories_by_size(directory_structure):
        sum += dir["size"]

    return sum


def solve_part2(fileInfo):
    directory_structure = get_values(fileInfo)
    calc_sizes(directory_structure)
    result = delete_directories_for_update(directory_structure)["size"]

    return result
