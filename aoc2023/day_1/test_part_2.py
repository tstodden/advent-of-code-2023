import pytest
from aoc2023.day_1.part_2 import extract_digits


@pytest.mark.parametrize(
    "line,expected",
    [
        ("two1nine", [2, 1, 9]),
        ("eightwothree", [8, 2, 3]),
        ("abcone2threexyz", [1, 2, 3]),
    ],
)
def test_extracting_digits(line, expected):
    got = extract_digits(line)

    assert got == expected
