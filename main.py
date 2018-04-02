from trayio_coding_challenge.utils import parse_instructions, create_room
from trayio_coding_challenge.route_controller import RouteController

def main():
    with open('./input.txt') as f:
        lines = f.readlines()
    instructions = parse_instructions(lines)
    map = create_room(
        instructions[0], instructions[2:len(instructions)-1])
    controller = RouteController(
        map, instructions[1], instructions[len(instructions)-1])
    return controller.run_route()

if __name__ == "__main__":
    final_x, final_y, dirt_cleaned = main()
    print (final_x, final_y)
    print (dirt_cleaned)
