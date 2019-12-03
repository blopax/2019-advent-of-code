import unittest
import day03_map
import day03_complex


class TestDay03(unittest.TestCase):
    def test_get_dict_from_dir(self):
        self.assertEqual(day03_map.get_dict_from_dir("R1"), {'side': 'R', 'distance': 1})
        self.assertEqual(day03_map.get_dict_from_dir("L877"), {'side': 'L', 'distance': 877})
        self.assertEqual(day03_map.get_dict_from_dir("U112"), {'side': 'U', 'distance': 112})
        self.assertEqual(day03_map.get_dict_from_dir("D654"), {'side': 'D', 'distance': 654})

    def test_day03_map(self):
        map_input = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
        self.assertEqual(day03_map.full_test(map_input), (159, 610))
        map_input = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        self.assertEqual(day03_map.full_test(map_input), (135, 410))

    def test_day03_complex(self):
        map_input = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
        self.assertEqual(day03_complex.full_test(map_input), (159, 610))
        map_input = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        self.assertEqual(day03_complex.full_test(map_input), (135, 410))


if __name__ == '__main__':
    unittest.main()
