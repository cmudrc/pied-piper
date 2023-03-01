try: from .compare_keys import compare_keys
except: from compare_keys import compare_keys


def add(main: dict, other):
    result = {}
    if isinstance(other, dict):
        shared_keys, uncommon_keys = compare_keys(main, other)
        for key in shared_keys:
            result[key] = main[key] + other[key]
        for key in uncommon_keys['main']:
            result[key] = main[key]
        for key in uncommon_keys['other']:
            result[key] = other[key]
    return result