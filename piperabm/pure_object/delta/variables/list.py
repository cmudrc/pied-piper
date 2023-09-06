from piperabm.pure_object.delta.variables.dict import DeltaDict


class DeltaList:

    def create(main: list, other: list) -> list:
        """ Create delta for list variables """
        delta = None
        if main is not None:
            if other is not None:
                main_dict = list_to_dict(main)
                other_dict = list_to_dict(other)
                delta = DeltaDict.create(main_dict, other_dict)
            else:
                delta = main
        else:
            delta = other
        return delta
    
    def apply(main: list, delta: dict) -> list:
        """ Apply delta to list variables """
        if main is not None:
            other = main
            if delta is not None:
                pass
            else:
                other = main
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


if __name__ == '__main__':
    main = [2, 'asl', True]
    other = [1, 'aslan', False]
    result = DeltaList.create(main, other)
    print(result)