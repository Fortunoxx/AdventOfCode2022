# import day24
# import day23
# import day22
# import day21
# import day20
# import day19
# import day18
# import day17
# import day16
# import day15
# import day14
# import day13
# import day12
import day11
import day10
import day09
import day08
import day07
import day06
import day05
import day04
import day03
import day02
import day01
import sys
sys.path.append('src/puzzle')
import puzzle

def getFileInfo(day, key="input"):
    return {"key": key, "file": f"src/data/day{day}.input.dat"}
    # return {"key": key, "file": f"test/data/day{day}.sample.dat"}

# use beautiful colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
T  = '\033[36m' # turquoise

# download all puzzles
for i in range(24):
    day = str(i+1)
    if len(day) == 1:
        day = "0" + day
    print(f"{W}Day {day}: fetching puzzle data...")
    (fileName, skipped) = puzzle.FetchForDay(day)
    print(f"{W}Day {day}: {G}fetching complete: {fileName} (Skipped: {O}{skipped}{G})")

print(f"{P}")
print(f"--- Solving puzzles now ---")
print(f"{G}")

print(f"{W}Day {O}01{W}: Part {O}1: {G}{day01.solve_part1(getFileInfo('01'))}")
print(f"{W}Day {O}01{W}: Part {O}2: {G}{day01.solve_part2(getFileInfo('01'))}")
print(f"{W}Day {O}02{W}: Part {O}1: {G}{day02.solve_part1(getFileInfo('02'))}")
print(f"{W}Day {O}02{W}: Part {O}2: {G}{day02.solve_part2(getFileInfo('02'))}")
print(f"{W}Day {O}03{W}: Part {O}1: {G}{day03.solve_part1(getFileInfo('03'))}")
print(f"{W}Day {O}03{W}: Part {O}2: {G}{day03.solve_part2(getFileInfo('03'))}")
print(f"{W}Day {O}04{W}: Part {O}1: {G}{day04.solve_part1(getFileInfo('04'))}")
print(f"{W}Day {O}04{W}: Part {O}2: {G}{day04.solve_part2(getFileInfo('04'))}")
print(f"{W}Day {O}05{W}: Part {O}1: {G}{day05.solve_part1(getFileInfo('05'))}")
print(f"{W}Day {O}05{W}: Part {O}2: {G}{day05.solve_part2(getFileInfo('05'))}")
print(f"{W}Day {O}06{W}: Part {O}1: {G}{day06.solve_part1(getFileInfo('06'))}")
print(f"{W}Day {O}06{W}: Part {O}2: {G}{day06.solve_part2(getFileInfo('06'))}")
print(f"{W}Day {O}07{W}: Part {O}1: {G}{day07.solve_part1(getFileInfo('07'))}")
print(f"{W}Day {O}07{W}: Part {O}2: {G}{day07.solve_part2(getFileInfo('07'))}")
print(f"{W}Day {O}08{W}: Part {O}1: {G}{day08.solve_part1(getFileInfo('08'))}")
print(f"{W}Day {O}08{W}: Part {O}2: {G}{day08.solve_part2(getFileInfo('08'))}")
print(f"{W}Day {O}09{W}: Part {O}1: {G}{day09.solve_part1(getFileInfo('09'))}")
print(f"{W}Day {O}09{W}: Part {O}2: {G}{day09.solve_part2(getFileInfo('09'))}")
print(f"{W}Day {O}10{W}: Part {O}1: {G}{day10.solve_part1(getFileInfo('10'))}")
print(f"{W}Day {O}10{W}: Part {O}2: {G}{day10.solve_part2(getFileInfo('10'))}")
print(f"{W}Day {O}11{W}: Part {O}1: {G}{day11.solve_part1(getFileInfo('11'))}")
print(f"{W}Day {O}11{W}: Part {O}2: {G}{day11.solve_part2(getFileInfo('11'))}")
# print(f"{W}Day {O}12{W}: Part {O}1: {G}{day12.solve_part1(getFileInfo('12'))}")
# print(f"{W}Day {O}12{W}: Part {O}2: {G}{day12.solve_part2(getFileInfo('12'))}")
# print(f"{W}Day {O}13{W}: Part {O}1: {G}{day13.solve_part1(getFileInfo('13'))}")
# print(f"{W}Day {O}13{W}: Part {O}2: {G}{day13.solve_part2(getFileInfo('13'))}")
# print(f"{W}Day {O}14{W}: Part {O}1: {G}{day14.solve_part1(getFileInfo('14'))}")
# print(f"{W}Day {O}14{W}: Part {O}2: {G}{day14.solve_part2(getFileInfo('14'))}")
# print(f"{W}Day {O}15{W}: Part {O}1: {G}{day15.solve_part1(getFileInfo('15'))}")
# print(f"{W}Day {O}15{W}: Part {O}2: {G}{day15.solve_part2(getFileInfo('15'))}")
# print(f"{W}Day {O}16{W}: Part {O}1: {G}{day16.solve_part1(getFileInfo('16'))}")
# print(f"{W}Day {O}16{W}: Part {O}2: {G}{day16.solve_part2(getFileInfo('16'))}")
# print(f"{W}Day {O}17{W}: Part {O}1: {G}{day17.solve_part1(getFileInfo('17'))}")
# print(f"{W}Day {O}17{W}: Part {O}2: {G}{day17.solve_part2(getFileInfo('17'))}")
# print(f"{W}Day {O}18{W}: Part {O}1: {G}{day18.solve_part1(getFileInfo('18'))}")
# print(f"{W}Day {O}18{W}: Part {O}2: {G}{day18.solve_part2(getFileInfo('18'))}")
# print(f"{W}Day {O}19{W}: Part {O}1: {G}{day19.solve_part1(getFileInfo('19'))}")
# print(f"{W}Day {O}19{W}: Part {O}2: {G}{day19.solve_part2(getFileInfo('19'))}")
# print(f"{W}Day {O}20{W}: Part {O}1: {G}{day20.solve_part1(getFileInfo('20'))}")
# print(f"{W}Day {O}20{W}: Part {O}2: {G}{day20.solve_part2(getFileInfo('20'))}")
# print(f"{W}Day {O}21{W}: Part {O}1: {G}{day21.solve_part1(getFileInfo('21'))}")
# print(f"{W}Day {O}21{W}: Part {O}2: {G}{day21.solve_part2(getFileInfo('21'))}")
# print(f"{W}Day {O}22{W}: Part {O}1: {G}{day22.solve_part1(getFileInfo('22'))}")
# print(f"{W}Day {O}22{W}: Part {O}2: {G}{day22.solve_part2(getFileInfo('22'))}")
# print(f"{W}Day {O}23{W}: Part {O}1: {G}{day23.solve_part1(getFileInfo('23'))}")
# print(f"{W}Day {O}23{W}: Part {O}2: {G}{day23.solve_part2(getFileInfo('23'))}")
# print(f"{W}Day {O}24{W}: Part {O}1: {G}{day24.solve_part1(getFileInfo('24'))}")
# print(f"{W}Day {O}24{W}: Part {O}2: {G}{day24.solve_part2(getFileInfo('24'))}")
