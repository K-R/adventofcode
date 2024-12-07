valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_string_digit_positions(text: str) -> dict[int, str]:
    string_digit_positions = {}
    for string_digit in valid_digits:
        start_position = 0
        string_digit_index = text.find(string_digit, start_position)
        while string_digit_index != -1:
            string_digit_positions[string_digit_index + len(string_digit) -1] = valid_digits[string_digit]
            start_position += len(string_digit)
            string_digit_index = text.find(string_digit, start_position)

    return string_digit_positions


def get_digit_positions(text: str) -> dict[int, str]:
    return {index: character for index, character in enumerate(text) if character.isnumeric()}


def get_calibration_value(text: str) -> int | None:
    string_digit_positions = get_string_digit_positions(text)
    digit_positions = get_digit_positions(text)

    positions = string_digit_positions | digit_positions
    first_number = positions[min(positions)]
    last_number = positions[max(positions)]

    calibration_value = int(first_number + last_number)
    return calibration_value


filepath = "input/01.txt"

with open(filepath) as file:
    total = 0
    for line in file.readlines():
        text = line.strip()
        calibration_value = get_calibration_value(text)
        if calibration_value:
            total += calibration_value
