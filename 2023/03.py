import string


VALID_SYMBOLS = (string.punctuation).replace(".", "")


def has_symbol_diagonally_or_vertically_adjacent(line: str, start_index_number: int, end_index_number: int) -> bool:
    possible_symbol_index = []
    if start_index_number == 0:
        possible_symbol_index = list(range(start_index_number, end_index_number + 1))
    elif end_index_number == len(line) - 1:
        possible_symbol_index = list(range(start_index_number - 1, end_index_number + 1))
    else:
        possible_symbol_index = list(range(start_index_number - 1, end_index_number + 1))

    return any([line[index] in VALID_SYMBOLS for index in possible_symbol_index])


def has_symbol_horizontally_adjacent(line: str, start_index_number: int, end_index_number: int) -> bool:
    possible_symbol_index = []
    if start_index_number == 0:
        possible_symbol_index = [end_index_number]
    elif end_index_number == len(line) - 1:
        possible_symbol_index = [start_index_number]
    else:
        possible_symbol_index = [start_index_number -1 , end_index_number]

    return any([line[index] in VALID_SYMBOLS for index in possible_symbol_index])


def get_sum_of_line(line_above, line_below, line):
    total = 0
    number = ""
    for index, character in enumerate(line):
        final_character_is_numeric = character.isnumeric() and index == len(line) - 1

        if character.isnumeric():
            number += character

        if (not character.isnumeric() and number) or final_character_is_numeric:
            if any(
                [
                line_above and has_symbol_diagonally_or_vertically_adjacent(line_above, index - len(number), index),
                line_below and has_symbol_diagonally_or_vertically_adjacent(line_below, index - len(number), index),
                has_symbol_horizontally_adjacent(line, index - len(number), index)
            ]):
                total += int(number)
            number = ""
    return total


filepath = "../input/03.txt"
with open(filepath) as file:
    lines = [line.strip() for line in file.readlines()]
    total = 0
    for index, line in enumerate(lines):
        line_above = lines[index - 1] if index != 0 else None
        line_below = lines[index + 1] if index < len(lines) - 1 else None

        total += get_sum_of_line(line_above, line_below, line)
