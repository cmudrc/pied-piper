from copy import deepcopy

from piperabm.environment.structures.road import Road
from piperabm.degradation.sudden.distributions.samples import distribution_0 as distribution
from piperabm.boundary.rectangular.samples import rectangular_0 as boundary
from piperabm.unit import Date


road = Road(
    boundary=deepcopy(boundary),
    start_date=Date(2020, 1, 2),
    difficulty=1.5,
    width=2,
    sudden_degradation_dist=deepcopy(distribution)
)


if __name__ == "__main__":
    print(road)