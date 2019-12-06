

class Node:
    def __init__(self, name, parent=None, is_child=False):
        self.name = name
        self.parent = parent
        self.is_child = is_child
        self.counted = False


class Map:
    def __init__(self, lines_list):
        self.lines_list = lines_list
        self.nodes_list = []
        self.nodes_names_list = []

    def process_lines(self):
        for line in self.lines_list:
            self.process_line(line)

    def process_line(self, line):
        parent, child = line.split(')')
        if parent not in self.nodes_names_list:
            self.nodes_list.append(Node(parent))
            self.nodes_names_list.append(parent)
        else:
            self.update_node(name=parent, parent=None, is_child=False)

        if child not in self.nodes_names_list:
            self.nodes_list.append(Node(child, parent=parent, is_child=True))
            self.nodes_names_list.append(child)
        else:
            self.update_node(name=child, parent=parent, is_child=True)

    def update_node(self, name, parent, is_child):
        node = self.get_node(name=name)
        if parent is not None:
            if node.parent is not None:
                print(node.name, node.parent, parent)
            node.parent = parent
        if node.is_child is True and is_child is False:
            node.is_child = False

    def get_node(self, name):
        for node in self.nodes_list:
            if node.name == name:
                return node

    def orbit_count_checksum(self):
        count = 0
        for node in self.nodes_list:
            count += self.new_path_to_root(node)
        return count

    def new_path_to_root(self, node):
        count = 0
        while node.parent is not None:
            node = self.get_node(node.parent)
            count += 1
        return count

    def get_parent_nodes_that_are_not_in_common(self, node1_name, node2_name):
        node1 = self.get_node(node1_name)
        node2 = self.get_node(node2_name)
        node1_parents = []
        node2_parents = []
        while node1.parent is not None:
            node1 = self.get_node(node1.parent)
            node1_parents.append(node1.name)
        while node2.parent is not None:
            node2 = self.get_node(node2.parent)
            node2_parents.append(node2.name)
        return set(node1_parents) ^ set(node2_parents)


if __name__ == '__main__':
    input_path = 'input06.txt'
    with open(input_path) as f:
        input_list = f.readlines()
    lines = [item.strip() for item in input_list]
    # print(lines_list)

    santa_map = Map(lines)
    santa_map.process_lines()
    orbit_count_checksum = santa_map.orbit_count_checksum()
    print(orbit_count_checksum)
    answer_set = santa_map.get_parent_nodes_that_are_not_in_common("YOU", "SAN")
    print(len(answer_set))
