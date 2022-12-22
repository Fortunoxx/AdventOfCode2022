import pytest

from src.day09 import solve_part1, solve_part2

day = "09"


@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value=13):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value


@pytest.mark.parametrize("day,filenum,expected_value", [(day, "", 1), (day, ".01", 36)])
def test_part2(day, filenum, expected_value):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample{filenum}.dat"}
    assert solve_part2(testdata) == expected_value
