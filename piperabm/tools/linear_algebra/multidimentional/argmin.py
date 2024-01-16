from piperabm.tools.symbols import SYMBOLS


def argmin(multidimensional_list):
    """
    Find the position of the minimum value in a multidimensional list, ignoring None values.

    :param multidimensional_list: A list of lists with numerical values and possibly None values.
    :return: Tuple of indices representing the position of the minimum value.
    """
    min_value = SYMBOLS['inf']
    min_index = (-1, -1)

    for i, sublist in enumerate(multidimensional_list):
        for j, value in enumerate(sublist):
            if value is not None and value < min_value:
                min_value = value
                min_index = (i, j)

    if min_index == (-1, -1):
        min_index = None

    return min_index


if __name__ == '__main__':
    multidimensional_list = [
        [1, None, 3],
        [4, None, 6],
        [None, 8, 5]
    ]
    print(argmin(multidimensional_list))
