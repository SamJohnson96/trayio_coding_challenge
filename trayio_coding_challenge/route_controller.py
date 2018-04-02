class RouteController:

    def __init__(self, room, starting_place, directions):
        self.room = room
        self.x = int(starting_place[0])
        self.y = int(starting_place[1])
        self.directions = directions[0]
        self.dirt_cleaned = 0
        self.max_y = len(self.room) - 1
        self.max_x = len(self.room[0]) - 1

    def go_north(self):
        if self.y != self.max_y:
            self.y += 1

    def go_south(self):
        if self.y != 0:
            self.y -= 1

    def go_east(self):
        if self.x != self.max_x:
            self.x += 1

    def go_west(self):
        if self.x != 0:
            self.x -= 1

    def is_dirt(self):
        return self.room[self.x][self.y] == 1

    def remove_dirt(self):
        self.dirt_cleaned += 1
        self.room[self.x][self.y] = 0

    def run_route(self):
        # Check if starting place is dirt as hoover is always on
        if self.is_dirt():
            self.remove_dirt()

        for direction in self.directions:
            if direction.upper() == "N":
                self.go_north()
            elif direction.upper() == "E":
                self.go_east()
            elif direction.upper() == "S":
                self.go_south()
            elif direction.upper() == "W":
                self.go_west()

            if self.is_dirt():
                self.remove_dirt()

        return self.x, self.y, self.dirt_cleaned
