from piperabm.tools.lattice.conditions.condition import Condition
import numpy as np

filter = [
    [0, 0, 0,],
    [0, 1, 0,],
    [0, 0, 0,],
]

condition = Condition(
    name=0,
    filter=filter
)


if __name__ == "__main__":
    for filter in condition.filters:
        print(filter)