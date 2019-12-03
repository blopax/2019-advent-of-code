import copy


def get_input(input_path):
    with open(input_path) as f:
        input_str = f.read()
    return [int(x) for x in input_str.strip().split(',')]


def restore_initial_values(program, input_noun, input_verb):
    try:
        if len(program) < 4:
            return []
        program[1] = input_noun
        program[2] = input_verb
        return program
    except Exception as err:
        print(err)


def intcode_stop_program(position):
    stop_program = True
    return position, stop_program


def intcode_sum(program, position):
    try:
        stop_program = False
        input1_position = program[position + 1]
        input2_position = program[position + 2]
        output_position = program[position + 3]
        program[output_position] = program[input1_position] + program[input2_position]
        return position + 4, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_multiply(program, position):
    try:
        stop_program = False
        input1_position = program[position + 1]
        input2_position = program[position + 2]
        output_position = program[position + 3]
        program[output_position] = program[input1_position] * program[input2_position]
        return position + 4, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_operation(program, position):
    try:
        opcode = program[position]
        if opcode == 99:
            return intcode_stop_program(position)
        elif opcode == 1:
            return intcode_sum(program, position)
        elif opcode == 2:
            return intcode_multiply(program, position)
        else:
            raise Exception
    except Exception as err:
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def run_program(program, position):
    stop_program = False
    while stop_program is False:
        position, stop_program = intcode_operation(program, position)
    return position, stop_program


if __name__ == '__main__':
    program_input = get_input('input02.txt')

    # Part One
    program_list = copy.copy(program_input)
    program_list = restore_initial_values(program_list, 12, 2)
    run_program(program_list, 0)
    print(program_list[0])

    # Part Two
    keep_on = True
    expected_output = 19690720
    while keep_on:
        for noun in range(100):
            for verb in range(100):
                program_list = copy.copy(program_input)
                program_list = restore_initial_values(program_list, noun, verb)
                final_position, stop_program_list = run_program(program_list, 0)
                if program_list[0] == expected_output:
                    print(noun, verb)
                    keep_on = False
        keep_on = False
