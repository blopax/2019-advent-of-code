import unittest

import day07
import intcode


class TestDay07(unittest.TestCase):
    def test_sequential_amplifiers(self):
        program_input = intcode.get_input('input07.txt')
        self.assertEqual(day07.part_one(program_input), 21760)
        program_input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        self.assertEqual(day07.part_one(program_input), 43210)
        program_input = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0,
                         0]
        self.assertEqual(day07.part_one(program_input), 54321)
        program_input = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31,
                         31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
        self.assertEqual(day07.part_one(program_input), 65210)

    def test_signal_after_loop(self):
        phase_sequence = [9, 8, 7, 6, 5]
        program_input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005,
                         28, 6, 99, 0, 0, 5]
        self.assertEqual(day07.signal_after_loop(program_input, phase_sequence), 139629729)

        phase_sequence = [9, 7, 8, 5, 6]
        program_input = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54,
                         1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56,
                         -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
        self.assertEqual(day07.signal_after_loop(program_input, phase_sequence), 18216)

    def test_loop_amplifiers(self):
        program_input = intcode.get_input('input07.txt')
        self.assertEqual(day07.part_two(program_input), 69816958)
        program_input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005,
                         28, 6, 99, 0, 0, 5]
        self.assertEqual(day07.part_two(program_input), 139629729)
        program_input = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54,
                         1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56,
                         -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
        self.assertEqual(day07.part_two(program_input), 18216)


if __name__ == '__main__':
    unittest.main()
