import pytest
from aoc2023.day_1.digit_trie import DigitTrie, DigitTrieNode


def test_inserting_a_valid_digit():
    sut = DigitTrie()

    sut.insert("one")

    want = DigitTrie()

    want._root_node.children = {
        "o": DigitTrieNode(
            char="o",
            children={
                "n": DigitTrieNode(
                    char="n",
                    children={"e": DigitTrieNode(char="e", digit=1, is_end=True)},
                )
            },
        )
    }
    assert sut == want


def test_inserting_an_invalid_digit():
    sut = DigitTrie()

    with pytest.raises(Exception, match="Invalid digit: 'invalid'."):
        sut.insert("invalid")
