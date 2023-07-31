from solution import DayFive, Parts
import unittest

class TestDayFive(unittest.TestCase):
    def setUp(self):
        with open("test.txt", "r") as f:
            lines = f.readlines()
            self.d5 = DayFive(lines)

    def test_parseInput(self):
        expected = [["N", "Z"], ["D", "C", "M"], ["P"]]
        actual, _ = self.d5.parseInput()
        self.assertEqual(actual, expected)
    
    def test_crateDance_p1(self):
        expected = [["C"], ["M"], ["Z", "N", "D", "P"]]
        s, d = self.d5.parseInput()
        self.assertEqual(self.d5.crateDance(Parts.PART_ONE, s, d), expected)
   
    def test_crateDance_p2(self):
        expected = [["M"], ["C"], ["D", "N", "Z", "P"]]
        s, d = self.d5.parseInput()
        self.assertEqual(self.d5.crateDance(Parts.PART_TWO, s, d), expected)

    def test_topStackCrates_p1(self):
        s, d = self.d5.parseInput()
        rs = self.d5.crateDance(Parts.PART_ONE, s, d)
        self.assertEqual(self.d5.topStackCrates(rs), "CMZ")

    def test_topStackCratesV2_p2(self):
        s, d = self.d5.parseInput()
        rs = self.d5.crateDance(Parts.PART_TWO, s, d)
        self.assertEqual(self.d5.topStackCrates(rs), "MCD")

if __name__ == "__main__":
    unittest.main()