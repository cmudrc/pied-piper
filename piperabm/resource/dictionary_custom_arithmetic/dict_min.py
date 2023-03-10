def dict_min(dict: dict):
    return min(dict, key=dict.get)


if __name__ == "__main__":
    dictionary = {'a': 1, 'b': 2}
    print(dict_min(dictionary))