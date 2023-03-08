def truediv_function(current_amount: float, div_val: float, max_amount: float=None, min_amount: float=0):
    """
    Calculate the final amount when subtracting from the resource
    """
    remaining = 0
    new_current_amount = None

    if div_val is None: pass
    elif div_val < 0: raise ValueError

    if current_amount is None: pass
    elif current_amount < 0: raise ValueError

    if max_amount is not None:
        if max_amount < 0: raise ValueError

    if min_amount < 0: raise ValueError

    if div_val is not None and current_amount is not None:
        new_current_amount = current_amount / div_val
        remaining = 0
        if max_amount is not None:
            if new_current_amount > max_amount:
                remaining = new_current_amount - max_amount
                new_current_amount = max_amount
        if min_amount > 0:
            if new_current_amount < min_amount:
                remaining = min_amount - new_current_amount
                new_current_amount = min_amount
    else:
        if div_val is not None: #######
            new_current_amount = None
            remaining = 0
            if max_amount is not None:
                remaining = None
                new_current_amount = max_amount
        elif current_amount is not None:
            new_current_amount = None
            if max_amount is not None:
                remaining = None
                new_current_amount = max_amount
    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = truediv_function(
        current_amount=3,
        div_val=3, 
        max_amount=5,
        min_amount=1
    )
    print(result, remaining)