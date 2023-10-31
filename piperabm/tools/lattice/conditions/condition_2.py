from piperabm.tools.lattice.conditions.condition import Condition


filter = [
    [0, 1, 0,],
    [0, 1, 1,],
    [0, 0, 0,],
]

condition = Condition(
    name=2,
    filter=filter
)


if __name__ == "__main__":
    for filter in condition.filters:
        print(filter)