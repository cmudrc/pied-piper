class DeltaStr:
    """
    Create and apply delta for string variable
    """

    def create(main: str, other: str) -> str:
        """ Create delta for string variable """
        delta = None
        if main is not None:
            if other is not None:
                if other != main:
                    delta = other
                else:
                    delta = None
            else: # when *other* is None
                delta = None
        else:  # when *main* is None
            delta = other
        return delta

    def apply(main: str, delta: str = None) -> str:
        """ Apply delta to string variable """
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
    main = 'a'
    other = 'b'
    result = DeltaStr.create(main, other)
    print(result)
