from piperabm.tools.storage_custom_arithmetic import mul_function
try: from .dict_compare import compare_keys
except: from dict_compare import compare_keys


def dict_mul(main: dict, other, max=None):
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
            result[key], _ = mul_function(main[key], other[key], max_amount)
        for key in uncommon_keys['main']:
            result[key] = main[key]
        for key in uncommon_keys['other']:
            result[key] = 0
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 2}
    #result = dict_mul(main, other)
    result = dict_mul(main, 2)
    print(result)