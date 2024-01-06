from copy import deepcopy


class DeltaFloat:
    """
    Create and apply delta for float (and integer) variable
    """

    def create(old_variable: float, new_variable: float):
        """ Create delta for float variable """
        delta = None
        if old_variable is not None:
            if new_variable is not None:
                if new_variable != old_variable:
                    delta = new_variable - old_variable
                else:
                    delta = None
            else: # when *new_variable* is None
                delta = None
        else:  # when *old_variable* is None
            delta = new_variable
        return delta

    def apply(old_variable: float, delta: float = None):
        """ Apply delta to float variable """
        new_variable = None
        if old_variable is not None:
            if delta is not None:
                new_variable = old_variable + delta
            else:  # when *delta* is None
                new_variable = deepcopy(old_variable)
        else:  # when *old_variable* is None
            new_variable = deepcopy(delta)
        return new_variable


if __name__ == "__main__":
    old_variable = 2
    new_variable = 5
    delta = DeltaFloat.create(old_variable, new_variable)
    print(delta)
