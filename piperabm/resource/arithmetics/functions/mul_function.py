def mul_function(current_amount: float, mul_val: float, max_amount: float=0):
    """
    Calculate the final amount when subtracting from the resource
    """
    if current_amount < 0: raise ValueError
    new_current_amount = current_amount * mul_val
    remaining = 0
    if new_current_amount > max_amount:
        remaining = abs(new_current_amount) - max_amount
        new_current_amount = max_amount
    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = mul_function(2, 3, 5)
    print(result, remaining)