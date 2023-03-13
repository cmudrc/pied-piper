def truediv_function(current_amount: float, div_val: float, max_amount: float=None, min_amount: float=0):
    """
    Calculate the final amount when subtracting from the resource
    """

    def validate_input(current_amount, div_val, max_amount, min_amount):
        if div_val is None: pass
        elif div_val < 0: raise ValueError

        if current_amount is None: pass
        elif current_amount < 0: raise ValueError

        if max_amount is not None:
            if max_amount < 0: raise ValueError

        if min_amount < 0: raise ValueError

    def min_max_normalize(min_amount, max_amount, current_amount):
        remaining = 0
        if max_amount is not None:
            if current_amount is not None:
                if current_amount > max_amount:
                    remaining = current_amount - max_amount
                    current_amount = max_amount
            else: # current_amount is None
                remaining = None
                current_amount = max_amount
        if min_amount > 0:
            if current_amount < min_amount:
                remaining = min_amount - current_amount
                current_amount = min_amount
        return current_amount, remaining

    validate_input(current_amount, div_val, max_amount, min_amount)
    if div_val is None:
        if current_amount is None:
            new_current_amount = 1
        else: # current_amount is normal
            new_current_amount = 0
    elif div_val == 0:
        new_current_amount = None
    else: # div_val is normal
        if current_amount is None:
            new_current_amount = None
        else:
            new_current_amount = current_amount / div_val
    return min_max_normalize(
        min_amount,
        max_amount,
        new_current_amount
    )


if __name__ == "__main__":
    result, remaining = truediv_function(
        current_amount=3,
        div_val=3, 
        max_amount=5,
        min_amount=1
    )
    print(result, remaining)