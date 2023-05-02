from piperabm.tools.symbols import SYMBOLS


def refine_input(
        amount: float,
        current_amount: float,
        max_amount: float = None,
        min_amount: float = None
):
    ''' amount '''
    if amount is None:
        raise ValueError

    ''' current_amount '''
    if current_amount is None:
        raise ValueError
    
    ''' min_amount '''
    if min_amount is None:
        min_amount = 0
    elif min_amount < 0:
        raise ValueError

    ''' max_amount '''
    if max_amount is None:
        max_amount = SYMBOLS['inf']
    elif max_amount < min_amount:
        raise ValueError

    return amount, current_amount, max_amount, min_amount


def refine_output(
    current_amount: float,
    max_amount: float,
    min_amount: float
):
    remainder = 0
    if current_amount > max_amount:
        remainder = current_amount - max_amount
        current_amount -= remainder

    if current_amount < min_amount:
        remainder = min_amount - current_amount
        current_amount += remainder

    return current_amount, remainder