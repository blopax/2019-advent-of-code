import unittest
import intcode


class TestDay05(unittest.TestCase):
    def test_restore_initial_values(self):
        self.assertEqual(intcode.restore_initial_values([0, 0, 0, 0], 3, 3), [0, 3, 3, 0])
        self.assertEqual(intcode.restore_initial_values([0, 1, 2, 3, 4, 5, 6], 12, 12), [0, 12, 12, 3, 4, 5, 6])
        self.assertEqual(intcode.restore_initial_values([0, 0], 1, 1), [])

    def test_run_program(self):
        program_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        answer = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        cpu = intcode.Intcode(program_list)
        cpu.run_program()
        self.assertEqual(cpu.program, answer)

        program_list = [1, 0, 0, 0, 99]
        answer = [2, 0, 0, 0, 99]
        cpu = intcode.Intcode(program_list)
        cpu.run_program()
        self.assertEqual(cpu.program, answer)

        program_list = [2, 3, 0, 3, 99]
        answer = [2, 3, 0, 6, 99]
        cpu = intcode.Intcode(program_list)
        cpu.run_program()
        self.assertEqual(cpu.program, answer)

        program_list = [2, 4, 4, 5, 99, 0]
        answer = [2, 4, 4, 5, 99, 9801]
        cpu = intcode.Intcode(program_list)
        cpu.run_program()
        self.assertEqual(cpu.program, answer)

        program_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        answer = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        cpu = intcode.Intcode(program_list)
        cpu.run_program()
        self.assertEqual(cpu.program, answer)

    def test_program_input_output(self):
        program_list = [3, 0, 4, 0, 99]
        program_input = 42
        cpu = intcode.Intcode(program_list)
        cpu.run_program(program_input)
        self.assertEqual(cpu.output[-1], program_input)

        program_list = [3, 0, 4, 0, 99]
        program_input = 1
        cpu = intcode.Intcode(program_list)
        cpu.run_program(program_input)
        self.assertEqual(cpu.output[-1], program_input)

        program_list = [3, 0, 4, 0, 99]
        program_input = 2
        cpu = intcode.Intcode(program_list)
        cpu.run_program(program_input)
        self.assertEqual(cpu.output[-1], program_input)

    def test_equals_less(self):
        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input == 8)

        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input < 8)

        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input == 8)

        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input < 8)

    def test_jump_if_condition(self):
        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input != 0)

        for program_input in [x - 10 for x in range(30)]:
            program_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], program_input != 0)

    def test_bigger_test(self):
        for program_input in range(20):
            program_list = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                            1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                            999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
            if program_input < 8:
                answer = 999
            elif program_input == 8:
                answer = 1000
            else:
                answer = 1001
            cpu = intcode.Intcode(program_list)
            cpu.run_program(program_input)
            self.assertEqual(cpu.output[-1], answer)


if __name__ == '__main__':
    unittest.main()
