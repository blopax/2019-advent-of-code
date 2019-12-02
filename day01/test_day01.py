import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_fuel_for_mass(self):
        self.assertEqual(day01.fuel_for_mass(12), 2)
        self.assertEqual(day01.fuel_for_mass(14), 2)
        self.assertEqual(day01.fuel_for_mass(1969), 654)
        self.assertEqual(day01.fuel_for_mass(100756), 33583)

    def test_fuel_for_module(self):
        self.assertEqual(day01.fuel_for_module(12), 2)
        self.assertEqual(day01.fuel_for_module(14), 2)
        self.assertEqual(day01.fuel_for_module(1969), 966)
        self.assertEqual(day01.fuel_for_module(100756), 50346)


if __name__ == '__main__':
    unittest.main()
