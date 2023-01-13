from piperabm import Environment
from piperabm.boundary import Point, Circular, Rectangular
from piperabm.degradation import DiracDelta
from piperabm.unit import Date, DT


env = Environment()

env.add_settlement(
    name="Settlement 1",
    pos=[-60, 40],
    boundary=Point()
)
env.add_settlement(
    name="Settlement 2",
    pos=[200, 20],
    boundary=Circular(radius=5)
)
env.add_settlement(
    name="Settlement 3",
    pos=[100, -180],
    boundary=Rectangular(height=5, width=3, theta=0.3)
)

env.add_link(
    start="Settlement 1",
    end=[0, 0],
    initiation_date=Date(2020, 1, 1),
    degradation_dist=DiracDelta(main=DT(days=5).total_seconds())
    )
env.add_link(start=[0.5, 0.5], end=[80, 60])
env.add_link(start=[80, 60], end=[200, 20])
env.add_link(start=[0, 0], end="Settlement 3")

#start_date = Date(2020, 1, 1)
#end_date = start_date + DT(days=10)
#L.update_all_edges(start_date, end_date, unit_length=10)

env.show()

#P = Path(L)
#P.show()

#from agents import Society

#S = Society(L)
#S.add_agents(5)
#print(S.G)




