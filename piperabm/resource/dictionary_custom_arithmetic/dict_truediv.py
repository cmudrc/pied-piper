try: from storage_custom_arithmetic import truediv_function
except: from .storage_custom_arithmetic import truediv_function
try: from .dict_compare import compare_keys
except: from dict_compare import compare_keys


def dict_truediv(main: dict, other, max=None, min=None):
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
            result[key], remaining[key] = truediv_function(main[key], other, max_amount, min_amount)
    elif isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            if max is None: max_amount = None
            else: max_amount = max[key]
            if min is None: min_amount = 0
            else: min_amount = min[key]
            result[key], remaining[key] = truediv_function(main[key], other[key], max_amount, min_amount)
        for key in uncommon_keys['main']:
            result[key] = None
            #remaining[key] = 0
        for key in uncommon_keys['other']:
            result[key] = 0
            #remaining[key] = other[key]
    return result

'''
def dict_truediv(main: dict, other):
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
'''


if __name__ == "__main__":
    main = {'a': 1, 'b': 4}
    other = {'b': 2, 'c': 2}
    result = dict_truediv(main, other)
    #result = truediv(main, 2)
    print(result)