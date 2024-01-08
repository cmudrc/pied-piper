from copy import deepcopy

from piperabm.object.delta.simple_variables.bool import DeltaBool
from piperabm.object.delta.simple_variables.float import DeltaFloat
from piperabm.object.delta.simple_variables.str import DeltaStr


class Delta:
    """
    Create and apply delta for variables
    """

    def create(old_variable, new_variable):
        """ Create delta for variables """
        result = None
        if isinstance(old_variable, bool) or isinstance(new_variable, bool):
            result = DeltaBool.create(old_variable, new_variable)
        elif isinstance(old_variable, (float, int)) or isinstance(new_variable, (float, int)):
            result = DeltaFloat.create(old_variable, new_variable)
        elif isinstance(old_variable, str) or isinstance(new_variable, str):
            result = DeltaStr.create(old_variable, new_variable)
        elif isinstance(old_variable, dict) or isinstance(new_variable, dict):
            result = DeltaDict.create(old_variable, new_variable)
        elif isinstance(old_variable, list) or isinstance(new_variable, list):
            result = DeltaList.create(old_variable, new_variable)
        return result
    
    def apply(old_variable, delta):
        """ Apply delta to variables """
        result = None
        if isinstance(old_variable, bool) or isinstance(delta, bool):
            result = DeltaBool.apply(old_variable, delta)
        elif isinstance(old_variable, (float, int)) or isinstance(delta, (float, int)):
            result = DeltaFloat.apply(old_variable, delta)
        elif isinstance(old_variable, str) or isinstance(delta, str):
            result = DeltaStr.apply(old_variable, delta)
        elif isinstance(old_variable, dict) or isinstance(delta, dict):
            result = DeltaDict.apply(old_variable, delta)
        elif isinstance(old_variable, list) or isinstance(delta, list):
            result = DeltaList.apply(old_variable, delta)
        return result


class DeltaDict:
    """
    Create and apply delta for dictionary variable
    """

    def create(old_variable: dict, new_variable: dict) -> dict:
        """ Create delta for dictionary variable """
        delta = None
        if old_variable is not None and len(old_variable) != 0:
            if new_variable is not None:
                delta = {}
                for key in new_variable:
                    new_variable_value = new_variable[key]
                    if key in old_variable:
                        old_variable_value = old_variable[key]
                    else:
                        old_variable_value = None
                    delta_val = Delta.create(old_variable_value, new_variable_value)
                    if delta_val is not None and \
                        delta_val != {} and \
                        delta_val != []:
                        delta[key] = delta_val
                    #delta[key] = delta_val
        else:  # when *old_variable* is None
            delta = deepcopy(new_variable)
        return delta

    def apply(old_variable: dict, delta: dict) -> dict:
        """ Apply delta to dictionary variable """
        if old_variable is not None:
            new_variable = deepcopy(old_variable)
            if delta is not None:
                for key in delta:
                    delta_val = delta[key]
                    if key in old_variable:
                        old_variable_val = old_variable[key]
                        new_val = Delta.apply(old_variable_val, delta_val)
                    else:
                        new_val = delta_val
                    new_variable[key] = new_val
        else:  # when *old_variable* is None
            new_variable = deepcopy(delta)
        return new_variable
    

class DeltaList:
    """
    Create and apply delta for list variable
    work with lists after converting them into dictionaries
    """

    def create(old_variable: list, new_variable: list) -> list:
        """ Create delta for list variable """
        delta = None
        if old_variable is not None:
            if new_variable is not None:
                old_variable_dict = DeltaList.list_to_dict(old_variable)
                new_variable_dict = DeltaList.list_to_dict(new_variable)
                delta_dict = DeltaDict.create(old_variable_dict, new_variable_dict)
                delta = DeltaList.dict_to_list(delta_dict)
            else:
                delta = old_variable
        else:
            delta = deepcopy(new_variable)
        return delta
    
    def apply(old_variable: list, delta: list) -> list:
        """ Apply delta to list variable """
        if delta == []: delta = None  # empty and None are the same
        if old_variable is not None:
            #new_variable = old_variable
            if delta is not None:
                delta_dict = DeltaList.list_to_dict(delta)
                old_variable_dict = DeltaList.list_to_dict(old_variable)
                new_variable_dict = DeltaDict.apply(old_variable_dict, delta_dict)
                new_variable = DeltaList.dict_to_list(new_variable_dict)
            else:  # when *delta* is None
                new_variable = old_variable
        else:  # when *old_variable* is None
            new_variable = deepcopy(delta)
        return new_variable
    
    def list_to_dict(input: list) -> dict:
        """ Convert list to dictionary """
        result = {}
        for i, item in enumerate(input):
            result[i] = item
        return result

    def dict_to_list(input: dict) -> list:
        """ Convert dictionary to list """
        result = []
        if input is not None:
            for i in input:
                result.append(input[i])
        return result


if __name__ == '__main__':
    old_variable = {
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
    delta = Delta.apply(old_variable, delta)
    print(delta)