try: from storage_custom_arithmetic import add_function
except: from .storage_custom_arithmetic import add_function
try: from .dict_compare import compare_keys
except: from dict_compare import compare_keys


def dict_add(main: dict, other, max=None):
    result = {}
    remaining = {}
    if isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            if max is None: max_amount = None
            else: max_amount = max[key]
            result[key], remaining[key] = add_function(
                amount=other[key],
                current_amount=main[key],
                max_amount=max_amount
            )
        for key in uncommon_keys['main']:
            result[key] = main[key]
            remaining[key] = 0
        for key in uncommon_keys['other']:
            result[key] = other[key]
            remaining[key] = 0
    return result, remaining


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 2, 'c': 3}
    max = {'b': 3}
    result, remaining = dict_add(main, other, max)
    #result = truediv(main, 2)
    print(result, remaining)