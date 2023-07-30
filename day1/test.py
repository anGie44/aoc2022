import unittest
from solution import DayOne


class TestDayOne(unittest.TestCase):
	def test_calculate_max_n_calories(self):
		with open("test.txt", "r") as f:
			lines = f.readlines()
			d1 = DayOne(lines)
				
			self.assertEqual(d1.calculateMaxNCalories(1), 24000)
			self.assertEqual(d1.calculateMaxNCalories(2), 35000)
			self.assertEqual(d1.calculateMaxNCalories(3), 45000)

		
if __name__ == "__main__":
	unittest.main()
