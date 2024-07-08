"""
Serialization for networkx objects that includes both node and edge attributes
"""

import networkx as nx


terminology = {
    'type': 't',
    'nodes': 'n',
    'edges': 'e',
    'MultiDiGraph': 'MDG',
    'MultiGraph': 'MG',
    'DiGraph': 'DG',
    'Graph': 'G'
}


def nx_serialize(G) -> dict:
    """
    Serialize networkx object
    """
    result = {}

    # Type
    if isinstance(G, nx.MultiDiGraph):
        type = terminology["MultiDiGraph"]
        multi = True
    elif isinstance(G, nx.MultiGraph):
        type = terminology["MultiGraph"]
        multi = True
    elif isinstance(G, nx.DiGraph):
        type = terminology["DiGraph"]
        multi = False
    elif isinstance(G, nx.Graph):
        type = terminology["Graph"]
        multi = False
    else:
        raise TypeError
    result[terminology['type']] = type # Type

    # Nodes
    nodes_serialized = {}
    for node in G.nodes():
        nodes_serialized[node] = G.nodes[node]
    result[terminology['nodes']] = nodes_serialized

    # Edges 
    edges_serialized = {}
    if multi is False:
        for u, v, data in G.edges(data=True):
            if u not in edges_serialized:
                edges_serialized[u] = {}
            edges_serialized[u][v] = data
    elif multi is True:
        for u, v, key, data in G.edges(keys=True, data=True):
            if u not in edges_serialized:
                edges_serialized[u] = {}
            if v not in edges_serialized[u]:
                edges_serialized[u][v] = {}
            edges_serialized[u][v][key] = data
    result[terminology['edges']] = edges_serialized # Edges

    return result


def nx_deserialize(dictionary: dict):
    """
    Deserialize networkx object
    """

    # Type
    if dictionary[terminology['type']] == terminology["MultiDiGraph"]:
        G = nx.MultiDiGraph()
        multi = True
    elif dictionary[terminology['type']] == terminology["MultiGraph"]:
        G = nx.MultiGraph()
        multi = True
    elif dictionary[terminology['type']] == terminology["DiGraph"]:
        G = nx.DiGraph()
        multi = False
    elif dictionary[terminology['type']] == terminology["Graph"]:
        G = nx.Graph()
        multi = False
    else:
        raise TypeError
    
    # Nodes
    nodes_serialized = dictionary[terminology['nodes']]
    for node in nodes_serialized:
        G.add_node(node)
        for key in nodes_serialized[node]:
            G.nodes[node][key] = nodes_serialized[node][key]

    # Edges
    edges_serialized = dictionary[terminology['edges']]
    for u in edges_serialized:
        edge_serialized_u = edges_serialized[u]
        for v in edge_serialized_u:
            if multi is False:
                edge_attributes = edge_serialized_u[v]
                G.add_edge(u, v, **edge_attributes)
            elif multi is True:
                edge_serialized_u_v = edge_serialized_u[v]
                for key in edge_serialized_u_v:
                    edge_attributes = edge_serialized_u_v[key]
                    G.add_edge(u, v, **edge_attributes)

    return G


if __name__ == "__main__":
    G = nx.Graph()
    G.add_node(1, weight=1)
    G.add_node(2, weight=2)
    G.add_edge(1, 2, weight=3)
    G_serialized = nx_serialize(G)
    print(G_serialized)
    G_new = nx_deserialize(G_serialized)
    print(nx_serialize(G_new))
    print("Test: ", nx_serialize(G_new) == G_serialized)