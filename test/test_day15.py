import pytest

from src.day15 import solve_part1, solve_part2

day = "15"


@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value=26):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata, 10) == expected_value


@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value=0):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata) == expected_value
