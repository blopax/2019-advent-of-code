def count_passwords(lower_range, upper_range, remove_triple=False):
    count = 0
    for candidate in range(lower_range, upper_range + 1):
        candidate_str = str(candidate)
        ascending = True
        double = [0] * 10

        for index in range(5):
            if int(candidate_str[index]) > int(candidate_str[index + 1]):
                ascending = False
                break
            if candidate_str[index] == candidate_str[index + 1]:
                double[int(candidate_str[index]) - 1] += 1

        if not remove_triple and ascending and sum(double) > 0:
            count += 1

        if remove_triple and ascending and 1 in double:
            count += 1
    return count


if __name__ == '__main__':
    input_bottom = 246540
    input_top = 787419

    all_count = count_passwords(input_bottom, input_top)
    no_triple_count = count_passwords(input_bottom, input_top, remove_triple=True)

    print(all_count, no_triple_count)
