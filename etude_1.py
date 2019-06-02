"""
Exercise #1

"""


def get_number_of_living_neighbors(
        data_set: (list, tuple), point: tuple) -> int:
    """
    Get number of living neighbor-points avoiding point
    1 2 3
    4 * 5
    6 7 8
    where * - our point

    :param data_set: list of living points
    :param point: current point

    :return: number of alive points
    """

    result = 0
    x_min, x_max = point[0] - 1, point[0] + 1
    y_min, y_max = point[1] - 1, point[1] + 1

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) in data_set:
                result += 1

    if point in data_set:
        result -= 1

    return result


def next_generation(data_set: (list, tuple)) -> tuple:
    """
    Create the next-generation

    :param data_set: current generation

    :return: the next-generation
    """

    # -1 and +1 - additional cells
    min_x = min(x for x, y in data_set) - 1
    max_x = max(x for x, y in data_set) + 1
    min_y = min(y for x, y in data_set) - 1
    max_y = max(y for x, y in data_set) + 1

    new_result = []

    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            number_of_living_neighbors = get_number_of_living_neighbors(
                data_set, (x, y))
            if (x, y) in data_set:
                if number_of_living_neighbors in (2, 3):
                    new_result.append((x, y))
            elif number_of_living_neighbors == 3:
                new_result.append((x, y))

    return tuple(new_result)


def show_result(data_set: (list, tuple)) -> None:
    """
    Function for printing data set

    :param data_set: generation

    :return: None
    """

    min_x = min(x for x, y in data_set)
    max_x = max(x for x, y in data_set)
    min_y = min(y for x, y in data_set)
    max_y = max(y for x, y in data_set)

    for y in range(max_y, min_y - 1, -1):
        line = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in data_set:
                line += 'X'
            else:
                line += '.'
        print(line)


if __name__ == "__main__":
    # a couple of checking
    test_data_set = [(-1, 0), (0, 0), (1, 0)]
    result = get_number_of_living_neighbors(test_data_set, test_data_set[0])

    assert get_number_of_living_neighbors(test_data_set, test_data_set[0]) == 1
    assert get_number_of_living_neighbors(test_data_set, test_data_set[1]) == 2
    assert get_number_of_living_neighbors(test_data_set, test_data_set[2]) == 1

    NUMBER_OF_GENERATION = 15

    # leave point
    start_data = [
        (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
    ]

    data = start_data
    print('Generation # 1')
    show_result(start_data)
    print('\n')

    for generation in range(2, NUMBER_OF_GENERATION + 1):
        print('Generation # %s' % generation)
        data = next_generation(data)
        show_result(data)
        print('\n' * 2)

