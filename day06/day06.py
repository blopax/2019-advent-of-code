import time


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent


class Map:
    def __init__(self, lines_list):
        self.lines_list = lines_list
        self.nodes_list = set()
        self.nodes_names_list = set()

    def process_lines(self):
        for line in self.lines_list:
            self.process_line(line)

    def process_line(self, line):
        parent_name, child_name = line.split(')')
        if parent_name not in self.nodes_names_list:
            parent = Node(parent_name)
        else:
            parent = self.get_node(parent_name)
        if child_name not in self.nodes_names_list:
            child = Node(child_name)
        else:
            child = self.get_node(child_name)
        child.parent = parent

        self.nodes_list = self.nodes_list | {parent, child}
        self.nodes_names_list = self.nodes_names_list | {parent_name, child_name}

    def get_node(self, name):
        for node in self.nodes_list:
            if node.name == name:
                return node

    def orbit_count_checksum(self):
        count = 0
        for node in self.nodes_list:
            count += self.new_path_to_root(node)
        return count

    @staticmethod
    def new_path_to_root(node):
        count = 0
        while node.parent is not None:
            node = node.parent
            count += 1
        return count

    def get_parent_nodes_that_are_not_in_common(self, node1_name, node2_name):
        node1 = self.get_node(node1_name)
        node2 = self.get_node(node2_name)
        node1_parents = []
        node2_parents = []
        while node1.parent is not None:
            node1 = node1.parent
            node1_parents.append(node1.name)
        while node2.parent is not None:
            node2 = node2.parent
            node2_parents.append(node2.name)
        return set(node1_parents) ^ set(node2_parents)


if __name__ == '__main__':
    start_time = time.time()

    input_path = 'input06.txt'
    with open(input_path) as f:
        input_list = f.readlines()
    lines = [item.strip() for item in input_list]
    input_time = time.time()

    santa_map = Map(lines)
    santa_map.process_lines()
    map_time = time.time()
    
    orbit_count_checksum = santa_map.orbit_count_checksum()
    check_time = time.time()

    orbital_transfers = santa_map.get_parent_nodes_that_are_not_in_common("YOU", "SAN")
    end_time = time.time()

    output = """
    Input treatment time: {}
    Map creation time: {}
    Orbit count checksum: {} (time needed {}s)
    Minimum orbital transfer required: {} (time needed {}s)
    Total Time: {}
    """.format(input_time - start_time, map_time - input_time, orbit_count_checksum, check_time - map_time,
               len(orbital_transfers), end_time - check_time, end_time - start_time)
    print(output)
