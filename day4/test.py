import unittest
from solution import DayFour, Parts
from ddt import ddt, data, unpack

@ddt
class TestDayFour(unittest.TestCase):
    @data(
        ("2-4,6-8", [(2,4),(6,8)]), 
        ("2-3,4-5", [(2,3),(4,5)]), 
        ("5-7,7-9", [(5,7),(7,9)]), 
        ("2-8,3-7", [(2,8),(3,7)]), 
        ("6-6,4-6", [(6,6),(4,6)]), 
        ("2-6,4-8", [(2,6),(4,8)]), 
    )
    @unpack
    def test_parseAssignments(self, value, expected):
        d4 = DayFour(None)
        self.assertEqual(d4.parseAssignments(value), expected)

    @data(
        ((2,4),(6,8), False), 
        ((2,3),(4,5), False), 
        ((5,7),(7,9), False), 
        ((2,8),(3,7), True), 
        ((6,6),(4,6), True), 
        ((2,6),(4,8), False), 
    )
    @unpack
    def test_fullyContained(self, t1, t2, expected):
        d4 = DayFour(None)
        self.assertEqual(d4.fullyContained(t1, t2), expected)

    @data((Parts.PART_ONE, 2), (Parts.PART_TWO, 4))
    @unpack
    def test_run(self, part, expected):
        with open("test.txt", "r") as f:
            lines = list(map(lambda s: s.strip(), f.readlines()))
            d4 = DayFour(lines)
            self.assertEqual(d4.run(part), expected)

if __name__ == "__main__":
    unittest.main()