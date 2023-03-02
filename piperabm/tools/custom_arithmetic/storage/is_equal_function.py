def is_equal_function(amount_1: float, amount_2: float):
    """
    Calculate the final amount when adding to the resource
    """

    def handle_nones(amount):
        if amount is None:
            amount = 0
        return amount
    
    amount_1 = handle_nones(amount_1)
    amount_2 = handle_nones(amount_2)
    if amount_1 < 0 or amount_2 < 0: raise ValueError
    if amount_1 == amount_2: result = True
    else: result = False
    return result


if __name__ == "__main__":
    result = is_equal_function(0, None)
    print(result)