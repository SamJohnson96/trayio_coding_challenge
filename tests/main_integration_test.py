import unittest
import main

class IntegrationTest(unittest.TestCase):

    def test_main(self):
        final_x, final_y, dirt_cleaned = main.main()
        self.assertEqual(final_x,1)
        self.assertEqual(final_y,3)
        self.assertEqual(dirt_cleaned,1)
