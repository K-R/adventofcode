from copy import deepcopy

with open("input/06.txt") as file:
    map_grid = []
    for line in file.readlines():
        map_grid.append([character for character in line.strip()])


def get_current_position(map_data):
    for row_position, row in enumerate(map_data):
        for character_position, character in enumerate(row):
            if character in('<', '^', '>', 'v'):
                return character_position, row_position


def get_number_of_distinct_positions(map_data, obstruction_x_coordinate = None, obstruction_y_coordinate = None):    
    if (obstruction_x_coordinate or obstruction_x_coordinate == 0) and (obstruction_y_coordinate or obstruction_y_coordinate == 0):
        map_data[obstruction_y_coordinate][obstruction_x_coordinate] = '#'

    x, y = get_current_position(map_data)

    direction = map_data[y][x]
    guard_path = []
    number_of_steps = 0

    map_width = len(map_data[0])
    map_height = len(map_data)

    while True:
        guard_path.append((x,y))
        number_of_steps += 1

        if number_of_steps == (map_width * map_height):
            break

        is_possible_up = (y - 1) >= 0
        is_possible_down = (y + 1) <= map_height - 1
        is_possible_right = (x + 1) <= map_width - 1
        is_possible_left = (x - 1) >= 0

        if not all([is_possible_up, is_possible_right, is_possible_down, is_possible_left]):
            break

        if direction == '^' and is_possible_up:
            new_y = y - 1
            if map_data[new_y][x] == '#':
                direction = '>'
                continue
            y = new_y

        if direction == 'v' and is_possible_down:
            new_y = y + 1
            if map_data[new_y][x] == '#':
                direction = '<'
                continue
            y = new_y

        if direction == '>' and is_possible_right:
            new_x = x + 1
            if map_data[y][new_x] == '#':
                direction = 'v'
                continue
            x = new_x

        if direction == '<' and is_possible_left:
            new_x = x - 1
            if map_data[y][new_x] == '#':
                direction = '^'
                continue
            x = new_x

    total_distinct_positions = len(set(guard_path))
    is_stuck_in_loop = number_of_steps == (map_width * map_height)
    return total_distinct_positions, is_stuck_in_loop

total_distinct_positions, is_stuck_in_loop = get_number_of_distinct_positions(map_grid)

total_obstruction_placement_options = 0
for row_number, row in enumerate(map_grid):
    for column_number, character in enumerate(row):
        if map_grid[row_number][column_number] != '.':
            continue

        data = deepcopy(map_grid)
        total_distinct_positions, is_stuck_in_loop = get_number_of_distinct_positions(data, column_number, row_number)
        if is_stuck_in_loop:
            total_obstruction_placement_options += 1

print(total_distinct_positions)
print(total_obstruction_placement_options)