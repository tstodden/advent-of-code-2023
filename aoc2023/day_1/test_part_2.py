import pytest
from aoc2023.day_1.part_2 import (
    get_calibration_value,
    get_populated_trie,
    extract_digits,
    DIGIT_TERMS,
)


@pytest.mark.parametrize(
    "line,expected",
    [
        ("two1nine", ["2", "1", "9"]),
        ("eightwothree", ["8", "2", "3"]),
        ("abcone2threexyz", ["1", "2", "3"]),
    ],
)
def test_extracting_digits(line, expected):
    trie = get_populated_trie(DIGIT_TERMS)

    got = extract_digits(line, trie)

    assert got == expected


def test_getting_a_calibration_value_for_two_digits() -> None:
    trie = get_populated_trie(DIGIT_TERMS)
    line = "abconedef2"

    got = get_calibration_value(line, trie)

    assert got == 12


def test_getting_a_calibration_value_for_one_digit() -> None:
    trie = get_populated_trie(DIGIT_TERMS)
    line = "abconedef"

    got = get_calibration_value(line, trie)

    assert got == 11


def test_raising_an_exception_when_no_digits_exist() -> None:
    trie = get_populated_trie(DIGIT_TERMS)
    line = "abcdef"

    with pytest.raises(Exception, match="No digit is present in 'abcdef'."):
        get_calibration_value(line, trie)
