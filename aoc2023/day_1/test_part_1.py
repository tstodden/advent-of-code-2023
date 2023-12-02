from aoc2023.day_1.part_1 import get_calibration_value


def test_getting_a_calibration_value_for_two_digits() -> None:
    line = "ab1cde2f"

    got = get_calibration_value(line)

    assert got == 12


def test_getting_a_calibration_value_for_one_digit() -> None:
    line = "ab1cdef"

    got = get_calibration_value(line)

    assert got == 11
