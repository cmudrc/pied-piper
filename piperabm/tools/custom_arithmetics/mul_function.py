def mul_function(mul_val: float, current_amount: float, max_amount: float=None):
    """
    Calculate the final amount when subtracting from the resource
    """
    if mul_val < 0 or current_amount < 0: raise ValueError
    if max_amount is not None:
        if max_amount < 0: raise ValueError
    new_current_amount = current_amount * mul_val
    remaining = 0
    if max_amount is not None:
        if new_current_amount > max_amount:
            remaining = new_current_amount - max_amount
            new_current_amount = max_amount
    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = mul_function(2, 3, 5)
    print(result, remaining)