from piperabm.resource.dictionary_custom_arithmetic.storage_arithmetic.refine_input import refine_input, refine_output


def mul_function(
    val: float,
    current_amount: float,
    max_amount: float = None,
    min_amount: float = None
):
    """
    Calculate the final amount when subtracting from the resource
    """
    val, current_amount, max_amount, min_amount = \
    refine_input(val, current_amount, max_amount, min_amount)

    current_amount = current_amount * val
    
    return refine_output(current_amount, max_amount, min_amount)


if __name__ == "__main__":
    result, remaining = mul_function(
        val=2, 
        current_amount=3,
        max_amount=5,
        min_amount=1
    )
    print(result, remaining)