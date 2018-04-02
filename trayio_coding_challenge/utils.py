def parse_instructions(lines):
    instructions = [line.strip() for line in lines]
    return [line.split() for line in instructions]

def create_room(size, dirt_spots):
    room_matrix = [[0 for x in range(int(size[0])+1)]
                   for y in range(int(size[1])+1)]
    for dirt in dirt_spots:
        x = int(dirt[0])
        y = int(dirt[1])
        room_matrix[x][y] = 1
    return room_matrix
