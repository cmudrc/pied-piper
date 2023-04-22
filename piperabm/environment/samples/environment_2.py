from piperabm.environment import Environment
from piperabm.unit import Date, DT
from piperabm.degradation.sudden.distributions import DiracDelta
from piperabm.boundary import Circular
    

environment = Environment(links_unit_length=10)

environment.add_settlement(
    name="Settlement 1",
    pos=[-60, 40]
)
environment.add_settlement(
    name="Settlement 2",
    pos=[200, 20],
    boundary=Circular(radius=5)
)
environment.add_settlement(
    name="Settlement 3",
    pos=[100, -180],
    boundary=Circular(radius=5)
)
#environment.add_market(
#    name="Market",
#    pos=[70, -30]
#)

environment.add_link(
    start="Settlement 1",
    end=[0, 0],
    initiation_date=Date.today()-DT(days=3),
    degradation_dist=DiracDelta(main=DT(days=5).total_seconds())
)
environment.add_link(start=[0.5, 0.5], end=[80, 60])
environment.add_link(start=[80, 60], end=[200, 20])
environment.add_link(start=[0, 0], end="Settlement 3")
#enenvironmentv.add_link(start=[0, 0], end="Market")


if __name__ == "__main__":
    print(environment)
    '''
    from piperabm.unit import Date, DT

    start_date = Date.today()
    end_date = start_date + DT(days=1)
    environment.update_elements(start_date, end_date)
    current_graph = environment.to_current_graph(start_date, end_date)
    current_graph.show()
    '''