try: from .functions import compare_keys
except: from functions import compare_keys


def truediv(main: dict, other):
    result = {}
    if isinstance(other, (int, float)):
        for key in main:
            result[key] = main[key] / other
    elif isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            result[key] = main[key] / other[key]
        for key in uncommon_keys['other']:
            result[key] = 0
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 2, 'c': 2}
    result = truediv(main, other)
    #result = truediv(main, 2)
    print(result)