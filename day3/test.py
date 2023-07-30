import unittest
from solution import DayThree, PriorityType
from ddt import ddt, data, unpack, file_data

@ddt
class TestDayThree(unittest.TestCase):
    @data(
        ("vJrwpWtwJgWrhcsFMMfFFhFp", 16), 
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38), 
        ("PmmdzqPrVvPwwTWBwg", 42),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
        ("ttgJtRGJQctTZtZT", 20),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", 19)
    )
    @unpack
    def test_priority(self, value, expected):
        d3 = DayThree(None)
        self.assertEqual(d3.priority(d3.sharedItem(PriorityType.COMPARTMENT, [value])), expected)
    
    def test_run_compartment(self):
        with open("test.txt", "r") as f:
             lines = list(map(lambda s: s.strip(), f.readlines()))
             d3 = DayThree(lines)
             self.assertEqual(d3.run(PriorityType.COMPARTMENT), 157)

    def test_run_group(self):
        with open("test.txt", "r") as f:
             lines = list(map(lambda s: s.strip(), f.readlines()))
             d3 = DayThree(lines)
             self.assertEqual(d3.run(PriorityType.GROUP), 70)
		
if __name__ == "__main__":
	unittest.main()
