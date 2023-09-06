from piperabm.pure_object.delta.variables.bool import DeltaBool
from piperabm.pure_object.delta.variables.float import DeltaFloat
from piperabm.pure_object.delta.variables.str import DeltaStr


class VariableDelta:
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
        return result
    

if __name__ == '__main__':
    main = 'a'
    other = 'b'
    result = VariableDelta.create(main, other)
    print(result)


