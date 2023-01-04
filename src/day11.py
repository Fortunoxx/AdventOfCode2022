def get_values(fileInfo):
    values = []
    lcm = 1

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if line.startswith("Monkey "):
                monkey = {
                    "id": int(line.split()[1].replace(":", "")),
                    "inspected": 0,
                }
                values.append(monkey)
            elif line.startswith("  Starting items: "):
                items = list(
                    map(
                        lambda x: int(x),
                        line.replace("  Starting items: ", "").split(", "),
                    )
                )
                items.reverse()  # we want to use a stack
                monkey["items"] = items
            elif line.startswith("  Operation: "):
                sanitized = line.replace("  Operation: new = old ", "")
                parts = sanitized.split()
                if sanitized == "* old":
                    monkey["op"] = {"type": "square"}
                else:
                    monkey["op"] = {"type": parts[0], "number": int(parts[1])}
            elif line.startswith("  Test: divisible by "):
                monkey["test"] = {"mod": int(line.split()[-1])}
                lcm *= int(line.split()[-1])
            elif line.startswith("    If true: throw to monkey "):
                monkey["test"]["true"] = int(int(line.split()[-1]))
            elif line.startswith("    If false: throw to monkey "):
                monkey["test"]["false"] = int(int(line.split()[-1]))

    return (values, lcm)


def play(monkeys, rounds=20, part=1, lcm=1):
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                # get items from stack
                worry_level = monkey["items"].pop()
                if monkey["op"]["type"] == "square":
                    worry_level *= worry_level
                elif monkey["op"]["type"] == "+":
                    worry_level += monkey["op"]["number"]
                elif monkey["op"]["type"] == "*":
                    worry_level *= monkey["op"]["number"]

                # divide by div (3 or 1) and round
                if part == 1:
                    worry_level //= 3
                else:
                    worry_level %= lcm

                # check dividability and throw to next monkey
                if worry_level % monkey["test"]["mod"] == 0:
                    monkeys[monkey["test"]["true"]
                            ]["items"].insert(0, worry_level)
                else:
                    monkeys[monkey["test"]["false"]
                            ]["items"].insert(0, worry_level)

                # finally, count inspected items
                monkey["inspected"] += 1

    return monkeys


def get_most_active(monkeys, counter=2):
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey["inspected"])
    inspections.sort()

    result = 1
    for item in inspections[-1 * counter:]:
        result *= item

    return result


def solve_part1(fileInfo):
    (values, _) = get_values(fileInfo)
    monkeys = play(values, 20)
    result = get_most_active(monkeys)

    return result


def solve_part2(fileInfo, rounds=10000):
    (values, lcm) = get_values(fileInfo)
    monkeys = play(values, rounds, 2, lcm)
    result = get_most_active(monkeys)

    return result
