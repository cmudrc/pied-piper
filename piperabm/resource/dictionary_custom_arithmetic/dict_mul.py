try: from storage_custom_arithmetic import mul_function
except: from .storage_custom_arithmetic import mul_function
try: from .dict_compare import compare_keys
except: from dict_compare import compare_keys


def dict_mul(main: dict, other, max=None, min=None):
    result = {}
    remaining = {}
    if isinstance(other, (int, float)):
        for key in main:
            if max is None: max_amount = None
            elif key in max: max_amount = max[key]
            else: max_amount = None
            if min is None: min_amount = 0
            elif key in min: min_amount = min[key]
            else: min_amount = 0
            result[key], remaining[key] = mul_function(main[key], other, max_amount, min_amount)
    elif isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            if max is None: max_amount = None
            else: max_amount = max[key]
            if min is None: min_amount = 0
            else: min_amount = min[key]
            result[key], remaining[key] = mul_function(main[key], other[key], max_amount, min_amount)
        for key in uncommon_keys['main']:
            result[key] = main[key]
            #remaining[key] = 0
        for key in uncommon_keys['other']:
            result[key] = 0
            #remaining[key] = other[key]
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 0.2}
    min = {'b': 1}
    max = {'b': 3}
    #result = dict_mul(main, other)
    result = dict_mul(main, other, max, min)
    print(result)