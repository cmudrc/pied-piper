from piperabm.tools.custom_arithmetics import sub_function
try: from .dict_compare import compare_keys
except: from dict_compare import compare_keys


def sub(main: dict, other, min=None):
    result = {}
    remaining = {}
    if isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            if min is None:
                min_amount = 0
            else:
                min_amount = min[key]
            result[key], remaining[key] = sub_function(
                amount=other[key],
                current_amount=main[key],
                min_amount=min_amount
            )
        for key in uncommon_keys['main']:
            result[key] = main[key]
            remaining[key] = 0
        for key in uncommon_keys['other']:
            result[key] = 0
            remaining[key] = other[key]
    return result, remaining


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 2, 'c': 3}
    min = {'b': 1}
    result, remaining = sub(main, other, min)
    #result = truediv(main, 2)
    print(result, remaining)