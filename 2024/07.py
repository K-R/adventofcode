import itertools

with open("input/07.txt") as file:
    equations = []
    for line in file.readlines():
        target_number, number_row = line.strip().split(':')
        numbers = [int(number) for number in number_row.strip().split(' ')]
        equations.append((int(target_number), numbers))

def is_valid_equation(numbers: list[int], operators: list[str], target_number: int) -> bool:
    total = numbers[0]
    for index, operator in enumerate(operators):
        if operator == '+':
            total +=  numbers[index + 1]
            continue
        elif operator == '*':
            total *=  numbers[index + 1]
            continue
        elif operator == '||':
            total = int(str(total) + str(numbers[index + 1]))
            continue

    return total == target_number
    
total_calibration_result = 0
for equation in equations:
    target_number, numbers = equation
    operators = ['+', '*', "||"]
    
    operator_combinations = itertools.product(operators, repeat=len(numbers) - 1)
    for operators in operator_combinations:
        if is_valid_equation(numbers, operators, target_number):
            total_calibration_result += target_number
            break
