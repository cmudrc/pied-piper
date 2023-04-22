from piperabm.environment.structures.road import Road
from piperabm.degradation.sudden.distributions.samples import distribution_0 as distribution
from piperabm.boundary.samples import boundary_0 as boundary
from piperabm.unit import Date


road = Road(
    boundary=boundary,
    start_date=Date(2020, 1, 2),
    sudden_degradation_dist=distribution
)


if __name__ == "__main__":
    print(road)