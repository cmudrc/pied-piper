class DeltaFloat:
    """
    Create and apply delta for float (and integer) variable
    """

    def create(main: float, other: float):
        """ Create delta for float variable """
        delta = None
        if main is not None:
            if other is not None:
                if other != main:
                    delta = other - main
                else:
                    delta = None
            else: # when *other* is None
                delta = None
        else:  # when *main* is None
            delta = other
        return delta

    def apply(main: float, delta: float = None):
        """ Apply delta to float variable """
        other = None
        if main is not None:
            if delta is not None:
                other = main + delta
            else:  # when *delta* is None
                other = main
        else:  # when *main* is None
            other = delta
        return other


if __name__ == "__main__":
    main = 2
    other = 5
    result = DeltaFloat.create(main, other)
    print(result)
