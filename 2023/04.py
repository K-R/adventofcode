def get_number_list(numbers: str) -> set[int]:
    return {int(number) for number in numbers.split(' ') if number.isnumeric()}


def calculate_card_points(numbers: set) -> int:
    if len(numbers) == 1:
        return 1

    factor = len(numbers) -1

    return 2 ** factor


filepath = "input/04.txt"
with open(filepath) as file:
    total = 0
    cards: dict[int, int] = {}
    for card_number, line in enumerate(file.readlines(), start=1):
        if not card_number in cards:
            cards[card_number] =  1

        card = line[line.index(':'):].strip()
        
        card_numbers = card.split(' | ')

        own_numbers = get_number_list(card_numbers[0])
        all_winning_numbers = get_number_list(card_numbers[1])

        own_winning_numbers = own_numbers.intersection(all_winning_numbers)
        if own_winning_numbers:
            score = calculate_card_points(own_winning_numbers)
            total += score

            for index in range(1, len(own_winning_numbers) + 1):
                won_card_number = card_number + index
                number_of_won_cards = cards[card_number]
                if won_card_number not in cards:
                    cards[won_card_number] = number_of_won_cards + 1
                else:
                    cards[won_card_number] += number_of_won_cards
