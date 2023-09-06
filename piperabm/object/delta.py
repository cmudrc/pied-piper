from piperabm.object.delta_var import DeltaBool, DeltaFloat, DeltaStr


class Delta:
    """
    Create and apply delta for variables
    """

    def create_delta(main, other):
        result = None
        if isinstance(main, bool) or isinstance(other, bool):
            result = DeltaBool.create_bool_delta(main, other)
        elif isinstance(main, (float, int)) or isinstance(other, (float, int)):
            result = DeltaFloat.create_float_delta(main, other)
        elif isinstance(main, str) or isinstance(other, str):
            result = DeltaStr.create_str_delta(main, other)
        elif isinstance(main, dict) or isinstance(other, dict):
            result = Delta.create_dict_delta(main, other)
        elif isinstance(main, list) or isinstance(other, list):
            result = Delta.create_list_delta(main, other)
        return result
    
    def apply_delta(main, delta):
        result = None
        if isinstance(main, bool) or isinstance(delta, bool):
            result = DeltaBool.apply_bool_delta(main, delta)
        elif isinstance(main, (float, int)) or isinstance(delta, (float, int)):
            result = DeltaFloat.apply_float_delta(main, delta)
        elif isinstance(main, str) or isinstance(delta, str):
            result = DeltaStr.apply_str_delta(main, delta)
        elif isinstance(main, dict) or isinstance(delta, dict):
            result = Delta.apply_dict_delta(main, delta)
        elif isinstance(main, list) or isinstance(delta, dict):
            result = Delta.apply_list_delta(main, delta)
        return result
    
    def create_list_delta(main: list, other: list) -> list:
        delta = None
        if main is not None:
            if other is not None:
                main_dict = list_to_dict(main)
                other_dict = list_to_dict(other)
                delta = Delta.create_dict_delta(main_dict, other_dict)
            else:
                delta = main
        else:
            delta = other
        return delta
    
    def apply_list_delta(main: list, delta: dict) -> list:
        if main is not None:
            other = main
            if delta is not None:
                pass
            else:
                other = main
        else:
            other = delta
        return other
    
    def create_dict_delta(main: dict, other: dict) -> dict:
        delta = None
        if main is not None:
            if other is not None:
                delta = {}
                for key in main:
                    main_value = main[key]
                    if key in other:
                        other_value = other[key]
                        delta_val = Delta.create_delta(main_value, other_value)
                        if delta_val is not None:
                            delta[key] = delta_val
                if len(delta) == 0:
                    delta = None
        else:
            delta = other
        return delta

    def apply_dict_delta(main: dict, delta: dict) -> dict:
        if main is not None:
            other = main
            if delta is not None:
                for key in delta:
                    delta_val = delta[key]
                    if key in main:
                        main_val = main[key]
                        new_val = Delta.apply_delta(main_val, delta_val)
                    else:
                        new_val = delta_val
                    other[key] = new_val
        else:
            other = delta
        return other


def list_to_dict(input: list) -> dict:
    """ Convert list to dictionary """
    result = {}
    for i, item in enumerate(input):
        result[i] = item
    return result


def dict_to_list(input: dict) -> list:
    """ Convert dictionary to list """
    result = []
    for i in input:
        result.append(input[i])
    return result


if __name__ == "__main__":
    '''
    main = {
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
    '''
    ls_old = [3, True, 'Peter']
    dc_old = list_to_dict(ls_old)
    
    ls_new = [2, False, 'John']
    dc_new = list_to_dict(ls_new)
    print(dc_new)
    #print(Delta.create_dict_delta(dc_old, dc_new))
    #print(Delta.create_list_delta(ls_old, ls_new))