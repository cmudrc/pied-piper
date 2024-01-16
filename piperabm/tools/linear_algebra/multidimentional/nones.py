def nones(size):
    """
    Create a multidimensional list of a given size filled with None values.

    :param size: A tuple representing the dimensions of the list (rows, columns).
    :return: A multidimensional list filled with None values.
    """
    return [[None for _ in range(size[1])] for _ in range(size[0])]


if __name__ == '__main__':
    size = [2, 3]
    ls = nones(size)
    print(ls)
