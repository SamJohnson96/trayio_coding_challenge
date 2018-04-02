import unittest
from trayio_coding_challenge import utils

class TestMain(unittest.TestCase):

    def test_parse_instructions(self):
        lines = ['5 5\n', '1 2\n', '1 0\n', '2 2\n', '2 3\n', 'NNESEESWNWW\n']
        results = utils.parse_instructions(lines)
        expected_result = [['5','5'],['1','2'],['1','0'],['2','2'],['2','3'],['NNESEESWNWW']]
        self.assertEqual(results,expected_result)

    def test_create_room(self):
        size = ['3', '2']
        dirt_spots = [['1', '1'], ['0', '1']]
        map = utils.create_room(size, dirt_spots)
        self.assertEqual(3, len(map))
        self.assertEqual(4, len(map[0]))

    def test_create_room_detect_dirt_spots(self):
        size = ['5', '5']
        dirt_spots = [['0', '0'], ['5', '5']]
        map = utils.create_room(size, dirt_spots)
        self.assertEqual(1, map[0][0])
        self.assertEqual(1, map[5][5])

if __name__ == '__main__':
    unittest.main()
