from copy import deepcopy

from piperabm.environment.structures.settlement import Settlement
from piperabm.degradation.sudden.distributions.samples import distribution_0 as distribution
from piperabm.boundary.circular.samples import circular_0 as boundary
from piperabm.unit import Date


settlement = Settlement(
    name="Peter's Home",
    boundary=deepcopy(boundary),
    start_date=Date(2020, 1, 4),
    sudden_degradation_dist=deepcopy(distribution)
)


if __name__ == "__main__":
    settlement.print()