from piperabm.pure_object.delta.variables.bool import DeltaBool
from piperabm.pure_object.delta.variables.float import DeltaFloat
from piperabm.pure_object.delta.variables.str import DeltaStr
from piperabm.pure_object.delta.variables.dict import DeltaDict
from piperabm.pure_object.delta.variables.list import DeltaList


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
        elif isinstance(main, list) or isinstance(delta, dict):
            result = DeltaList.apply(main, delta)
        return result


if __name__ == "__main__":
    
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