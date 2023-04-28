class DeltaBool:

    def create_bool_delta(main: bool, other: bool) -> bool:
        result = None
        if main is True:
            if other is False:
                result = True
        else:
            if other is True:
                result = True
        return result
    
    def apply_bool_delta(main: bool, delta: bool) -> bool:        
        result = None
        if delta is not None:
            if main is True:
                if delta is True:
                    result = inverse_bool(main)
                else:
                    result = main
            else:
                if delta is True:
                    result = inverse_bool(main)
                else:
                    result = main
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
    pass