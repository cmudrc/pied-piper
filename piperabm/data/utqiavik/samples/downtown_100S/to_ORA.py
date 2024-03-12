import networkx as nx
import os
import json


def to_graphml(model):
    G = model.infrastructure.G
    path = model.path
    filename = model.name
    format = "graphml"
    filepath = os.path.join(path, filename + "." + format)
    nx.write_graphml(G, filepath, )

def to_json(model):
    G = model.infrastructure.G
    graph_dict = nx.node_link_data(G)
    path = model.path
    filename = model.name
    format = "json"
    filepath = os.path.join(path, filename + "." + format)
    with open(filepath, 'w') as json_file:
        json.dump(graph_dict, json_file)


if __name__ == "__main__":
    from load_initial import model

    to_graphml(model)