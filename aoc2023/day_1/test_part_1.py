from aoc2023.day_1.part_1 import greeting


def test_greeting_is_sufficient() -> None:
    got = greeting()

    assert got == "Day 1: Yay!"
