from copy import deepcopy


def add_function(amount: float, current_amount: float, max_amount: float=None):
    """
    Calculate the final amount when adding to the resource
    """
    remaining = 0
    new_current_amount = None

    if amount is None: pass
    elif amount < 0: raise ValueError

    if current_amount is None: pass
    elif current_amount < 0: raise ValueError

    if max_amount is not None:
        if max_amount < 0: raise ValueError

    if amount is not None and current_amount is not None:
        new_current_amount = current_amount + amount
        if max_amount is not None:
            if new_current_amount > max_amount:
                remaining = new_current_amount - max_amount
                new_current_amount = deepcopy(max_amount)
                
    return new_current_amount, remaining


if __name__ == "__main__":
    result, remaining = add_function(5, 6, 10)
    print(result, remaining)