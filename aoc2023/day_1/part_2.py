from aoc2023.day_1.digit_trie import DigitTrie

DIGIT_TERMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def run() -> None:
    with open("input/input.txt", "r") as f:
        all_lines = f.readlines()

    trie = get_populated_trie(DIGIT_TERMS)
    calibration_values = [get_calibration_value(line, trie) for line in all_lines]
    print(f"Sum of all calibration values is: '{sum(calibration_values)}'.")


def get_calibration_value(line: str, trie: DigitTrie) -> int:
    """
    Return an integer containing a calibration value for the input line.

    :param line: A string containing the input text.
    :param trie: A trie storing the available vocabulary.
    """
    digits = extract_digits(line, trie)
    if len(digits) == 0:
        raise Exception(f"No digit is present in '{line}'.")
    return int(digits[0] + digits[-1])


def extract_digits(line: str, trie: DigitTrie) -> [str]:
    result = []
    for i in range(0, len(line)):
        if digit := _extract_digit(line[i:], trie):
            result.append(digit)
    return result


def _extract_digit(text: str, trie: DigitTrie) -> str | None:
    first_letter, *_ = text
    if first_letter.isdigit():
        return first_letter
    elif digit := trie.query(text):
        return digit
    return None


def get_populated_trie(terms: [str]) -> DigitTrie:
    trie = DigitTrie()
    for t in terms:
        trie.insert(t)
    return trie


if __name__ == "__main__":
    run()
