def get_numbers_from_text(text, seperator) -> list[int]:
    result = []
    for number_part in text.strip().split(seperator):
        number = int(number_part)
        result.append(number)
    return result


with open("input/05.txt") as file:
    page_ordering_rules = []
    updates = []
    for line in file.readlines():
        if '|' in line:
            numbers = get_numbers_from_text(line, '|')
            page_ordering_rules.append(numbers)
        if ',' in line:
            numbers = get_numbers_from_text(line, ',')
            updates.append(numbers)


number_rules = {}
for rule in page_ordering_rules:
    number = rule[0]
    allowed_number = rule[1]

    if number not in number_rules:
        number_rules[number] = [allowed_number]
        continue

    number_rules[number].append(allowed_number)

correct_number_sequence = list()
for rule in page_ordering_rules:
    # print(f'current sequence {correct_number_sequence}')
    number = rule[0]
    allowed_number = rule[1]

    if number not in correct_number_sequence and allowed_number not in correct_number_sequence:
        correct_number_sequence.append(number)
        correct_number_sequence.append(allowed_number)
        # print(f'both new numbers: {number} should be before {allowed_number}')
        # print(f'new number sequence: {correct_number_sequence}')
        # print('\n')
        continue

    if number in correct_number_sequence and allowed_number not in correct_number_sequence:
        number_index = correct_number_sequence.index(number)
        correct_number_sequence.insert(number_index + 1, allowed_number)
        # print(f'number already exist: {number} and should be before new number {allowed_number}')
        # print(f'new number sequence: {correct_number_sequence}')
        # print('\n')
        continue

    if number not in correct_number_sequence and allowed_number in correct_number_sequence:
        allowed_number_index = correct_number_sequence.index(allowed_number)
        correct_number_sequence.insert(allowed_number_index - 1, number)
        # print(f'new number already exist: {number} and should be before existing number {allowed_number}')
        # print(f'new number sequence: {correct_number_sequence}')
        # print('\n')
        continue

    allowed_number_index = correct_number_sequence.index(allowed_number)
    number_index = correct_number_sequence.index(number)

    if number_index > allowed_number_index:
        # print(f'number already exist: {number} and should be before existing number {allowed_number}')
        # print('but current order is wrong')
        correct_number_sequence.insert(allowed_number_index, number)
        correct_number_sequence.pop(number_index + 1)
        # print(f'new number sequence: {correct_number_sequence}')
        # break
    else:
        ...
#         print(f'number {number} already before number {allowed_number}')
#     print('\n')
# print(correct_number_sequence)



test = 0
test2 = 0
total = 0
wrong_updates = []
for update in updates:
    is_correct_update = True
    final_number = update[-1]
    
    correct_update = [number for number in correct_number_sequence if number in update]

    for number in update:
        # print(f'current update {update}')
        # print(f'current number {number}')
        # numbers_after = update[update.index(number) + 1:]
        numbers_before = update[:update.index(number)]

        # print(f'numbers before {numbers_before}')
        # print(f'numbers after {numbers_after}')
        if not number in number_rules:
            # print('\n')
            continue
            
        # correct_update = [number for number in correct_number_sequence if number in update]
        # print(f'correct update {correct_update}')
        
        # if number == final_number:
        #     continue
        #     print('\n')

        # print([a in number_rules[number] for a in numbers_after])
        # print(f'number rules {number_rules[number]}')


        # test = not all([a in number_rules[number] for a in numbers_after])
        if any(a in number_rules[number] for a in numbers_before):
            is_correct_update= False
            # print(f'incorrect number placement of number: {number}')
            # print('\n')
            wrong_updates.append(update)
            break
        

        
        # print('\n')
    if is_correct_update:
        # print((len(update) - 1) / 2)
        total += update[int((len(update) - 1) / 2)]
        # print(f'correct: {update}')
    else:
        ...

    if update == correct_update:
        test += update[int((len(update) - 1) / 2)]
        print(f'correct {update}')
    else:
        print(f'added {correct_update[int((len(correct_update) - 1) / 2)]} of {correct_update} instead of {update}')
        test2 += correct_update[int((len(correct_update) - 1) / 2)]

print(f'old total {total}')
print(f'new total {test}')
print(f'total part 2 {test2}')
# print(page_ordering_rules)
# print(updates)
# print(number_rules)