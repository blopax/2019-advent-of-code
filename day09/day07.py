import copy
import itertools

import intcode


def part_one(program):
    max_signal = 0
    phase_sequence_lists = list(itertools.permutations([0, 1, 2, 3, 4]))

    for phase_sequence in phase_sequence_lists:
        input_amplifier = 0
        output_amplifier = 0
        for phase_input in phase_sequence:
            program_list = copy.deepcopy(program)
            cpu = intcode.Intcode(program_list)
            cpu.run_program(input_list=[phase_input, input_amplifier])
            output_amplifier = cpu.output[-1]
            input_amplifier = output_amplifier
        if output_amplifier > max_signal:
            max_signal = output_amplifier
    return max_signal


def signal_after_loop(program, phase_sequence):
    amplifiers_list = []
    i = 0
    for phase_input in phase_sequence:
        name = "Amplifier_{}".format((chr(ord('A') + i)))
        amplifier = intcode.Intcode(copy.deepcopy(program), name)
        amplifier.input = [phase_input]
        amplifiers_list.append(amplifier)
        i += 1

    signal_sent = 0
    i = 0
    while (amplifiers_list[4]).stop_program is False:
        amplifier = amplifiers_list[i % 5]
        amplifier.run_program(input_int=signal_sent)
        signal_sent = amplifier.output[-1]
        i += 1

    return signal_sent


def part_two(program):
    phase_sequence_lists = list(itertools.permutations([5, 6, 7, 8, 9]))
    max_signal = -1
    for phase_sequence in phase_sequence_lists:
        max_signal = max(signal_after_loop(program, list(phase_sequence)), max_signal)
    return max_signal


if __name__ == '__main__':
    # Part One
    program_input = intcode.get_input('input07.txt')
    print(part_one(program_input))

    # Part Two
    program_input = intcode.get_input("input07.txt")
    print(part_two(program_input))
