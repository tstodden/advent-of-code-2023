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
    for char in line:
        if char.isdigit():
            result.append(char)
    return result


if __name__ == "__main__":
    run()
