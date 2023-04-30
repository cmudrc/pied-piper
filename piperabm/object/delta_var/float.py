class DeltaFloat:

    def create_float_delta(main, other):
        delta = None
        if other is not None:
            if main is None:
                delta = other
            elif main != other:
                delta = other - main
        return delta

    def apply_float_delta(main, delta):
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
    result = DeltaFloat.create_float_delta(main, other)
    print(result)