from piperabm.tools import average as avg


def multi_time_accessibility(accessibilities: list, durations: list) -> float:
    return avg.arithmetic(values=accessibilities, weights=durations)


if __name__ == "__main__":
    accessibilities = [1, 0.8, 0.5, 0.2, 0]
    durations = [1, 1, 1, 1, 1]
    print(multi_time_accessibility(accessibilities, durations))