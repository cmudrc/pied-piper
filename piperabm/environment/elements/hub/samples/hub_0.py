from copy import deepcopy

from piperabm.environment.elements import Hub
from piperabm.environment.structures.settlement.samples import settlement_0
from piperabm.unit import Date


hub = Hub(
    name="John's Home",
    pos=[-2, -2],
    start_date=Date(2020, 1, 2),
    structure=deepcopy(settlement_0)
)


if __name__ == "__main__":
    print(hub)