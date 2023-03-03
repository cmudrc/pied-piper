from piperabm.tools.storage_custom_arithmetic import is_equal_function


def find_zeros_index(main: dict, other: dict):
    zeros_index = [] # when both dicts have zero for a key
    # find zeros and add them to the other dictionary
    for key in main:
        if main[key] == 0 and key not in other:
            other[key] = 0
    for key in other:
        if other[key] == 0 and key not in main:
            main[key] = 0
    # filter all zeros
    for key in main:
        if main[key] == 0 and other[key] == 0:
            if key not in zeros_index:
                zeros_index.append(key)
    return zeros_index

def compare_keys(main: dict, other: dict):
    shared_keys = [] # nonzeros
    uncommon_keys = {'main': [], 'other': []}
    zeros_index = find_zeros_index(main, other)
    # compare
    for key in main:
        if key in other:
            if key not in shared_keys and key not in zeros_index:
                shared_keys.append(key)
    for key in main:
        if key not in other:
            if key not in uncommon_keys['main']:
                uncommon_keys['main'].append(key)
    for key in other:
        if key not in main:
            if key not in uncommon_keys['other']:
                uncommon_keys['other'].append(key)
    return shared_keys, uncommon_keys

def compare_common_vals(main: dict, other: dict):
    shared_keys, uncommon_keys = compare_keys(main, other)
    result_list = []
    result = None
    for key in shared_keys:
        result_list.append(is_equal_function(main[key], other[key]))
    if False in result_list:
        result = False
    else:
        result = True
    #print(shared_keys)
    return result

def compare_vals(main: dict, other: dict):
    result = None
    shared_keys, uncommon_keys = compare_keys(main, other)
    if len(uncommon_keys['main']) > 0 or len(uncommon_keys['other']) > 0:
        result = False
    else:
        result = compare_common_vals(main, other)
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 3, 'c': 4, 'd': 0}
    shared_keys, uncommon_keys = compare_keys(main, other)
    print(shared_keys, uncommon_keys)