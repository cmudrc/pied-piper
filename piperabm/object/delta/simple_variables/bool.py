class DeltaBool:
    """
    Create and apply delta for boolean variable
    """

    def create(main: bool, other: bool) -> bool:
        """ Create delta for boolean variable """
        delta = None
        if main is not None:
            if other is not None:
                if other != main:
                    delta = other
                else:
                    delta = None
            else:  # when *other* is None
                delta = None
        else:  # when *main* is None
            delta = other
        return delta
    
    def apply(main: bool, delta: bool = None) -> bool:
        """ Create delta to boolean variable """  
        other = None
        if main is not None:
            if delta is not None:
                other = delta
            else:  # when *delta* is None
                other = main
        else:  # when *main* is None
            other = delta
        return other


if __name__ == "__main__":
    main = True
    other = False
    result = DeltaBool.create(other, main)
    print(result)