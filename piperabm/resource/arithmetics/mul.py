try: from .functions import mul_function, compare_keys
except: from functions import mul_function, compare_keys


def mul(main: dict, other, max=None):
    result = {}
    if isinstance(other, (int, float)):
        for key in main:
            if max is None: max_amount = None
            else: max_amount = max[key]
            result[key], _ = mul_function(main[key], other, max_amount)
    elif isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            if max is None: max_amount = None
            else: max_amount = max[key]
            result[key] = mul_function(main[key], other[key], max_amount)
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 2}
    result = mul(main, other)
    #result = truediv(main, 2)
    print(result)