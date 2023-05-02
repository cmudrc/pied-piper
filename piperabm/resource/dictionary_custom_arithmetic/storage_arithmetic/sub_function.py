from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic.add_function import add_function


def sub_function(
        val: float,
        current_amount: float,
        max_amount: float = None,
        min_amount: float = None
    ):
    """
    Calculate the final amount when subtracting from the resource
    """
    val *= -1
    return add_function(val, current_amount, max_amount, min_amount)    


if __name__ == "__main__":
    result, remaining = sub_function(
        val=6,
        current_amount=5,
        min_amount=1
    )
    print(result, remaining)