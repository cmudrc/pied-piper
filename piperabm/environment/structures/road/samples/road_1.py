from copy import deepcopy

from piperabm.environment.structures.road import Road
from piperabm.degradation.sudden.distributions.samples import distribution_0 as distribution
from piperabm.unit import Date


road = Road(
    name='Halfway 1',
    start_date=Date(2020, 1, 4),
    difficulty=1.5,
    width=2,
    sudden_degradation_dist=deepcopy(distribution)
)


if __name__ == "__main__":
    road.print()