from solution import DaySeven
from ddt import ddt, data, unpack
import unittest

@ddt
class TestDaySeven(unittest.TestCase):
    def setUp(self):
        with open("test.txt", "r") as f:
            lines = f.readlines()
            self.d7 = DaySeven(lines)
  
    def test_root_total_size(self):
        self.assertEqual(self.d7.root_total_size(), 48381165) 
    
    @data([('/', 48381165), ('a', 94853), ('d', 24933642), ('e', 584)])
    def test_tree_directories(self, expected):
        dirs = sorted(self.d7.tree_directories())
        self.assertEqual(dirs, expected)
         
    @data((10000000, 95437))
    @unpack
    def test_sum_of_all_directories_lte(self, total_size, expected):
        self.assertEqual(self.d7.sum_of_all_directories_lte(total_size), expected)   

    @data((70000000, 30000000))
    @unpack
    def test_size_of_smallest_dir_to_delete_for_space(self, totalSpace, requiredFreeSpace):
        self.assertEqual(self.d7.size_of_smallest_dir_to_delete_for_space(totalSpace-self.d7.root_total_size(), requiredFreeSpace), 24933642)


if __name__ == "__main__":
    unittest.main()