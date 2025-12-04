import time

start = time.time()

filepath = "input/02.txt"

product_id_ranges = []
with open(filepath) as file:
    product_id_ranges = file.readline().split(',')

part_1_total = 0
part_2_total = 0
for product_id_range in product_id_ranges:
    lower_range, upper_range = product_id_range.split('-') 
    product_ids = list(range(int(lower_range), int(upper_range) + 1))

    for product_id in [str(product_id) for product_id in product_ids if len(str(product_id)) % 2 == 0]:
        seperated_numbers = "".join(number for number in product_id)
        all_number_occurences_are_even = all(seperated_numbers.count(number) % 2 == 0 for number in set(seperated_numbers))
        if not all_number_occurences_are_even:
            continue
        
        is_invalid_id = len({product_id[:int(len(product_id) / 2)], product_id[int(len(product_id) / 2):]}) == 1

        if not is_invalid_id:
            continue

        part_1_total += int(product_id)
    
    for product_id in [str(product_id) for product_id in product_ids]:
        number_pieces_sequences = []

        for piece_lenght in [piece_lenght for piece_lenght in range(1, len(product_id)) if len(product_id) % piece_lenght == 0]:

            sequences = []
            for index in range(int(len(product_id) / piece_lenght)):
                number_part = product_id[index * piece_lenght: (index * piece_lenght) + piece_lenght]
                sequences.append(number_part)
            number_pieces_sequences.append(sequences)

        is_invalid_id = any([len(set(sequence)) == 1 for sequence in number_pieces_sequences])

        if not is_invalid_id:
            continue
    
        part_2_total += int(product_id)

    
print(part_1_total)
print(part_2_total)

end = time.time()
print(f"{end - start:.2f} seconden")