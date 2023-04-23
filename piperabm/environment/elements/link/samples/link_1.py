from copy import deepcopy

from piperabm.environment.elements import Link
from piperabm.environment.structures.road.samples import road_1
from piperabm.unit import Date


link = Link(
    name='halfway 1',
    start_date=Date(2020, 1, 4),
    structure=deepcopy(road_1)
)


if __name__ == "__main__":
    print(link)