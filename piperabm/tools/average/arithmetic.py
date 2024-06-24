def arithmetic(values: list, weights: list = None):
    result = None
    if weights is None:
        #print(values)
        result = sum(values) / len(values)
    else:
        if len(values) != len(weights):
            raise ValueError("The lengths of values and weights must be the same.")
        weighted_sum = sum(v * w for v, w in zip(values, weights))
        total_weight = sum(weights)
        if total_weight == 0:
            raise ValueError("The sum of weights must not be zero.")
        result = weighted_sum / total_weight
    return result


if __name__ == "__main__":
    values = [1, 2, 3]
    print(arithmetic(values=values))

    weights = [1, 1, 1]
    print(arithmetic(values=values, weights=weights))

    weights = [100, 1, 1]
    print(arithmetic(values=values, weights=weights))