from piperabm.environment.structures.settlement import Settlement
from piperabm.degradation.sudden.distributions import DiracDelta
from piperabm.unit import Date, DT
from piperabm.boundary import Circular


settlement = Settlement(
    boundary=Circular(radius=5),
    start_date=Date(2020, 1, 4),
    sudden_degradation_dist=DiracDelta(main=DT(days=10))
)


if __name__ == "__main__":
    print(settlement)