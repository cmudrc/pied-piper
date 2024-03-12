import networkx as nx
import os


def to_ora(model, path):
    G = model.infrastructure
    path = model.path
    filename = model.name
    format = "xml"
    filepath = os.path.join(path, filename + "." + format)
    nx.write_graphml(G, filepath)

if __name__ == "__main__":
    from load_initial import model

    to_ora(model)