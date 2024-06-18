import networkx as nx

from piperabm.infrastructure.query import Query
from piperabm.infrastructure.degradation import Degradation
from piperabm.infrastructure.serialize import Serialize
from piperabm.infrastructure.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.infrastructure.heuristic_paths import HeuristicPaths


class Infrastructure(
    Query,
    Degradation,
    Serialize,
    Graphics
):

    type = 'infrastructure'

    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.model = None # Binding
        self.baked_streets = True
        self.baked_neighborhood = True
        self.heuristic_paths = HeuristicPaths()

    @property
    def baked(self) -> bool:
        """
        Check if the network is fully baked
        """
        result = False
        if self.baked_streets is True and \
        self.baked_neighborhood is True:
            result = True
        return result

    def node_type(self, id):
        return self.node_attr(id, 'type')
    
    def node_name(self, id):
        return self.node_attr(id, 'name', None)
    
    def node_pos(self, id):
        return [float(self.node_attr(id, 'x', None)), float(self.node_attr(id, 'y', None))]
    
    def pos(self, id):
        """
        Alias for node_pos method
        """
        return self.node_pos(id)

    def edge_type(self, id=None, ids=None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        return self.G.edges[*ids].get('type', None)
    
    def edge_length(self, id: int = None, ids: list = None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        return float(self.G.edges[*ids].get('length', None))   
    
    def edge_degradation(self, id: int = None, ids: list = None, new_val: float = None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        if new_val is None:
            return float(self.G.edges[*ids].get('degradation', None))
        else:
            self.G[ids[0]][ids[1]]['degradation'] = new_val
    
    def adjusted_length(self, id: int = None, ids: int = None, new_val: float = None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        if new_val is None:
            return float(self.G[ids[0]][ids[1]]['adjusted_length'])
        else:
            self.G[ids[0]][ids[1]]['adjusted_length'] = new_val
    
    def balance(self, id: int, new_val: float = None):
        if new_val is None:
            return self.G.nodes[id].get('balance', None)
        else:
            self.G.nodes[id]['balance'] = new_val
    
    def food(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('food', None))
        else:
            if new_val < 0:
                new_val = 0
            self.G.nodes[id]['food'] = new_val

    def water(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('water', None))
        else:
            if new_val < 0:
                new_val = 0
            self.G.nodes[id]['water'] = new_val

    def energy(self, id: int, new_val: float = None):
        if new_val is None:
            return float(self.G.nodes[id].get('energy', None))
        else:
            if new_val < 0:
                new_val = 0
            self.G.nodes[id]['energy'] = new_val

    def enough_food(self, id: int):
        return self.G.nodes[id].get('enough_food', None)
    
    def enough_water(self, id: int):
        return self.G.nodes[id].get('enough_water', None)

    def enough_energy(self, id: int):
        return self.G.nodes[id].get('enough_energy', None)
    
    def bake(
            self,
            report: bool = False,
            proximity_radius: float = 1,
            search_radius: float = None
        ):
        if self.baked is False:
            grammar = Grammar(
                infrastructure=self,
                proximity_radius=proximity_radius,
                search_radius=search_radius
            )
            grammar.apply(report=report)
            if report is True:
                print("baking is done.")
            self.heuristic_paths.create(infrastructure=self)
        else:
            print("already baked.")

    def update(self, duration: float):
        """
        Update the network
        """
        # Update degradation from climate change
        '''
        for edge_ids in self.streets_ids:
            delta = self.model.thawing * duration
            degradation = self.edge_degradation(ids=edge_ids)
            new_degradation = degradation + delta
            self.edge_degradation(ids=edge_ids, new_val=new_degradation)
        '''
        # Update adjusted length
        for edge_ids in self.edges_ids:
            length = self.edge_length(ids=edge_ids)
            degradation = self.edge_degradation(ids=edge_ids)
            self.adjusted_length(ids=edge_ids, new_val=self.calculate_adjusted_length(length, degradation))

    @property
    def stat(self):
        """
        Return stats of the network
        """
        return {
            'node': {
                'junction': len(self.junctions),
                'home': len(self.homes),
                'market': len(self.markets),
            },
            'edge': {
                'street': len(self.streets),
                'neighborhood_access': len(self.neighborhood_accesses),
            },
        }
    
    def __str__(self):
        """
        Return print-friendly stats of the network
        """
        stat = self.stat
        txt = ''
        for category in stat:
            for name in stat[category]:
                txt += f"# {name}: {str(stat[category][name])}" + "\n"
        txt = txt[:-1]
        return txt


if __name__ == "__main__":
    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 10])
    print(infrastructure)

'''
    from piperabm.model import Model

    model = Model()
    #infrastructure = Infrastructure(climate_change_degradation_rate=0.001)
    model.infrastructure.add_junction(pos=[1.2, 0.8], id=0)
    model.infrastructure.add_street(pos_1=[0, 0], pos_2=[2, 2], id=1)
    model.infrastructure.bake()
    #infrastructure.show()
    data = model.infrastructure.serialize()
    model_new = Model()
    model_new.infrastructure.deserialize(data)
    print(model.infrastructure.serialize() == model_new.infrastructure.serialize())

    

    #edge_ids = model.infrastructure.streets_ids[0]
    #print(model.infrastructure.adjusted_length(ids=edge_ids))
    #model.infrastructure.update(duration=100)
    #print(model.infrastructure.adjusted_length(ids=edge_ids))
'''
