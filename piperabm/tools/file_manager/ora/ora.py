import networkx as nx
import os


'''
import csv
def location_x_location(infrastructure, path):
    # Recreate G
    G = nx.Graph()
    edges_ids = infrastructure.edges_ids
    for edge_ids in edges_ids:
        edge_id = infrastructure.edge_id(*edge_ids)
        object = infrastrcuture.get(edge_id)
        G.add_edge(edge_ids[0], edge_ids[1], degradation=object.degradation)

    # Save
    filename = "location_x_location"
    format = "xml"
    filepath = os.path.join(path, filename + "." + format)
    nx.write_graphml(G, filepath)

def location_attributes(infrastructure, path):
    # Extract info
    header = ['id', 'type', 'x', 'y']
    result = []
    nodes_id = infrastructure.nodes_id
    for id in nodes_id:
        object = infrastrcuture.get(id)
        type = object.type
        pos = object.pos
        x = pos[0]
        y = pos[1]
        result.append([id, type, x, y])

    # Save
    filename = "location_attributes"
    format = "csv"
    filepath = os.path.join(path, filename + "." + format)
    # WRITE CODE TO SAVE THE result (with header) as CSV FILE
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Writing the header
        writer.writerows(result)  # Writing the content


def infrastructure_to_ora(infrastructure, path):
    location_x_location(infrastructure, path)
    location_attributes(infrastructure, path)
'''

def infrastructure_to_ora(infrastructure, path):
    # Recreate G
    G = nx.Graph()
    nodes_id = infrastructure.nodes_id
    for id in nodes_id:
        object = infrastructure.get(id)
        type = object.type
        pos = object.pos
        x = pos[0]
        y = pos[1]
        G.add_node(id, type=type, x=x, y=y)
    edges_ids = infrastructure.edges_ids
    for edge_ids in edges_ids:
        edge_id = infrastructure.edge_id(*edge_ids)
        object = infrastructure.get(edge_id)
        G.add_edge(edge_ids[0], edge_ids[1], degradation=object.degradation)
    # Save
    filename = "location_x_location"
    format = "graphml"
    filepath = os.path.join(path, filename + "." + format)
    nx.write_graphml(G, filepath)


if __name__ == "__main__":

    from piperabm.infrastructure_new.samples import infrastructure_2 as infrastrcuture

    path = os.path.dirname(os.path.realpath(__file__))
    infrastructure_to_ora(infrastrcuture, path)