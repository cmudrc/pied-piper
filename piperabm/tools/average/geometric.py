import math


def geometric(values: list, weights: list = None):
    result = None
    if weights is None:
        total = 1
        for value in values:
            total *= value
        result = total ** (1 / len(values))
    else:
        if len(values) != len(weights):
            raise ValueError("The lengths of values and weights must be the same.")
        
        if any(v <= 0 for v in values):
            raise ValueError("All values must be greater than zero.")
        
        log_values = [math.log(v) * w for v, w in zip(values, weights)]
        total_weight = sum(weights)
        
        if total_weight == 0:
            raise ValueError("The sum of weights must not be zero.")
        
        log_weighted_mean = sum(log_values) / total_weight
        result = math.exp(log_weighted_mean)
    return result


if __name__ == "__main__":
    values = [1, 2, 3]
    print(geometric(values=values))

    weights = [1, 1, 1]
    print(geometric(values=values, weights=weights))

    weights = [100, 1, 1]
    print(geometric(values=values, weights=weights))
