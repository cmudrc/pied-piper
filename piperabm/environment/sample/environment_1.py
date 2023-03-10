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
#env.add_market(
#    name="Market",
#    pos=[70, -30]
#)

env.add_link(
    start="Settlement 1",
    end=[0, 0],
    initiation_date=Date.today()-DT(days=3),
    degradation_dist=DiracDelta(main=DT(days=5).total_seconds())
)
env.add_link(start=[0.5, 0.5], end=[80, 60])
env.add_link(start=[80, 60], end=[200, 20])
env.add_link(start=[0, 0], end="Settlement 3")
#env.add_link(start=[0, 0], end="Market")


if __name__ == "__main__":
    from piperabm.unit import Date, DT

    start_date = Date.today()
    end_date = start_date + DT(days=1)
    env.update_elements(start_date, end_date)
    link_graph = env.to_link_graph(start_date, end_date)
    link_graph.show()