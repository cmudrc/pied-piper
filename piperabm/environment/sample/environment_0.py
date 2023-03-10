from piperabm import Environment
from piperabm.unit import Date, DT
from piperabm.degradation import DiracDelta
from piperabm.boundary import Circular


env = Environment(links_unit_length=10)

env.add_settlement(
    name="John's Home",
    pos=[-2, -2],
    boundary=Circular(radius=5),
    initiation_date=Date(2020, 1, 2),
    degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
)
env.add_settlement(
    name="Peter's Home",
    pos=[20, 20],
    boundary=Circular(radius=5),
    initiation_date=Date(2020, 1, 4),
    degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
)

env.add_link(
    "John's Home",
    [20, 0],
    initiation_date=Date(2020, 1, 2),
    degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
)
env.add_link(
    [20.3, 0.3],
    "Peter's Home",
    initiation_date=Date(2020, 1, 4),
    degradation_dist=DiracDelta(main=DT(days=10).total_seconds())
)

if __name__ == "__main__":
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    env.update_elements(start_date, end_date)
    link_graph = env.to_link_graph(start_date, end_date)
    link_graph.show()
