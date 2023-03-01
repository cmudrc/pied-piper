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


if __name__ == "__main__":
    main = {'a': 1, 'b': 2}
    other = {'b': 3, 'c': 4}
    shared_keys, uncommon_keys = compare_keys(main, other)
    print(shared_keys, uncommon_keys)