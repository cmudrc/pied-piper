class DeltaBool:
    """
    Create and apply delta for boolean variable
    """

    def create(main: bool, other: bool) -> bool:
        """ Create delta for boolean variable """
        result = None
        if main is not None:
            if other is not None:
                if other != main:
                    result = True
        else:
            result = other
        return result
    
    def apply(main: bool, delta: bool) -> bool:
        """ Create delta to boolean variable """       
        result = None
        if delta is not None:
            if main is not None:
                if delta is True:
                    result = inverse_bool(main)
                else:
                    result = main
            else:
                result = delta
        else:
            result = main
        return result    


def inverse_bool(main: bool):
    """
    Inverse the boolean input
    """
    result = None
    if main is True:
        result = False
    elif main is False:
        result = True
    return result


if __name__ == "__main__":
    main = True
    other = False
    result = DeltaBool.create(other, main)
    print(result)