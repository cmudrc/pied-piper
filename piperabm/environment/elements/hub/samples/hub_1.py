from piperabm.environment.elements.hub import Hub
from piperabm.environment.structures.settlement.samples import settlement_1
from piperabm.unit import Date


hub = Hub(
    name="Peter's Home",
    pos=[20, 20],
    start_date=Date(2020, 1, 4),
    structure=settlement_1
)


if __name__ == "__main__":
    print(hub)