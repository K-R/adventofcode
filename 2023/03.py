import string

test = [
    ".......855.442......190..................................969..........520.......59.............................................172..........",
    ".......................-....@...21...........971........................*..............965.......577=..........316..465*169.................", 
    "........881.......881....635......*..........*.............%.577.....864.......873.........................742...*...............714..244...",
    ".......*..../..................602......351...423....939.906...*.........899..-..........833..60..%....965...*....309......43......*.*......",
    "....737......294..........321*.......................$.......337....511.*.........58..............305.*.......153.............130.....638...",
    ".........296.......715.794..759...............590.................410.......233.............*.....#.....................477..342....729*....",
    ".....989*...........................568..571.....*.488..98.......*........................123.577.............988...........*....$......285.",
    "...............667.857*127............*....*..343..*............506...702..........295.................*......*.........600.....626.*.......",
    ".......*563......*........................349.....945.................+......@........*....964%......33.642...431.......*............968....",
    "....229..........48....=....*.....447......................%....745$..........569...787.........*.....................887...................",
    ".......................369...515..............100...........174..............................633.973........................................",
    ".....@........776...*..........*.....877.....87....*.997*..........*..................285........775.845.........962.....651........509..321",
    "82...................184.....418..........54*....35.........782%..201...........=734..*......$...................*........../...866.....*..."
]

test2 = [
    "467..114..", 
    "...*......",
    "..35..633.",
    "......#...", 
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664$.598.$",
]

VALID_SYMBOLS = (string.punctuation).replace(".", "")

def has_symbol_diagonally_or_vertically_adjacent(line: str, start_index_number: int, end_index_number: int) -> bool:
    possible_symbol_index = []
    if start_index_number == 0:
        possible_symbol_index = list(range(start_index_number, end_index_number + 2))
    elif end_index_number == len(line) -1:
        possible_symbol_index = list(range(start_index_number - 1, end_index_number))
    else:
        possible_symbol_index = list(range(start_index_number - 1, end_index_number + 2))

    # print(f'{possible_symbol_index}')

    return any([line[index] in VALID_SYMBOLS for index in possible_symbol_index])


def has_symbol_horizontally_adjacent(line: str, start_index_number: int, end_index_number: int) -> bool:
    possible_symbol_index = []
    if start_index_number == 0:
        possible_symbol_index = [end_index_number + 1]
    elif end_index_number == len(line) -1:
        possible_symbol_index = [start_index_number - 1]
    else:
        possible_symbol_index = [end_index_number + 1, start_index_number -1]

    # print(f'{possible_symbol_index}')

    return any([line[index] in VALID_SYMBOLS for index in possible_symbol_index])


def get_sum_of_line(line_above, line_below, line):
    total = 0
    number = ""
    test_numbers = []
    for index, character in enumerate(line):
        final_character_is_numeric = character.isnumeric() and index == len(line) - 1

        if character.isnumeric():
            number += character
                
        if (not character.isnumeric() and number) or final_character_is_numeric:
            if any(
                [
                line_above and has_symbol_diagonally_or_vertically_adjacent(line_above, index - len(number), index -1),
                line_below and has_symbol_diagonally_or_vertically_adjacent(line_below, index - len(number), index -1),
                has_symbol_horizontally_adjacent(line, index - len(number), index -1)
            ]):
                total += int(number)
                test_numbers.append(int(number))
            number = ""
    
    if '294..483' in line:

        if line_above:
            print(f'line above: {line_above}')
        print(f'            {line} - sum of line is {total}={sum(test_numbers)} with numbers: {test_numbers}')
        if line_below:
            print(f'line below: {line_below}')
        print('')
        print('')
        print('')
        print('')

    return total


filepath = "../input/03.txt"
with open(filepath) as file:
    lines = [line.strip() for line in file.readlines()]
    # lines = test2

    total = 0
    for index, line in enumerate(lines):
        line_above = lines[index - 1] if index != 0 else None
        line_below = lines[index + 1] if index < len(lines) - 1 else None

        total += get_sum_of_line(line_above, line_below, line)

print(total)
# 531213 not the answer
