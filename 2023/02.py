import re

MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14
MAX_RED_CUBES = 12


def get_number_of_cubes(text: str, color: str) -> int:
    needle = f"([\d]*) (?={color})"
    pattern = re.compile(needle)
    match = pattern.search(text)
    
    if match:
        return int(match.group())
    
    return 0


def get_draws(text: str) -> list[str]:
    draws = text[text.index(":") + 1:].split(";")
    return draws


def game_is_possible(green_cubes: int, blue_cubes: int, red_cubes: int) -> bool:
    if green_cubes > MAX_GREEN_CUBES:
        return False
    
    if blue_cubes > MAX_BLUE_CUBES:
        return False

    if red_cubes > MAX_RED_CUBES:
        return False

    return True

filepath = "../input/02.txt"
with open(filepath) as file:
    total = 0
    power = 0
    for index, line in enumerate(file.readlines(), 1):
        game = line.strip()
        draws = get_draws(game)
        
        highest_green_cubes = max([get_number_of_cubes(draw, "green") for draw in draws])
        highest_blue_cubes = max([get_number_of_cubes(draw, "blue") for draw in draws])
        highest_red_cubes = max([get_number_of_cubes(draw, "red") for draw in draws])

        if game_is_possible(highest_green_cubes, highest_blue_cubes, highest_red_cubes):
            total += index

        power += highest_green_cubes * highest_blue_cubes * highest_red_cubes