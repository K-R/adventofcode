filepath = "input/01.txt"

with open(filepath) as file:
    locations_first_group = []
    locations_second_group = []
    for line in file.readlines():
        location_first_group, location_second_group = line.split()

        locations_first_group.append(int(location_first_group))
        locations_second_group.append(int(location_second_group))

locations_first_group = sorted(locations_first_group)
locations_second_group = sorted(locations_second_group)

total_distance = 0
total_similarity = 0
similary_calculations = dict()
for location_first_group, location_second_group in zip(locations_first_group, locations_second_group):
    distance = abs(location_first_group - location_second_group)
    total_distance += distance

    similarity = location_first_group * locations_second_group.count(location_first_group)
    total_similarity += similarity