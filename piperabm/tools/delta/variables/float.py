class DeltaFloat:
    """
    Create and apply delta for float (and integer) variable
    """

    def create(main, other):
        """ Create delta for float variable """
        delta = None
        if other is not None:
            if main is None:
                delta = other
            elif main != other:
                delta = other - main
        return delta

    def apply(main, delta):
        """ Apply delta to float variable """
        other = None
        if delta is not None:
            if main is None:
                other = delta
            else:
                other = main + delta
        else:
            other = main
        return other   


if __name__ == "__main__":
    main = 2
    other = 5
    result = DeltaFloat.create(main, other)
    print(result)