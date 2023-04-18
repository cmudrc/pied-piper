from piperabm.environment.structures.settlement import Settlement
from piperabm.degradation.sudden.distributions.samples import distribution_0 as distribution
from piperabm.boundary.samples import boundary_1 as boundary
from piperabm.unit import Date


settlement = Settlement(
    boundary=boundary,
    start_date=Date(2020, 1, 4),
    sudden_degradation_dist=distribution
)


if __name__ == "__main__":
    print(settlement)