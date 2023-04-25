from piperabm.environment import Environment
from piperabm.unit import Date, DT
from piperabm.degradation.sudden.distributions import DiracDelta
    

environment = Environment()

environment.add_settlement(
    name="Settlement 1",
    pos=[-60, 40],
    start_date=Date(2020, 1, 2)
)
environment.add_settlement(
    name="Settlement 2",
    pos=[200, 20],
    start_date=Date(2020, 1, 2)
)
environment.add_settlement(
    name="Settlement 3",
    pos=[100, -180],
    start_date=Date(2020, 1, 2)
)
#environment.add_market(
#    name="Market",
#    pos=[70, -30]
#)

environment.add_road(
    _from="Settlement 1",
    _to=[0, 0],
    start_date=Date(2020, 1, 2),
    sudden_degradation_dist=DiracDelta(main=DT(days=5))
)
environment.add_road(
    _from=[0.5, 0.5],
    _to=[80, 60],
    start_date=Date(2020, 1, 2)
)
environment.add_road(
    _from=[80, 60],
    _to=[200, 20],
    start_date=Date(2020, 1, 2)
)
environment.add_road(
    _from=[0, 0],
    _to="Settlement 3",
    start_date=Date(2020, 1, 2)
)
#enenvironmentv.add_road(start=[0, 0], end="Market")


if __name__ == "__main__":
    environment.print()
