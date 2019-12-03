import numpy as np
import copy
import time


def get_dict_from_dir(direction_str):
    direction_dict = dict()
    direction_dict['side'] = direction_str[0]
    direction_dict['distance'] = int(direction_str[1:])
    return direction_dict


def get_input(map_input):
    map_list = map_input.split('\n')
    wire0_raw = map_list[0].split(',')
    wire1_raw = map_list[1].split(',')
    wire0 = [get_dict_from_dir(item) for item in wire0_raw]
    wire1 = [get_dict_from_dir(item) for item in wire1_raw]
    return wire0, wire1


def get_wire_size(wire):
    right, left, up, down = 0, 0, 0, 0
    horizontal, vertical = 0, 0
    for instruction in wire:
        if instruction['side'] == 'R':
            horizontal += instruction['distance']
        elif instruction['side'] == 'L':
            horizontal -= instruction['distance']
        elif instruction['side'] == 'U':
            vertical -= instruction['distance']
        elif instruction['side'] == 'D':
            vertical += instruction['distance']
        if horizontal > right:
            right = horizontal
        elif -horizontal > left:
            left = -horizontal
        elif vertical > down:
            down = vertical
        elif -vertical > up:
            up = -vertical
    return right, left, up, down


def get_map_size(wire0, wire1):
    wire0_right, wire0_left, wire0_up, wire0_down = get_wire_size(wire0)
    wire1_right, wire1_left, wire1_up, wire1_down = get_wire_size(wire1)
    map_right = max(wire0_right, wire1_right)
    map_left = max(wire0_left, wire1_left)
    map_up = max(wire0_up, wire1_up)
    map_down = max(wire0_down, wire1_down)
    map_horizontal = map_right + map_left + 1
    map_vertical = map_up + map_down + 1
    initial_position = (map_up, map_left)
    return map_horizontal, map_vertical, initial_position


def draw_line(w_map, instruction, position, value):
    position = list(position)
    position_up = position[0]
    position_down = position[0]
    position_left = position[1]
    position_right = position[1]
    if instruction['side'] == 'U':
        position_up = position[0] - instruction['distance']
        position[0] -= instruction['distance']
        position_right += 1
    elif instruction['side'] == 'D':
        position_up += 1
        position_down = position[0] + instruction['distance'] + 1
        position[0] += instruction['distance']
        position_right += 1
    elif instruction['side'] == 'L':
        position_left = position[1] - instruction['distance']
        position[1] -= instruction['distance']
        position_down += 1
    elif instruction['side'] == 'R':
        position_left += 1
        position_right = position[1] + instruction['distance'] + 1
        position[1] += instruction['distance']
        position_down += 1
    w_map[position_up:position_down, position_left:position_right] += value
    return tuple(position)


def draw_wire(w_map, wire, position, value):
    for instruction in wire:
        position = draw_line(w_map, instruction, position, value)


def draw_initial_map(wire0, wire1):
    map_horizontal, map_vertical, initial_position = get_map_size(wire0, wire1)
    w_map = np.zeros((map_vertical, map_horizontal))
    w_map[initial_position] = -1
    return w_map, initial_position


def get_min_manhattan_distance(contact, position):
    min_distance, closest_contact = None, None
    for item in contact:
        dist = abs(item[0] - position[0]) + abs(item[1] - position[1])
        if min_distance is None or dist < min_distance:
            min_distance = dist
            closest_contact = item
    return min_distance, closest_contact


def step_is_in(position, new, final_position):
    for i in [0, 1]:
        if final_position[i] == new[i] and final_position[i] == position[i]:
            if (position[1 - i] < final_position[1 - i] <= new[1 - i] or
                    new[1 - i] <= final_position[1 - i] < position[1 - i]):
                return True
    return False


def get_steps(wire, initial_position, item):
    steps = 0
    position = list(initial_position)
    final_position = list(item)
    for instruction in wire:
        new = copy.copy(position)
        if instruction['side'] == 'U':
            new[0] = position[0] - instruction['distance']
        elif instruction['side'] == 'D':
            new[0] = position[0] + instruction['distance']
        elif instruction['side'] == 'L':
            new[1] = position[1] - instruction['distance']
        elif instruction['side'] == 'R':
            new[1] = position[1] + instruction['distance']
        if step_is_in(position, new, final_position):
            steps += abs(final_position[0] - position[0]) + abs(final_position[1] - position[1])
            break
        else:
            steps += instruction['distance']
            position = new
    return steps


def get_min_combined_steps(contact, position, wire0, wire1):
    min_combined_steps, closest_steps = None, None
    for item in contact:
        wire0_steps = get_steps(wire0, position, item)
        wire1_steps = get_steps(wire1, position, item)
        combined_steps = wire0_steps + wire1_steps
        if min_combined_steps is None or combined_steps < min_combined_steps:
            min_combined_steps = combined_steps
            closest_steps = item
    return min_combined_steps, closest_steps


def full_test(map_input):
    w_instructions_0, w_instructions_1 = get_input(map_input)
    w_map, initial_position = draw_initial_map(w_instructions_0, w_instructions_1)
    draw_wire(w_map, w_instructions_0, initial_position, 1)
    draw_wire(w_map, w_instructions_1, initial_position, 2)
    y, x = np.where(w_map == 3)
    contact = zip(y, x)
    manhattan_distance, _ = get_min_manhattan_distance(contact, initial_position)
    contact = zip(y, x)
    steps, _ = get_min_combined_steps(contact, initial_position, w_instructions_0, w_instructions_1)
    return manhattan_distance, steps


if __name__ == '__main__':
    start_time = time.time()

    with open('input03.txt') as f:
        map_string = f.read().strip()

    wire_a, wire_b = get_input(map_string)
    # wire_a, wire_b = get_input('input03_test.txt')
    input_time = time.time()

    wire_map, init_position = draw_initial_map(wire_a, wire_b)
    draw_wire(wire_map, wire_a, init_position, 1)
    draw_wire(wire_map, wire_b, init_position, 2)
    create_map_time = time.time()

    index_y, index_x = np.where(wire_map == 3)
    wire_contact = zip(index_y, index_x)
    get_contact_time = time.time()

    min_manhattan_distance, closest = get_min_manhattan_distance(wire_contact, init_position)
    print(min_manhattan_distance, closest)
    manhattan_time = time.time()

    min_steps, closest = get_min_combined_steps(wire_contact, init_position, wire_a, wire_b)
    print(min_steps, closest)
    steps_time = time.time()

    print("""
    Get input time: {}
    Create map time: {}
    Find intersections time: {}
    Manhattan time: {}
    Steps time: {}
    Total Time: {}
    """.format(input_time - start_time, create_map_time - input_time, get_contact_time - create_map_time,
               manhattan_time - get_contact_time, steps_time - manhattan_time, steps_time - start_time))
