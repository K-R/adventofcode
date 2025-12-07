import time

start = time.time()

def get_movable_papers(grid) -> list[tuple[str, str]]:
    coordinates_of_papers_to_move = []
    for x, line in enumerate(lines):
        for y, character in enumerate(line):
            if character != '@':
                continue
            
            # print(f'search for {x, y}')

            coordinates = [
                {'x': x - 1,'y': y - 1},
                {'x': x - 1,'y': y},
                {'x': x - 1,'y': y + 1},
                {'x': x,'y': y + 1},
                {'x': x + 1,'y': y + 1},
                {'x': x + 1,'y': y},
                {'x': x + 1, 'y': y - 1},
                {'x': x,'y': y - 1},
            ]

            paper_rolls = 0
            for coordinate in coordinates:
                if coordinate['x'] < 0 or coordinate['x'] > len(lines) - 1:
                    continue

                if coordinate['y'] < 0 or coordinate['y'] > len(line) - 1:
                    continue
                
                # print(f"looking at {coordinate['x'], coordinate['y']} for total x of {len(lines)} and width of {len(line)}")

                shelve = lines[coordinate['x']][coordinate['y']]
                if '@' in shelve:
                    # print(f"Adjecent role at {coordinate['x'], coordinate['y']} for column with value {shelve}")
                    paper_rolls += 1
            
            # print(f"number of adjecent paper rolls {paper_rolls} for {x, y} \n")
            if paper_rolls < 4:
                coordinates_of_papers_to_move.append((x, y))
    return coordinates_of_papers_to_move


total_roles = 0
filepath = "input/04.txt"
with open(filepath) as file:
    lines = [line.strip() for line in file.readlines()]
    
    movable_paper_coordinates = get_movable_papers(lines)
    total_roles += len(movable_paper_coordinates)

    while movable_paper_coordinates:
        for coordinate in movable_paper_coordinates:
            x, y = coordinate
            lines[x] = lines[x][:y] + '.' + lines[x][y + 1:]

        movable_paper_coordinates = get_movable_papers(lines)
        total_roles += len(movable_paper_coordinates)

print(f"total roles {total_roles}")

end = time.time()
print(f"{end - start:.2f} seconden")