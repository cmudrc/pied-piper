def sub_function(amount: float, current_amount: float, min_amount: float=0):
    """
    Calculate the final amount when subtracting from the resource
    """
    if amount < 0 or current_amount < 0:
        raise ValueError
    new_current_amount = (current_amount - min_amount) - amount
    remaining = 0
    if new_current_amount < 0:
        remaining = abs(new_current_amount)
        new_current_amount = min_amount
    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = sub_function(6, 5, 1)
    print(result, remaining)