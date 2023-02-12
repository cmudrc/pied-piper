from copy import deepcopy


def add_function(amount, current_amount, max_amount):
    """
    Calculate the final amount when adding to the resource
    """
    new_current_amount = current_amount + amount
    remaining = 0
    if max_amount is not None:
        if new_current_amount > max_amount:
            remaining = new_current_amount - max_amount
            new_current_amount = deepcopy(max_amount)
    if new_current_amount < 0:
        remaining = -new_current_amount
        new_current_amount = 0
    return new_current_amount, remaining