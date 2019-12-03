import math


def get_modules_mass(input_path):
    with open(input_path) as f:
        input_list = f.readlines()
    return [int(x) for x in input_list]


def fuel_for_mass(mass):
    return max(0, int(math.floor(mass/3.0) - 2))


def fuel_for_module(module_mass):
    total = 0
    added_fuel = fuel_for_mass(module_mass)
    while added_fuel > 0:
        total += added_fuel
        added_fuel = fuel_for_mass(added_fuel)
    return total


def sum_fuel(modules, fuel_func):
    total = 0
    for module_mass in modules:
        total += fuel_func(module_mass)
    return total


if __name__ == '__main__':
    modules_mass_list = get_modules_mass('input01.txt')
    print("Sum of fuel requirement part one: {}".format(sum_fuel(modules_mass_list, fuel_for_mass)))
    print("Sum of fuel requirement part two: {}".format(sum_fuel(modules_mass_list, fuel_for_module)))
