from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.structures.settlement.samples import settlement_0, settlement_1
from piperabm.environment.structures.road.samples import road_0, road_1


environment = Environment()

environment.append_node(
    pos=[-2, -2],
    structure=deepcopy(settlement_0)
)
environment.append_node(
    pos=[20, 20],
    structure=deepcopy(settlement_1)
)

environment.add_edge_object(
    _from="John's Home",
    _to=[20, 0],
    structure=deepcopy(road_0)
)
environment.add_edge_object(
    _from=[20, 0],
    _to="Peter's Home",
    structure=deepcopy(road_1)
)


if __name__ == "__main__":
    import networkx as nx

    environment.print()
    #G = environment.G
    #dictionary = environment.to_dict()
    #dictionary = nx.to_dict_of_dicts(G, edge_data={})
    #G_new = nx.Graph()
    #G_new = nx.from_dict_of_dicts(dictionary)
    #print(G_new)
    #environment.G = G_new
    #pos = environment.get_edge_pos(0, 1)
    #print(pos)
    #print(dictionary['edges'])
