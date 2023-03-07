import networkx as nx

G = nx.DiGraph()
G.add_edge('a', 'b')
G.add_node('c')
r = G.out_edges('c')
print(r)