import copy


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


class Intcode:
    def __init__(self, program, name=None):
        self.memory = [0] * 10000
        self.program = program + self.memory
        self.name = name
        self.input = []
        self.output = []
        self.position = 0
        self.relative_base = 0
        self.stop_program = False
        self.next = False

    def __str__(self):
        string = """
        program_state = {}
        program_name = {}
        inputs = {}
        output = {}
        position = {}
        stop_program = {}
        next = {}
        """.format(self.program, self.name, self.input, self.output, self.position, self.stop_program, self.next)
        return string
    
    def get_param(self, param_position, param_mode):
        if param_mode == 0:  # position mode
            return self.program[param_position]
        elif param_mode == 1:  # immediate mode
            return param_position
        elif param_mode == 2:  # relative mode
            return self.program[param_position] + self.relative_base

    def intcode_stop_program(self):
        self.stop_program = True

    def intcode_sum(self, param_modes):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            param2 = self.get_param(self.position + 2, int(param_modes_str[-2]))
            param3 = self.get_param(self.position + 3, int(param_modes_str[-3]))
            self.program[param3] = self.program[param1] + self.program[param2]
            self.position += 4
        except Exception as err: 
            self.stop_program = True
            print(self)
            print("An error occured in add: {}".format(err))

    def intcode_multiply(self, param_modes):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            param2 = self.get_param(self.position + 2, int(param_modes_str[-2]))
            param3 = self.get_param(self.position + 3, int(param_modes_str[-3]))
            self.program[param3] = self.program[param1] * self.program[param2]
            self.position += 4 
        except Exception as err:  
            self.stop_program = True
            print(self)
            print("An error occured in multiply: {}".format(err))

    def intcode_read_input(self, param_modes):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            if len(self.input) > 0:
                self.program[param1] = self.input.pop(0)
                self.position += 2
            else:
                raise Exception
        except Exception as err:  
            self.stop_program = True
            print(self)
            print("self.input = {}".format(self.input))
            print("An error occured in read: {}".format(err))

    def intcode_write_output(self, param_modes):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            self.output.append(self.program[param1])
            self.position += 2
        except Exception as err: 
            self.stop_program = True
            print(self)
            print("An error occured in write: {}".format(err))

    def intcode_jump_if_condition(self, param_modes, condition=True):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            param2 = self.get_param(self.position + 2, int(param_modes_str[-2]))
            if (self.program[param1] != 0) is condition:
                self.position = self.program[param2]
            else:
                self.position += 3
        except Exception as err: 
            self.stop_program = True
            print(self)
            print("An error occured in jump: {}".format(err))

    def intcode_check(self, param_modes, check="equals"):
        try:
            param_modes_str = str("000" + str(param_modes))
            param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
            param2 = self.get_param(self.position + 2, int(param_modes_str[-2]))
            param3 = self.get_param(self.position + 3, int(param_modes_str[-3]))
            if check == "equals" and self.program[param1] == self.program[param2]:
                self.program[param3] = 1
            elif check == "less" and self.program[param1] < self.program[param2]:
                self.program[param3] = 1
            else:
                self.program[param3] = 0
            self.position += 4
        except Exception as err: 
            self.stop_program = True
            print(self)
            print("An error occured in less or in equals: {}".format(err))

    def intcode_adjust_relative_base(self, param_modes):
        param_modes_str = str("000" + str(param_modes))
        param1 = self.get_param(self.position + 1, int(param_modes_str[-1]))
        self.relative_base += self.program[param1]
        self.position += 2

    def intcode_operation(self):
        try:
            opcode_param_modes_value = self.program[self.position]
            opcode = opcode_param_modes_value % 100
            param_modes = int(opcode_param_modes_value / 100)
            if opcode == 99:
                self.intcode_stop_program()
            elif opcode == 1:
                self.intcode_sum(param_modes)
            elif opcode == 2:
                self.intcode_multiply(param_modes)
            elif opcode == 3:
                self.intcode_read_input(param_modes)
            elif opcode == 4:
                # self.next = True  # TODO: define if next active or not as an option
                self.intcode_write_output(param_modes)
            elif opcode == 5:
                self.intcode_jump_if_condition(param_modes, condition=True)
            elif opcode == 6:
                self.intcode_jump_if_condition(param_modes, condition=False)
            elif opcode == 7:
                self.intcode_check(param_modes, check="less")
            elif opcode == 8:
                self.intcode_check(param_modes, check="equals")
            elif opcode == 9:
                self.intcode_adjust_relative_base(param_modes)
            else:
                raise Exception
        except Exception as err:
            self.stop_program = True
            print(self)
            print("An error occured in the intcode operation. the opcode doesn't exist.: {}".format(err))

    def run_program(self, input_int=0, input_list=None):
        if input_list is not None:
            self.input += input_list
        else:
            self.input.append(input_int)
        self.next = False
        while self.stop_program is False and self.next is False:
            self.intcode_operation()
        return self


if __name__ == '__main__':
    program_input = get_input('input05.txt')

    # Part One
    program_list = copy.copy(program_input)
    cpu = Intcode(program_list)
    cpu.run_program(input_int=1)
    print(cpu.output)

    # Part Two
    program_list_2 = copy.copy(program_input)
    cpu = Intcode(program_list_2)
    cpu.run_program(input_int=5)
    print(cpu.output)

    print("bob")
    # Part Two
    program_list_2 = [109, 19, 99]
    cpu = Intcode(program_list_2)
    cpu.relative_base = 2000
    cpu.run_program()
    print(cpu.relative_base)

    program_list_2 = [109, 19, 204, -34, 99] # + list_2000
    cpu = Intcode(program_list_2)
    cpu.relative_base = 2000
    cpu.run_program()
    print(cpu.output)

    program_list_2 = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    cpu = Intcode(program_list_2)
    cpu.run_program()
    print(cpu.output)

    program_list_2 = [1102,34915192,34915192,7,4,7,99,0]
    cpu = Intcode(program_list_2)
    cpu.run_program()
    print(cpu.output)

    program_list_2 = [104,1125899906842624,99]
    cpu = Intcode(program_list_2)
    cpu.run_program()
    print(cpu.output)

    program_input = get_input('input09.txt')
    program_list_2 = program_input
    cpu = Intcode(program_list_2)
    cpu.run_program(input_int=1)
    print(cpu.output)

    program_input = get_input('input09.txt')
    program_list_2 = program_input
    cpu = Intcode(program_list_2)
    cpu.run_program(input_int=2)
    print(cpu.output)