def compare_keys(main: dict, other: dict):
    shared_keys = []
    uncommon_keys = {'main': [], 'other': []}
    for key in main:
        if key in other:
            if key not in shared_keys:
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

def compare_val(main: dict, other: dict):
    shared_keys, uncommon_keys = compare_keys(main, other)
    result_list = []
    result = None
    for key in shared_keys:
        main_val = main[key]
        if main_val == 0:
            result_list.append(True)
        else:
            if main[key] == other[key]:
                result_list.append(True)
            else:
                result_list.append(False)
    if False in result_list:
        result = False
    else:
        result = True
    return result


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 3, 'c': 4}
    shared_keys, uncommon_keys = compare_keys(main, other)
    print(shared_keys, uncommon_keys)