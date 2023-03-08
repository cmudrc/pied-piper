def sub_function(amount: float, current_amount: float, min_amount: float=0):
    """
    Calculate the final amount when subtracting from the resource
    """
    remaining = 0
    new_current_amount = None

    if amount is None: pass
    elif amount < 0: raise ValueError

    if current_amount is None: pass
    elif current_amount < 0: raise ValueError

    if min_amount < 0: raise ValueError

    if amount is not None and current_amount is not None:
        new_current_amount = (current_amount - min_amount) - amount
        if new_current_amount < 0:
            remaining = abs(new_current_amount)
            new_current_amount = min_amount
    else:
        if amount is not None:
            new_current_amount = None
            remaining = 0
        elif current_amount is not None:
            new_current_amount = 0
            remaining = None

    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = sub_function(6, 5, 1)
    print(result, remaining)