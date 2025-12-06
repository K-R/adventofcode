import time

start = time.time()

filepath = "input/03.txt"


def get_voltage(bank, number_of_batteries):
    configured_bank = []
    for index, battery in enumerate(bank):
        new_battery = int(battery)
        if not configured_bank:
            configured_bank.append(new_battery)
            continue

        top_battery = configured_bank[-1]
        if new_battery <= top_battery and len(configured_bank) < number_of_batteries:
            configured_bank.append(new_battery)
            continue
            
        if new_battery > top_battery:
            batteries_smaller_then_new_battery = [existing_battery for existing_battery in configured_bank if existing_battery < new_battery]
            lowest_stacked_battery = max(batteries_smaller_then_new_battery)
            batteries_to_remove = configured_bank[configured_bank.index(lowest_stacked_battery):]

            if (len(configured_bank) - len(batteries_to_remove) + (len(bank) - index)) < number_of_batteries:
                allowed_number_of_batteries_removed = (len(bank) - index) + len(configured_bank) - number_of_batteries

                if allowed_number_of_batteries_removed == 0:
                    batteries_to_remove = []
                else:
                    batteries_to_remove = batteries_to_remove[-allowed_number_of_batteries_removed:]

            for remove_battery in batteries_to_remove:
                configured_bank.remove(remove_battery)
            configured_bank.append(new_battery)
    
    final_bank = ""
    for battery in configured_bank:
        final_bank += str(battery)

    return int(final_bank)


total_output_joltage_2_batterie = 0
total_output_joltage_12_batteries = 0
with open(filepath) as file:
    for bank in file:
        
        bank = bank.strip()
        og_bank = bank
        highest_number = max(bank)

        if bank.count(highest_number) == 1 and bank.index(highest_number) == len(bank) - 1:
            numbers = [number for number in bank if number != highest_number]
            highest_number = max(numbers)

        total_output_joltage_2_batterie += get_voltage(bank, 2)
        total_output_joltage_12_batteries += get_voltage(bank, 12)

print(total_output_joltage_2_batterie)
print(total_output_joltage_12_batteries)

end = time.time()
print(f"{end - start:.2f} seconden")