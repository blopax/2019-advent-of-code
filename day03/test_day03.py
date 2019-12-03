import unittest
import day03


class TestDay03(unittest.TestCase):
    def test_get_dict_from_dir(self):
        self.assertEqual(day03.get_dict_from_dir("R1"), {'side': 'R', 'distance': 1})
        self.assertEqual(day03.get_dict_from_dir("L877"), {'side': 'L', 'distance': 877})
        self.assertEqual(day03.get_dict_from_dir("U112"), {'side': 'U', 'distance': 112})
        self.assertEqual(day03.get_dict_from_dir("D654"), {'side': 'D', 'distance': 654})


if __name__ == '__main__':
    unittest.main()
