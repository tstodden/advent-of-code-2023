from __future__ import annotations
from dataclasses import dataclass, field

_TERM_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


@dataclass
class DigitTrieNode:
    char: str

    children: dict[str, DigitTrieNode] = field(default_factory=dict)

    digit: int = 0

    is_end: bool = False


class DigitTrie:
    _root_node: DigitTrieNode

    def __init__(self) -> None:
        self._root_node = DigitTrieNode(char="")

    def insert(self, word: str) -> None:
        if word not in _TERM_MAP:
            raise Exception(f"Invalid digit: '{word}'.")
        self._insert(_TERM_MAP[word], word, self._root_node)

    def query(self, text: str) -> int | None:
        return None

    def _insert(self, digit: int, word: str, node: DigitTrieNode):
        if len(word) == 0:
            node.digit = digit
            node.is_end = True
            return

        first_letter, *rest = word
        if first_letter not in node.children:
            node.children[first_letter] = DigitTrieNode(char=first_letter)

        self._insert(digit, rest, node.children[first_letter])

    def __eq__(self, other) -> bool:
        if not isinstance(other, DigitTrie):
            return False

        return self._root_node == other._root_node

    def __repr__(self) -> str:
        return f"DigitTrie<_root_node: {self._root_node}>"
