def mul(main: dict, other):
    result = {}
    if isinstance(other, (int, float)):
        for key in main:
            result[key] = main[key] * other
    return result