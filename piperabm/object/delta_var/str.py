class DeltaStr:

    def create_str_delta(main: str, other: str) -> str:
        delta = None
        if main is not None:
            if other != main:
                delta = other
        else:
            delta = other
        return delta
    
    def apply_str_delta(main: str, delta: str) -> str:
        other = None
        if delta is not None:
            other = delta
        else:
            other = main
        return other
    

if __name__ == "__main__":
    pass