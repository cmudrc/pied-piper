def dict_max(dict: dict):
    return max(dict, key=dict.get)


if __name__ == "__main__":
    dictionary = {'a': 1, 'b': 2}
    print(dict_max(dictionary))