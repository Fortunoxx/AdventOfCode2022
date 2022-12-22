def get_values(fileInfo):
    values = []

    with open(fileInfo["file"]) as file:
        for line in file:
            line = line.replace("\n", "")
            if line.startswith("Monkey "):
                monkey = {"id": int(line.split(" ")[1].removesuffix(":")), "inspected": 0}
                values.append(monkey)
            elif line.startswith("  Starting items: "):
                items = list(map(lambda x: int(x), line.removeprefix("  Starting items: ").split(", ")))
                items.reverse() # we want to use a stack
                monkey["items"] = items
            elif line.startswith("  Operation: "):
                sanitized = line.removeprefix("  Operation: new = old ")
                parts = sanitized.split(" ")
                if sanitized == "* old":
                    monkey["op"] = {"type": "square"}
                else: 
                    monkey["op"] = {"type": parts[0], "number": int(parts[1])}
            elif line.startswith("  Test: divisible by "):
                monkey["test"] = {"mod": int(line.removeprefix("  Test: divisible by "))}
            elif line.startswith("    If true: throw to monkey "):
                monkey["test"]["true"] = int(line.removeprefix("    If true: throw to monkey "))
            elif line.startswith("    If false: throw to monkey "):
                monkey["test"]["false"] = int(line.removeprefix("    If false: throw to monkey "))
            
    return values


def play(monkeys, rounds = 20, div = 3):
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

                # divide by 3 and round
                worry_level = int(worry_level / div)

                # check dividability and throw to next monkey
                if worry_level % monkey["test"]["mod"] == 0:
                    monkeys[monkey["test"]["true"]]["items"].insert(0, worry_level)
                else:
                    monkeys[monkey["test"]["false"]]["items"].insert(0, worry_level)

                # finally, count inspected items
                monkey["inspected"] += 1

    return monkeys


def solve_part1(fileInfo):
    values = get_values(fileInfo)
    monkeys = play(values, 20)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey["inspected"])
    inspections.sort()

    result = 1
    for item in inspections[-2:]:
        result *= item
    return result


def solve_part2(fileInfo):
    values = get_values(fileInfo)

    return 0
