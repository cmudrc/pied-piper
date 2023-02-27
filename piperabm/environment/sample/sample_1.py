from piperabm import Environment
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular
    
    
env = Environment(links_unit_length=10)

env.add_settlement(
    name="Settlement 1",
    pos=[-60, 40]
)
env.add_settlement(
    name="Settlement 2",
    pos=[200, 20],
    boundary=Circular(radius=5)
)
env.add_settlement(
    name="Settlement 3",
    pos=[100, -180],
    boundary=Circular(radius=5)
)
env.add_market(
    name="Market",
    pos=[70, -30]
)

env.add_link(
    start="Settlement 1",
    end=[0, 0],
    initiation_date=Date.today()-DT(days=3),
    degradation_dist=DiracDelta(main=DT(days=5).total_seconds())
)
env.add_link(start=[0.5, 0.5], end=[80, 60])
env.add_link(start=[80, 60], end=[200, 20])
env.add_link(start=[0, 0], end="Settlement 3")
env.add_link(start=[0, 0], end="Market")