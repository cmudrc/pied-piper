from piperabm import Model, Environment
from piperabm.boundary import Circular, Rectangular
from piperabm.degradation import DiracDelta
from piperabm.unit import Date, DT


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
    boundary=Rectangular(height=5, width=3, theta=0.3)
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
'''
start_date = Date.today()-DT(days=3)
end_date = start_date + DT(days=10)
env.update_elements(start_date, end_date)

env.show()
'''
# P = Path(L)
# P.show()

# from agents import Society

# S = Society(L)
# S.add_agents(5)
# print(S.G)

m = Model(
    environment=env,
    step_size=DT(days=5),
    current_date=Date.today()-DT(days=5)
)
m.show()
m.run()
m.show()
m.run()
m.show()
m.run()

