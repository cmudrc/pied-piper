def inverse_function(inverse: bool=False):
    inverse_factor = 1
    if inverse is True:
        inverse_factor *= -1
    return inverse_factor


if __name__ == "__main__":
    factor = inverse_function(False)
    print(factor)