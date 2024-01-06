from copy import deepcopy


class DeltaStr:
    """
    Create and apply delta for string variable
    """

    def create(old_variable: str, new_variable: str) -> str:
        """ Create delta for string variable """
        delta = None
        if old_variable is not None:
            if new_variable is not None:
                if new_variable != old_variable:
                    delta = new_variable
                else:
                    delta = None
            else: # when *new_variable* is None
                delta = None
        else:  # when *old_variable* is None
            delta = new_variable
        return delta

    def apply(old_variable: str, delta: str = None) -> str:
        """ Apply delta to string variable """
        new_variable = None
        if old_variable is not None:
            if delta is not None:
                new_variable = deepcopy(delta)
            else:  # when *delta* is None
                new_variable = deepcopy(old_variable)
        else:  # when *old_variable* is None
            new_variable = deepcopy(delta)
        return new_variable


if __name__ == "__main__":
    old_variable = 'a'
    new_variable = 'b'
    delta = DeltaStr.create(old_variable, new_variable)
    print(delta)
