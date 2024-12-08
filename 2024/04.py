with open("input/04.txt") as file:
    data = []
    for line in file.readlines():   
        data += [line.strip()]

    grid_width = len(data[0])
    grid_height = len(data)

search_word = 'XMAS'
first_letter = search_word[0]
search_word_lenght = len(search_word)
word_range = range(search_word_lenght)

possible_words = []

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
            possible_words.append(word)

        if is_possible_vertical_down:
            word = ''.join([data[y + index][x] for index in word_range])
            possible_words.append(word)
        
        if is_possible_horizontal_forward:
            word = ''.join([data[y][x + index] for index in word_range])
            possible_words.append(word)
        
        if is_possible_horizontal_backward:
            word = ''.join([data[y][x - index] for index in word_range])
            possible_words.append(word)

        if is_possible_diagonal_right_up:
            word = ''.join([data[y - index][x + index] for index in word_range])
            possible_words.append(word)


        if is_possible_diagonal_left_up:
            word = ''.join([data[y - index][x - index] for index in word_range])
            possible_words.append(word)

        if is_possible_diagonal_right_down:
            word = ''.join([data[y + index][x + index] for index in word_range])
            possible_words.append(word)

        if is_possible_diagonal_left_down:
            word = ''.join([data[y + index][x - index] for index in word_range])
            possible_words.append(word)


total = possible_words.count(search_word)