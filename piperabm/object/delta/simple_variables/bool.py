from copy import deepcopy


class DeltaBool:
    """
    Create and apply delta for boolean variable
    """

    def create(old_variable: bool, new_variable: bool) -> bool:
        """ Create delta for boolean variable """
        delta = None
        if old_variable is not None:
            if new_variable is not None:
                if new_variable != old_variable:
                    delta = new_variable
                else:
                    delta = None
            else:  # when *new_variable* is None
                delta = None
        else:  # when *old_variable* is None
            delta = new_variable
        return delta
    
    def apply(old_variable: bool, delta: bool = None) -> bool:
        """ Create delta to boolean variable """  
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
    old_variable = True
    new_variable = False
    delta = DeltaBool.create(new_variable, old_variable)
    print(delta)