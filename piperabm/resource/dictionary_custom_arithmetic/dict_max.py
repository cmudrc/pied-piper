def dict_max(dictionary: dict):
    """
    Return key that has max value
    """
    result = None
    for key in dictionary:
        if dictionary[key] is None:
            result = key
            break
    if result is None: # no None in dictionary
        result = max(dictionary, key=dictionary.get)
    return result


if __name__ == "__main__":
    dictionary = {'a': 1, 'b': 2}
    print(dict_max(dictionary))