from solution import DayEight
import unittest
from ddt import ddt, data, unpack

@ddt
class TestDayEight(unittest.TestCase):
    def setUp(self):
        with open("test.txt", "r") as f:
            lines = f.readlines()
            self.d8 = DayEight(lines)
    
    def test_init(self):
        self.assertTrue(self.d8.n_rows, 5)
        self.assertTrue(self.d8.n_columns, 5)
        self.assertTrue(self.d8.n_visible, 16)
        self.assertEqual(self.d8.interior_tree_coords,[(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)])

    @data(
        ((1,1), True),
        ((1,2), True),
        ((1,3), False),
        ((2,1), True),
        ((2,2), False),
        ((2,3), True),
        ((3,1), False),
        ((3,2), True),
        ((3,3), False),
    )
    @unpack
    def test_is_visible(self, input, expected):
        self.assertEqual(self.d8.is_visible(input), expected)

    def test_total_visible_trees(self):
        self.assertEqual(self.d8.total_visible_trees(), 21)

    @data(
        ((1,1), 1),
        ((1,2), 6),
        ((1,3), 1),
        ((2,1), 4),
        ((2,2), 1),
        ((2,3), 8),
        ((3,1), 1),
        ((3,2), 2),
        ((3,3), 3),
    )
    @unpack
    def test_scenic_score(self, input, expected):
        self.assertEqual(self.d8.scenic_score(input), expected)

    def test_highest_scenic_score(self):
        self.assertEqual(self.d8.highest_scenic_score(), 8)


if __name__ == "__main__":
    unittest.main()