from piperabm.tools.symbols import SYMBOLS


def argmax(multidimensional_list):
    """
    Find the position of the maximum value in a multidimensional list, ignoring None values.

    :param multidimensional_list: A list of lists with numerical values and possibly None values.
    :return: Tuple of indices representing the position of the maximum value.
    """
    max_value = -SYMBOLS['inf']
    max_index = (-1, -1)

    for i, sublist in enumerate(multidimensional_list):
        for j, value in enumerate(sublist):
            if value is not None and value > max_value:
                max_value = value
                max_index = (i, j)

    if max_index == (-1, -1):
        max_index = None

    return max_index


if __name__ == '__main__':
    multidimensional_list = [
        [1, None, 3],
        [4, None, 6],
        [None, 8, 5]
    ]
    print(argmax(multidimensional_list))
