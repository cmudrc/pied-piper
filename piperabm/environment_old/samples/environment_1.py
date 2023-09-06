from copy import deepcopy

from piperabm.environment_old import Environment
from piperabm.infrastructure.settlement.samples import settlement_0, settlement_1
from piperabm.infrastructure.road.samples import road_0, road_1


environment = Environment()

environment.append_node(
    pos=[-2, -2],
    structure=deepcopy(settlement_0)
)
environment.append_node(
    pos=[20, 20],
    structure=deepcopy(settlement_1)
)

environment.add_edge_object(
    _from="John's Home",
    _to=[20, 0],
    structure=deepcopy(road_0)
)
environment.add_edge_object(
    _from=[20, 0],
    _to="Peter's Home",
    structure=deepcopy(road_1)
)


if __name__ == "__main__":
    environment.print()

