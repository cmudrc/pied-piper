class DeltaStr:
    """
    Create and apply delta for string variable
    """

    def create(main: str, other: str) -> str:
        """ Create delta for string variables """
        delta = None
        if main is not None:
            if other != main:
                delta = other
        else:
            delta = other
        return delta
    
    def apply(main: str, delta: str) -> str:
        """ Apply delta to string variables """
        other = None
        if delta is not None:
            other = delta
        else:
            other = main
        return other
    

if __name__ == "__main__":
    main = 'a'
    other = 'b'
    result = DeltaStr.create(main, other)
    print(result)