import copy

INPUT = 1
OUTPUT = []


def get_input(input_path):
    with open(input_path) as f:
        input_str = f.read()
    input_list = input_str.strip().split(',')
    return [int(x) for x in input_list]


def restore_initial_values(program, input_noun, input_verb):
    try:
        if len(program) < 4:
            return []
        program[1] = input_noun
        program[2] = input_verb
        return program
    except Exception as err:
        print(err)


def get_param(program, param_position, param_mode):
    if param_mode == 0:
        return program[param_position]
    elif param_mode == 1:
        return param_position


def intcode_stop_program(position):
    stop_program = True
    return position, stop_program


def intcode_sum(program, position, param_modes):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        param2 = get_param(program, position + 2, int(param_modes_str[-2]))
        param3 = get_param(program, position + 3, int(param_modes_str[-3]))
        program[param3] = program[param1] + program[param2]
        return position + 4, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_multiply(program, position, param_modes):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        param2 = get_param(program, position + 2, int(param_modes_str[-2]))
        param3 = get_param(program, position + 3, int(param_modes_str[-3]))
        program[param3] = program[param1] * program[param2]
        return position + 4, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_read_input(program, position, param_modes):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        program[param1] = INPUT
        return position + 2, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_write_output(program, position, param_modes):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        OUTPUT.append(program[param1])
        return position + 2, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_jump_if_condition(program, position, param_modes, condition=True):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        param2 = get_param(program, position + 2, int(param_modes_str[-2]))
        if (program[param1] != 0) is condition:
            return program[param2], stop_program
        return position + 3, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_check(program, position, param_modes, check="equals"):
    try:
        stop_program = False
        param_modes_str = str("000" + str(param_modes))
        param1 = get_param(program, position + 1, int(param_modes_str[-1]))
        param2 = get_param(program, position + 2, int(param_modes_str[-2]))
        param3 = get_param(program, position + 3, int(param_modes_str[-3]))
        if check == "equals" and program[param1] == program[param2]:
            program[param3] = 1
        elif check == "less" and program[param1] < program[param2]:
            program[param3] = 1
        else:
            program[param3] = 0
        return position + 4, stop_program
    except Exception as err:  # depassement de liste
        stop_program = True
        print("An error occured: {}".format(err))
        return position, stop_program


def intcode_operation(program, position):
    try:
        opcode_param_modes_value = program[position]
        opcode = opcode_param_modes_value % 100
        param_modes = int(opcode_param_modes_value / 100)
        if opcode == 99:
            return intcode_stop_program(position)
        elif opcode == 1:
            return intcode_sum(program, position, param_modes)
        elif opcode == 2:
            return intcode_multiply(program, position, param_modes)
        elif opcode == 3:
            return intcode_read_input(program, position, param_modes)
        elif opcode == 4:
            return intcode_write_output(program, position, param_modes)
        elif opcode == 5:
            return intcode_jump_if_condition(program, position, param_modes, condition=True)
        elif opcode == 6:
            return intcode_jump_if_condition(program, position, param_modes, condition=False)
        elif opcode == 7:
            return intcode_check(program, position, param_modes, check="less")
        elif opcode == 8:
            return intcode_check(program, position, param_modes, check="equals")
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
    program_input = get_input('input05.txt')

    # Part One

    program_list = copy.copy(program_input)
    run_program(program_list, 0)
    print(OUTPUT)

    # Part One
    INPUT = 5
    OUTPUT = []
    program_list_2 = copy.copy(program_input)
    run_program(program_list_2, 0)
    print(OUTPUT)
