from piperabm.object.delta.simple_variables.bool import DeltaBool
from piperabm.object.delta.simple_variables.float import DeltaFloat
from piperabm.object.delta.simple_variables.str import DeltaStr


class Delta:
    """
    Create and apply delta for variables
    """

    def create(main, other):
        """ Create delta for variables """
        result = None
        if isinstance(main, bool) or isinstance(other, bool):
            result = DeltaBool.create(main, other)
        elif isinstance(main, (float, int)) or isinstance(other, (float, int)):
            result = DeltaFloat.create(main, other)
        elif isinstance(main, str) or isinstance(other, str):
            result = DeltaStr.create(main, other)
        elif isinstance(main, dict) or isinstance(other, dict):
            result = DeltaDict.create(main, other)
        elif isinstance(main, list) or isinstance(other, list):
            result = DeltaList.create(main, other)
        return result
    
    def apply(main, delta):
        """ Apply delta to variables """
        result = None
        if isinstance(main, bool) or isinstance(delta, bool):
            result = DeltaBool.apply(main, delta)
        elif isinstance(main, (float, int)) or isinstance(delta, (float, int)):
            result = DeltaFloat.apply(main, delta)
        elif isinstance(main, str) or isinstance(delta, str):
            result = DeltaStr.apply(main, delta)
        elif isinstance(main, dict) or isinstance(delta, dict):
            result = DeltaDict.apply(main, delta)
        elif isinstance(main, list) or isinstance(delta, list):
            result = DeltaList.apply(main, delta)
        return result


class DeltaDict:
    """
    Create and apply delta for dictionary variable
    """

    def create(main: dict, other: dict) -> dict:
        """ Create delta for dictionary variable """
        delta = None
        if main is not None:
            if other is not None:
                delta = {}
                for key in other:
                    other_value = other[key]
                    if key in main:
                        main_value = main[key]
                    else:
                        main_value = None
                    delta_val = Delta.create(main_value, other_value)
                    if delta_val is not None:
                        delta[key] = delta_val
                if len(delta) == 0:
                    delta = None
        else:  # when *main* is None
            delta = other
        return delta

    def apply(main: dict, delta: dict) -> dict:
        """ Apply delta to dictionary variable """
        if main is not None:
            other = main
            if delta is not None:
                for key in delta:
                    delta_val = delta[key]
                    if key in main:
                        main_val = main[key]
                        new_val = Delta.apply(main_val, delta_val)
                    else:
                        new_val = delta_val
                    other[key] = new_val
        else:  # when *main* is None
            other = delta
        return other
    

class DeltaList:
    """
    Create and apply delta for list variable
    work with lists after converting them into dictionaries
    """

    def create(main: list, other: list) -> list:
        """ Create delta for list variable """
        delta = None
        if main is not None:
            if other is not None:
                main_dict = DeltaList.list_to_dict(main)
                other_dict = DeltaList.list_to_dict(other)
                delta_dict = DeltaDict.create(main_dict, other_dict)
                delta = DeltaList.dict_to_list(delta_dict)
            else:
                delta = main
        else:
            delta = other
        return delta
    
    def apply(main: list, delta: list) -> list:
        """ Apply delta to list variable """
        if delta == []: delta = None  # empty and None are the same
        if main is not None:
            #other = main
            if delta is not None:
                delta_dict = DeltaList.list_to_dict(delta)
                main_dict = DeltaList.list_to_dict(main)
                other_dict = DeltaDict.apply(main_dict, delta_dict)
                other = DeltaList.dict_to_list(other_dict)
            else:  # when *delta* is None
                other = main
        else:  # when *main* is None
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


if __name__ == '__main__':
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
    result = Delta.apply(main, delta)
    print(result)