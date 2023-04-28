from piperabm.object.delta import DeltaBool, DeltaFloat, DeltaStr


class Delta:

    def create_delta(main, other):
        result = None
        if isinstance(main, bool):
            result = DeltaBool.create_bool_delta(main, other)
        elif isinstance(main, (float, int)):
            result = DeltaFloat.create_float_delta(main, other)
        elif isinstance(main, str):
            result = DeltaStr.create_str_delta(main, other)
        elif isinstance(main, dict):
            result = Delta.create_dict_delta(main, other)
        elif isinstance(main, list):
            result = Delta.create_list_delta(main, other)
        else:
            result = None
        return result
    
    def apply_delta(main, delta):
        result = None
        if isinstance(main, bool):
            result = DeltaBool.apply_bool_delta(main, delta)
        elif isinstance(main, (float, int)):
            result = DeltaFloat.apply_float_delta(main, delta)
        elif isinstance(main, str):
            result = DeltaStr.apply_str_delta(main, delta)
        elif isinstance(main, dict):
            result = Delta.apply_dict_delta(main, delta)
        elif isinstance(main, list):
            result = Delta.apply_list_delta(main, delta)
        else:
            result = None
        return result
    
    def create_list_delta(main, other) -> list:
        pass
    
    def apply_list_delta(main: list, delta: list) -> list:
        result = main
        for delta_item in delta:
            if delta_item not in main:
                result.append(delta_item)
        return result
    
    def create_dict_delta(main: dict, other: dict) -> dict:
        delta = None
        if other is not None:
            delta = {}
            for key in main:
                main_value = main[key]
                if key in other:
                    other_value = other[key]
                    delta_val = Delta.create_delta(main_value, other_value)
                    if delta_val is not None:
                        delta[key] = delta_val
        return delta

    def apply_dict_delta(main: dict, delta: dict) -> dict:
        result = main
        for key in delta:
            delta_val = delta[key]
            if key in main:
                main_val = main[key]
                new_val = Delta.apply_delta(main_val, delta_val)
                result[key] = new_val
        return result


if __name__ == "__main__":
    #print(Delta.apply_bool_delta(main=True, delta=False))
    #print(Delta.apply_bool_delta(main=True, delta=True))
    main = {
        'a': 'a',
        'b': 2,
        'c': True,
        'd': {
            'a': 'a',
            'b': 2,
            'c': True
        },
        'e': [{'b': 2}],
    }
    delta = {
        'a': 'b',
        'b': 1,
        'c': True,
        'd': {
            'a': 'b',
            'b': 1,
            'c': True,
        },
        'e': [{'b': 3}]
    }
    print(Delta.apply_dict_delta(main, delta))