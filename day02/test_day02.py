import unittest
import day02


class TestDay02(unittest.TestCase):
    def test_restore_initial_values(self):
        self.assertEqual(day02.restore_initial_values([0, 0, 0, 0], 3, 3), [0, 3, 3, 0])
        self.assertEqual(day02.restore_initial_values([0, 1, 2, 3, 4, 5, 6], 12, 12), [0, 12, 12, 3, 4, 5, 6])
        self.assertEqual(day02.restore_initial_values([0, 0], 1, 1), [])

    def test_run_program(self):
        program_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        answer = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        day02.run_program(program_list, 0)
        self.assertEqual(program_list, answer)
        program_list = [1, 0, 0, 0, 99]
        answer = [2, 0, 0, 0, 99]
        day02.run_program(program_list, 0)
        self.assertEqual(program_list, answer)
        program_list = [2, 3, 0, 3, 99]
        answer = [2, 3, 0, 6, 99]
        day02.run_program(program_list, 0)
        self.assertEqual(program_list, answer)
        program_list = [2, 4, 4, 5, 99, 0]
        answer = [2, 4, 4, 5, 99, 9801]
        day02.run_program(program_list, 0)
        self.assertEqual(program_list, answer)
        program_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        answer = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        day02.run_program(program_list, 0)
        self.assertEqual(program_list, answer)


if __name__ == '__main__':
    unittest.main()
