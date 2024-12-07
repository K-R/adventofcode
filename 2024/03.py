import re

with open("input/03.txt") as file:
    data = file.read()

is_part_one = False

total = 0
multiplying_enabled = True
matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))", data)
for match in matches:
    first_number, second_number, do_instruction, do_not_instruction = match

    if do_instruction:
        multiplying_enabled = True

    if do_not_instruction:
        multiplying_enabled = False

    if first_number and second_number and (multiplying_enabled or is_part_one):
        result = int(first_number) * int(second_number)
        total += result
