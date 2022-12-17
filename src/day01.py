def get_values(fileInfo):
    sum = 0
    sums = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if line == "":
                sums.append(sum)
                sum = 0
            else:
                sum += int(line)
        sums.append(sum)
    return sums


def solve_part1(fileInfo):
    sums = get_values(fileInfo)
    return max(sums)


def solve_part2(fileInfo):
    sums = get_values(fileInfo)
    sums.sort()
    sums.reverse()

    sum_top_3 = 0
    for i in range(0, 3):
        sum_top_3 += sums[i]
    return sum_top_3
