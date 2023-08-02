import unittest
from solution import DaySix
from ddt import ddt, data, unpack

@ddt
class TestDaySix(unittest.TestCase):
    @data(
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    )
    @unpack
    def test_markerPosition_packet(self, input, expected):
        d6 = DaySix()
        actual = d6.markerPosition(input, 4)
        self.assertEqual(actual, expected)

    @data(
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    )
    @unpack
    def test_markerPosition_message(self, input, expected):
        d6 = DaySix()
        actual = d6.markerPosition(input, 14)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()