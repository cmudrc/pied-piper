def sub_function(amount: float, current_amount: float):
    """
    Calculate the final amount when subtracting from the resource
    """
    if amount < 0 or current_amount < 0:
        raise ValueError
    new_current_amount = current_amount - amount
    remaining = 0
    if new_current_amount < 0:
        remaining = abs(new_current_amount)
        new_current_amount = 0
    return new_current_amount, remaining