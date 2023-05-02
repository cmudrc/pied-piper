from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic.refine_input import refine_input, refine_output


def add_function(
        val: float,
        current_amount: float,
        max_amount: float = None,
        min_amount: float = None
    ):
    """
    Calculate the final amount when additing to the resource
    """
    val, current_amount, max_amount, min_amount = \
    refine_input(val, current_amount, max_amount, min_amount)
    
    current_amount = current_amount + val

    return refine_output(current_amount, max_amount, min_amount)


if __name__ == "__main__":
    result, remaining = add_function(
        val=5,
        current_amount=6,
        max_amount=10
    )
    print(result, remaining)