import time


def get_dict_from_dir(direction_str):
    if direction_str[0] == 'R':
        return complex(int(direction_str[1:]), 0)
    if direction_str[0] == 'L':
        return complex(-int(direction_str[1:]), 0)
    if direction_str[0] == 'U':
        return complex(0, + int(direction_str[1:]))
    if direction_str[0] == 'D':
        return complex(0, -int(direction_str[1:]))


def get_input(map_string):
    map_list = map_string.split('\n')
    wire_instructions_0_raw = map_list[0].split(',')
    wire_instructions_1_raw = map_list[1].split(',')
    wire_instructions_0 = [get_dict_from_dir(item) for item in wire_instructions_0_raw]
    wire_instructions_1 = [get_dict_from_dir(item) for item in wire_instructions_1_raw]
    return wire_instructions_0, wire_instructions_1


def get_full_wire(wire_instructions):
    wire = [0]
    for instruction in wire_instructions:
        if instruction.real > 0:
            for i in range(int(instruction.real)):
                wire.append(wire[-1] + 1)
        if instruction.imag > 0:
            for i in range(int(instruction.imag)):
                wire.append(wire[-1] + complex(0, 1))
        if instruction.real < 0:
            for i in range(int(-instruction.real)):
                wire.append(wire[-1] - 1)
        if instruction.imag < 0:
            for i in range(int(-instruction.imag)):
                wire.append(wire[-1] - complex(0, 1))
    return wire


def get_minimum_manhattan_distance(candidates):
    minimum_manhattan = None
    for item in candidates:
        distance = int(abs(item.real) + abs(item.imag))
        if minimum_manhattan is None or distance < minimum_manhattan:
            minimum_manhattan = distance
    return minimum_manhattan


def get_min_steps(candidates, wire_0, wire_1):
    min_steps = None
    for item in candidates:
        wire_0_steps = wire_0.index(item)
        wire_1_steps = wire_1.index(item)
        total_steps = wire_0_steps + wire_1_steps
        if min_steps is None or total_steps < min_steps:
            min_steps = total_steps
    return min_steps


def full_test(map_string):
    wire_instructions_0, wire_instructions_1 = get_input(map_string)
    wire_0 = get_full_wire(wire_instructions_0)
    wire_1 = get_full_wire(wire_instructions_1)
    commons = set(wire_0) & set(wire_1) - {0}
    manhattan = get_minimum_manhattan_distance(commons)
    steps = get_min_steps(commons, wire_0, wire_1)
    return manhattan, steps


if __name__ == '__main__':
    start_time = time.time()
    
    with open('input03.txt') as f:
        map_input = f.read().strip()
    wire_instructions_a, wire_instructions_b = get_input(map_input)
    input_time = time.time()

    wire_a = get_full_wire(wire_instructions_a)
    wire_b = get_full_wire(wire_instructions_b)
    create_map_time = time.time()

    intersections = set(wire_a) & set(wire_b) - {0}
    intersections_time = time.time()

    manhattan_distance = get_minimum_manhattan_distance(intersections)
    manhattan_time = time.time()

    steps_distance = get_min_steps(intersections, wire_a, wire_b)
    steps_time = time.time()

    print(manhattan_distance)
    print(steps_distance)
    print("""
       Get input time: {}
       Create map time: {}
       Find intersections time: {}
       Manhattan time: {}
       Steps time: {}
       Total time: {}
       """.format(input_time - start_time, create_map_time - input_time, intersections_time - create_map_time,
                  manhattan_time - intersections_time, steps_time - manhattan_time, steps_time - start_time))
