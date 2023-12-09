import pytest
from aoc2023.day_1.part_2 import get_calibration_value, extract_digits


@pytest.mark.parametrize(
    "line,expected",
    [
        ("two1nine", ["2", "1", "9"]),
        ("eightwothree", ["8", "2", "3"]),
        ("abcone2threexyz", ["1", "2", "3"]),
    ],
)
def test_extracting_digits(line, expected):
    got = extract_digits(line)

    assert got == expected


def test_getting_a_calibration_value_for_two_digits() -> None:
    line = "abconedef2"

    got = get_calibration_value(line)

    assert got == 12


def test_getting_a_calibration_value_for_one_digit() -> None:
    line = "abconedef"

    got = get_calibration_value(line)

    assert got == 11


def test_raising_an_exception_when_no_digits_exist() -> None:
    line = "abcdef"

    with pytest.raises(Exception, match="No digit is present in 'abcdef'."):
        get_calibration_value(line)
