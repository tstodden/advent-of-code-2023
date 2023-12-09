from aoc2023.day_1.digit_trie import DigitTrie

_DIGIT_TERMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def extract_digits(line: str) -> [str]:
    result = []
    trie = _get_prefilled_digit_trie(_DIGIT_TERMS)
    for i in range(0, len(line)):
        if digit := _extract_digit(trie, line[i:]):
            result.append(digit)
    return result


def _extract_digit(trie: DigitTrie, text: str) -> str | None:
    first_letter, *_ = text
    if first_letter.isdigit():
        return first_letter
    elif digit := trie.query(text):
        return digit
    return None


def _get_prefilled_digit_trie(terms: [str]) -> DigitTrie:
    trie = DigitTrie()
    for t in terms:
        trie.insert(t)
    return trie
