import networkx as nx

class Test():
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return str(self.val)

G = nx.DiGraph()
info = {
    'type': 'storage'
}
G.add_node('n1', **info)

info = {
    'type': 'storage'
}
G.add_node('n2', **info)

t = Test(val=5)
info = {
    'source': t
}
G.add_edge('n1', 'n2', **info)

#print(G['n1']['n2']['source'])
t_prime = G['n1']['n2']['source']
t_prime.val = 6
print(t, t_prime)
