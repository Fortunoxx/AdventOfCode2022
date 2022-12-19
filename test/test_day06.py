import pytest

from src.day06 import solve_part1, solve_part2

day = "06"


@pytest.mark.parametrize("day,filenum,expected_value", [(day,"",7),(day,".01",5),(day,".02",6),(day,".03",10),(day,".04",11)])
def test_part1(day, filenum, expected_value):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample{filenum}.dat"}
    assert solve_part1(testdata) == expected_value


@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value=0):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata) == expected_value
