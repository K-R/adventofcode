is_part_one = True

with open("input/04.txt") as file:
    data = []
    for line in file.readlines():   
        data += [line.strip()]

    grid_width = len(data[0])
    grid_height = len(data)

search_word = 'XMAS' if is_part_one else 'SAM'
first_letter = search_word[0]
search_word_lenght = len(search_word)
word_range = range(search_word_lenght)

number_of_matches = 0
number_of_x_patterns = 0
indexes_of_middle_character = []

for y, row in enumerate(data):
    for x, character in enumerate(row):
        if character != first_letter:
            continue
        
        is_possible_vertical_up = (y - (search_word_lenght - 1)) >= 0
        is_possible_vertical_down = (y + search_word_lenght) <= grid_height
        
        is_possible_horizontal_forward = (x + search_word_lenght) <= grid_width
        is_possible_horizontal_backward = (x - (search_word_lenght - 1)) >= 0

        is_possible_diagonal_right_up = is_possible_vertical_up and is_possible_horizontal_forward
        is_possible_diagonal_left_up = is_possible_vertical_up and is_possible_horizontal_backward
        is_possible_diagonal_right_down = is_possible_vertical_down and is_possible_horizontal_forward
        is_possible_diagonal_left_down = is_possible_vertical_down and is_possible_horizontal_backward

        if is_possible_vertical_up:
            word = ''.join([data[y - index][x] for index in word_range])
            if word == search_word:
                number_of_matches += 1
        if is_possible_vertical_down:
            word = ''.join([data[y + index][x] for index in word_range])
            if word == search_word:
                number_of_matches += 1        
        if is_possible_horizontal_forward:
            word = ''.join([data[y][x + index] for index in word_range])
            if word == search_word:
                number_of_matches += 1        
        if is_possible_horizontal_backward:
            word = ''.join([data[y][x - index] for index in word_range])
            if word == search_word:
                number_of_matches += 1
        if is_possible_diagonal_right_up:
            word = ''.join([data[y - index][x + index] for index in word_range])

            if word == search_word:
                number_of_matches += 1

                middle_character_index = (y - 1, x + 1)
                if middle_character_index not in indexes_of_middle_character:
                    indexes_of_middle_character.append(middle_character_index)
                else:
                    number_of_x_patterns += 1


        if is_possible_diagonal_left_up:
            word = ''.join([data[y - index][x - index] for index in word_range])
            if word == search_word:
                number_of_matches += 1
            
                middle_character_index = (y - 1, x - 1)
                if middle_character_index not in indexes_of_middle_character:
                    indexes_of_middle_character.append(middle_character_index)
                else:
                    number_of_x_patterns += 1


        if is_possible_diagonal_right_down:
            word = ''.join([data[y + index][x + index] for index in word_range])
            if word == search_word:
                number_of_matches += 1
            
                middle_character_index = (y + 1, x + 1)
                if middle_character_index not in indexes_of_middle_character:
                    indexes_of_middle_character.append(middle_character_index)
                else:
                    number_of_x_patterns += 1


        if is_possible_diagonal_left_down:
            word = ''.join([data[y + index][x - index] for index in word_range])
            if word == search_word:
                number_of_matches += 1
            
                middle_character_index = (y + 1, x - 1)
                if middle_character_index not in indexes_of_middle_character:
                    indexes_of_middle_character.append(middle_character_index)
                else:
                    number_of_x_patterns += 1
