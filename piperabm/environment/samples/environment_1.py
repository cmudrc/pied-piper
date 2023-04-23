from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.elements.hub.samples import hub_0, hub_1
from piperabm.environment.elements.link.samples import link_0, link_1
#from piperabm.degradation.sudden.distributions.samples.dirac_delta import dirac_delta_0 as distribution
#from piperabm.unit import Date


environment = Environment()

environment.append_node(element=deepcopy(hub_0))
environment.append_node(element=deepcopy(hub_1))

environment.add_link_object(
    _from="John's Home",
    _to=[20, 0],
    link=deepcopy(link_0)  
)
environment.add_link_object(
    _from=[20, 0],
    _to="Peter's Home",
    link=deepcopy(link_1)
)


'''
environment.add_road(
    _from="John's Home",
    _to=[20, 0],
    start_date=Date(2020, 1, 2),
    sudden_degradation_dist=distribution
)
environment.add_road(
    _from=[20, 0],
    _to="Peter's Home",
    start_date=Date(2020, 1, 4),
    sudden_degradation_dist=distribution
)

from piperabm.tools.coordinate import slope, center

s1 = environment.get_node_element(0)
pos_start = s1.pos
s2 = environment.get_node_element(2)
pos_end = s2.pos
center_pos = center(pos_start, pos_end)
angle = slope(pos_start, pos_end)
e = environment.get_edge_element(0,2)
#e.pos
print(pos_start, pos_end)
print(angle * 180 / 3.1415, center_pos)
'''


if __name__ == "__main__":
    print(environment)
