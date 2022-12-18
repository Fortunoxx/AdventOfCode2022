import pytest

from src.day02 import solve_part1, solve_part2

day = "02"

@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value = 15): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value = 12): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata) == expected_value