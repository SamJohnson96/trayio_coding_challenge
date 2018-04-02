import unittest
from trayio_coding_challenge import utils
from trayio_coding_challenge.route_controller import RouteController

class TestRouteController(unittest.TestCase):

    def test_create_route_controller(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '1']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        self.assertEqual(room, route_controller.room)
        self.assertEqual(0, route_controller.x)
        self.assertEqual(1, route_controller.y)
        self.assertEqual('NWES', route_controller.directions)
        self.assertEqual(0, route_controller.dirt_cleaned)

    def test_go_north(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '1']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_north()
        self.assertEqual(2, route_controller.y)

    def test_go_south(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '1']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_south()
        self.assertEqual(0, route_controller.y)

    def test_go_east(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '1']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_east()
        self.assertEqual(1, route_controller.x)

    def test_go_west(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['1', '1']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_west()
        self.assertEqual(0, route_controller.x)

    def test_outbounds_north(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['1', '3']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_north()
        self.assertEqual(3, route_controller.y)

    def test_outbounds_south(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['1', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_south()
        self.assertEqual(0, route_controller.y)

    def test_outbounds_east(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['3', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_east()
        self.assertEqual(3, route_controller.x)

    def test_outbounds_west(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_west()
        self.assertEqual(0, route_controller.x)

    def test_is_dirt(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_north()
        self.assertTrue(route_controller.is_dirt())

    def test_is_not_dirt(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        self.assertFalse(route_controller.is_dirt())

    def test_remove_dirt(self):
        size = ['3', '3']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '0']
        instructions = ['NWES']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        route_controller.go_north()
        self.assertTrue(route_controller.is_dirt())
        route_controller.remove_dirt()
        self.assertFalse(route_controller.is_dirt())

    def test_run_route(self):
        size = ['5', '5']
        dirt_spots = [['1', '1'], ['0', '1']]
        current_spot = ['0', '0']
        instructions = ['NESSE']
        room = utils.create_room(size, dirt_spots)
        route_controller = RouteController(room, current_spot, instructions)
        new_x, new_y, dirt_collected = route_controller.run_route()
        self.assertEqual(2, new_x)
        self.assertEqual(0, new_y)
        self.assertEqual(2, dirt_collected)


if __name__ == '__main__':
    unittest.main()
