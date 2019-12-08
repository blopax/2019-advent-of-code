
def get_input(input_path):
    with open(input_path) as f:
        input_str = f.read().strip()
    return input_str


if __name__ == '__main__':
    image_input = get_input('input08.txt')
    layers = []
    layer_size = 25 * 6

    i = 0
    while i < len(image_input):
        layers.append(image_input[i:i + layer_size])
        i += layer_size

    min_0 = layer_size + 1
    for layer in layers:
        count_0 = layer.count("0")
        if count_0 < min_0:
            min_0 = count_0
            total = layer.count("1") * layer.count("2")
    print(total)

    final_layer = list(layers[0])
    for index, pixel in enumerate(final_layer):
        if pixel == "2":
            for layer in layers:
                layer_lst = list(layer)
                if layer_lst[index] != "2":
                    final_layer[index] = layer_lst[index]
                    break

    layer_lines = []
    i = 0
    while i < layer_size:
        layer_lines.append(''.join(final_layer[i: i + 25]).replace('0', ' ').replace('1', '@'))
        i += 25
    print('\n'.join(layer_lines))

