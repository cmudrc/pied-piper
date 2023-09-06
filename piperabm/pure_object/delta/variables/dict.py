from piperabm.pure_object.delta.variables.variable_delta import VariableDelta


class DeltaDict:

    def create(main: dict, other: dict) -> dict:
        """ Create delta for dictionary variables """
        delta = None
        if main is not None:
            if other is not None:
                delta = {}
                for key in main:
                    main_value = main[key]
                    if key in other:
                        other_value = other[key]
                        delta_val = VariableDelta.create(main_value, other_value)
                        if delta_val is not None:
                            delta[key] = delta_val
                if len(delta) == 0:
                    delta = None
        else:
            delta = other
        return delta

    def apply(main: dict, delta: dict) -> dict:
        """ Apply delta to dictionary variables """
        if main is not None:
            other = main
            if delta is not None:
                for key in delta:
                    delta_val = delta[key]
                    if key in main:
                        main_val = main[key]
                        new_val = VariableDelta.apply(main_val, delta_val)
                    else:
                        new_val = delta_val
                    other[key] = new_val
        else:
            other = delta
        return other
    

if __name__ == '__main__':
    main = {'a': 2, 'b': 'asl', 'c': True}
    other = {'a': 1, 'b': 'aslan', 'c': False}
    result = DeltaDict.create(main, other)
    print(result)