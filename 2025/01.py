filepath = "input/01.txt"

rotations = []
with open(filepath) as file:
    for line in file.readlines():
        text = line.strip()
        rotations.append(text)

on_zero = 0
pointed_at_zero = 0
rotation_position = 50
upper_limit = 99
lower_limit = 0

for rotation in rotations:
    dial_turns = int(rotation[1:])

    if dial_turns > upper_limit + 1:
        dial_turns = dial_turns % (upper_limit + 1)
        pointed_at_zero += (int(rotation[1:]) - dial_turns) / (upper_limit + 1)

    if 'R' in rotation:
        if rotation_position + dial_turns == upper_limit + 1:
            rotation_position = lower_limit
            on_zero += 1
        elif rotation_position + dial_turns > upper_limit:
            rotation_position = lower_limit + (rotation_position + dial_turns - upper_limit) - 1
            pointed_at_zero += 1
        else:
            rotation_position += dial_turns
    elif 'L' in rotation:
        if rotation_position - dial_turns == lower_limit:
            rotation_position = lower_limit
            on_zero += 1
        elif rotation_position - dial_turns < lower_limit:
            if rotation_position != 0:
                pointed_at_zero += 1
            rotation_position = upper_limit - (dial_turns - rotation_position) + 1
        else:
            rotation_position -= dial_turns

print(on_zero)
print(pointed_at_zero)
print(on_zero + pointed_at_zero)