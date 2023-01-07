import networkx as nx

from piperabm.boundary import Point, Circular, Rectangular
from piperabm.degradation import Eternal, DiracDelta, Gaussian


class Links:
    def __init__(self):
        self.G = nx.MultiDiGraph()

    def add_settlement(self, pos, boundary=None, active=True, degradation_dist=None):
        name = 1 ####
        if boundary is None:
            boundary = Point()
        if degradation_dist is None:
            degradation_dist = Eternal()
        self.G.add_node(
            name,
            pos=pos,
            boundary=boundary
        )
    

if __name__ == "__main__":
    L = Links()
    L.add_settlement(pos=[0,0], boundary=None)
    print(L.G.nodes[1]['pos'])