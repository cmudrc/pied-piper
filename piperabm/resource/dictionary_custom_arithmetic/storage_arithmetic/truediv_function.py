from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic.mul_function import mul_function
from piperabm.tools.symbols import SYMBOLS


def truediv_function(
    val: float,
    current_amount: float,
    max_amount: float = None,
    min_amount: float = None
):
    """
    Calculate the final amount when subtracting from the resource
    """
    if val != 0:
        val = 1 / val
    else:
        val = SYMBOLS['inf']
    return mul_function(val, current_amount, max_amount, min_amount)


if __name__ == "__main__":
    result, remaining = truediv_function(
        val=0.5,
        current_amount=3,
        max_amount=5,
        min_amount=1
    )
    print(result, remaining)