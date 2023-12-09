from aoc2023.day_1.digit_trie import DigitTrie

_DIGIT_TERMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def run() -> None:
    with open("input/input.txt", "r") as f:
        all_lines = f.readlines()

    calibration_values = [get_calibration_value(line) for line in all_lines]
    print(f"Sum of all calibration values is: '{sum(calibration_values)}'.")


def get_calibration_value(line: str) -> int:
    """
    Return an integer containing a calibration value for the input line.

    :param line: A string containing the input text.
    """
    digits = extract_digits(line)
    if len(digits) == 0:
        raise Exception(f"No digit is present in '{line}'.")
    return int(digits[0] + digits[-1])


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


if __name__ == "__main__":
    run()
