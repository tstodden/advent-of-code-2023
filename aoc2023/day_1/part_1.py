def get_calibration_value(line: str) -> int:
    """
    Return an integer containing a calibration value for the input line.
    :param line: A string containing the input text.
    """
    digits = extract_digits(line)
    return int(digits[0] + digits[-1])


def extract_digits(line: str) -> [str]:
    result = []
    for char in line:
        if char.isdigit():
            result.append(char)
    return result
