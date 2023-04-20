from piperabm.environment import Environment
from piperabm.environment.elements.samples.hub import hub_0, hub_1
from piperabm.environment.elements.samples.link import link_0, link_1


environment = Environment(links_unit_length=10)
index = environment.find_next_index()
environment.add_node(index, element=hub_0)
index = environment.find_next_index()
environment.add_node(index, element=hub_1)

'''
environment.add_link(
    "John's Home",
    [20, 0],
    start_date=Date(2020, 1, 2),
    sudden_degradation_dist=DiracDelta(main=DT(days=10))
)
environment.add_link(
    [20.3, 0.3],
    "Peter's Home",
    start_date=Date(2020, 1, 4),
    sudden_degradation_dist=DiracDelta(main=DT(days=10))
)
'''

if __name__ == "__main__":
    from piperabm.unit import Date

    start_date = Date(2020, 1, 5)
    end_date = Date(2020, 1, 10)
    environment.update_elements(start_date, end_date)
    current_graph = environment.to_current_graph(start_date, end_date)
    current_graph.show()
