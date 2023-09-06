class DeltaBool:
    """
    Create and apply delta for boolean variable
    """

    def create_bool_delta(main: bool, other: bool) -> bool:
        result = None
        if main is not None:
            if other is not None:
                if other != main:
                    result = True
        else:
            result = other
        return result
    
    def apply_bool_delta(main: bool, delta: bool) -> bool:        
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
    result = DeltaBool.create_bool_delta(other, main)
    print(result)