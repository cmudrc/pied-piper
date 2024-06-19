"""
Serialization for networkx objects that includes both node and edge attributes
"""

import networkx as nx


terminology = {
    'type': 't',
    'nodes': 'n',
    'edges': 'e',
    'to': 't',
    'attributes': 'a',
}


def nx_serialize(G) -> dict:
    """
    Serialize networkx object
    """
    result = {}

    # Type
    if isinstance(G, nx.DiGraph):
        type = "DiGraph"
    elif isinstance(G, nx.Graph):
        type = "Graph"
    elif isinstance(G, nx.MultiGraph):
        type = "MultiGraph"
    elif isinstance(G, nx.MultiDiGraph):
        type = "MultiDiGraph"
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
    for edge in G.edges():
        edges_serialized[edge[0]] = {
            terminology['to']: edge[1], # To
            terminology['attributes']: G.edges[*edge] # Attributes
        }
    result[terminology['edges']] = edges_serialized # Edges

    return result


def nx_deserialize(dictionary: dict):
    """
    Deserialize networkx object
    """

    # Type
    if dictionary[terminology['type']] == "DiGraph":
        G = nx.DiGraph()
    elif dictionary[terminology['type']] == "Graph":
        G = nx.Graph()
    elif dictionary[terminology['type']] == "MultiDiGraph":
        G = nx.MultiDiGraph()
    elif dictionary[terminology['type']] == "MultiGraph":
        G = nx.MultiGraph()
    else:
        raise TypeError
    
    # Nodes
    nodes_serialized = dictionary[terminology['nodes']]
    for node in nodes_serialized:
        G.add_node(node)
        for key in nodes_serialized[node]:
            G.nodes[node][key] = nodes_serialized[node][key]

    # Edge
    edges_serialized = dictionary[terminology['edges']]
    for edge_from in edges_serialized:
        edge_serialized = edges_serialized[edge_from]
        edge_to = edge_serialized[terminology['to']]
        edge_attributes = edge_serialized[terminology['attributes']]
        G.add_edge(edge_from, edge_to, **edge_attributes)
    return G


if __name__ == "__main__":
    G = nx.Graph()
    G.add_node(1, weight=1)
    G.add_node(2, weight=2)
    G.add_edge(1, 2, weight=3)
    G_serialized = nx_serialize(G)
    print(G_serialized)
    G_new = nx_deserialize(G_serialized)
    #print(nx_serialize(G_new))
    print("Test: ", nx_serialize(G_new) == G_serialized)