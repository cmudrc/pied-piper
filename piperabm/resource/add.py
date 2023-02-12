from copy import deepcopy


def add_function(amount: float, current_amount: float, max_amount: float=None):
    """
    Calculate the final amount when adding to the resource
    """
    if amount < 0 or current_amount < 0:
        raise ValueError
    if max_amount is not None:
        if max_amount < 0:
            raise ValueError
    new_current_amount = current_amount + amount
    remaining = 0
    if max_amount is not None:
        if new_current_amount > max_amount:
            remaining = new_current_amount - max_amount
            new_current_amount = deepcopy(max_amount)
    return new_current_amount, remaining
