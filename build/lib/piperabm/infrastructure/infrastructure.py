import networkx as nx
import numpy as np
import uuid
from copy import deepcopy

from piperabm.tools.coordinate import distance as ds
from piperabm.infrastructure.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.infrastructure.heuristic_paths import HeuristicPaths
from piperabm.tools.serializers import nx_serialize, nx_deserialize


class Infrastructure(Graphics):

    type = 'infrastructure'

    def __init__(self):
        super().__init__()
        self.G = nx.Graph()
        self.model = None # Binding
        self.baked_streets = True
        self.baked_neighborhood = True
        self.heuristic_paths = HeuristicPaths()

    @property
    def baked(self):
        result = False
        if self.baked_streets is True and \
        self.baked_neighborhood is True:
            result = True
        return result

    def check_id(self, id):
        if id is None:
            id = self.new_id()
        else:
            if id in self.all_id:
                id = self.new_id()
                print("id already exists. replaced with new id.")
        return id

    def new_id(self):
        return uuid.uuid4().int
    
    @property
    def all_id(self):
        return self.nodes_id + self.edges_id
    
    @property
    def all(self):
        return self.all_id

    @property
    def nodes_id(self):
        """
        Return all nodes id
        """
        return list(self.G.nodes())

    @property
    def nodes(self):
        return self.nodes_id
    
    @property
    def edges(self):
        return self.edges_id

    @property
    def edges_id(self):
        """
        Return all edges id
        """
        result = []
        edges = self.edges_ids
        for ids in edges:
            id = self.edge_id(*ids)
            result.append(id)
        return result

    @property
    def edges_ids(self):
        """
        Return all edges ids
        """
        return list(self.G.edges())

    def edge_ids(self, id: int):
        """
        Get edge id_1 and id_2 (both ends) based on its id
        """
        result = None
        for id_1, id_2 in self.G.edges():
            if self.edge_id(id_1, id_2) == id:
                result = [id_1, id_2]
                break
        return result
    
    def edge_id(self, id_1: int, id_2: int) -> int:
        """
        Get edge id based on its id_1 and id_2 (both ends)
        """
        result = None
        if self.G.has_edge(id_1, id_2):
            edge = self.G.edges[id_1, id_2]
            result = edge['id']
        return result
    
    def node_attr(self, id: int, attr: str, default=None):
        return self.G.nodes[id].get(attr, default)

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
    
    def has_edge(self, id: int = None, ids: list = None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        return self.G.has_edge(*ids)

    def has_node(self, id: int):
        return self.G.has_node(id)
    
    def remove_edge(self, id: int = None, ids: list = None, report: bool = False):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        if report is True:
            print(f">>> {self.edge_type(ids=ids)} edge at {self.pos(ids[0])} - {self.pos(ids[1])} removed.")
        self.G.remove_edge(*ids)

    def remove_node(self, id, report: bool = False):
        if report is True:
            print(f">>> {self.node_type(id=id)} node at position {self.pos(id)} removed.")
        self.G.remove_node(id)

    def adjacents_ids(self, id):
        """
        All edges from a node
        """
        return list(self.G.edges(id))

    def replace_node(self, id, new_id, report=False):
        # Find all adjacent edges
        edges_ids = self.adjacents_ids(id)
        # Apply change to adjacent edges
        for edge_ids in edges_ids:
            # Create new edge
            if edge_ids[0] == id:
                new_edge_ids = [new_id, edge_ids[1]]
            else:
                new_edge_ids = [edge_ids[0], new_id]
            type = self.edge_type(ids=edge_ids)
            length = ds.point_to_point(
                    self.pos(new_edge_ids[0]),
                    self.pos(new_edge_ids[1])
                )
            degradation = self.edge_degradation(ids=edge_ids)
            self.G.add_edge(
                new_edge_ids[0],
                new_edge_ids[1],
                id=self.edge_id(*edge_ids),
                length=length,
                adjusted_length=self.calculate_adjusted_length(length, degradation),
                type=type,
                degradation=degradation,
            )
            if report is True:
                print(f">>> {type} edge at positions {self.pos(new_edge_ids[0])} - {self.pos(new_edge_ids[1])} added.")
            # Remove old edge
            self.remove_edge(ids=edge_ids, report=report)
        # Remove old node
        self.remove_node(id, report=report)

    def adjustment_factor(self, degradation: float):
        k = 1000
        return float(np.exp(degradation / k))

    def calculate_adjusted_length(self, length: float, degradation: float) -> float:
        return length * self.adjustment_factor(degradation)
    
    def adjusted_length(self, id: int = None, ids: int = None, new_val: float = None):
        if id is not None and ids is None:
            ids = self.edge_ids(id)
        if new_val is None:
            return float(self.G[ids[0]][ids[1]]['adjusted_length'])
        else:
            self.G[ids[0]][ids[1]]['adjusted_length'] = new_val

    @property
    def junctions(self):
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'junction']
        except:
            return []
        
    @property
    def nonjunctions(self):
        return self.homes + self.markets    
        
    @property
    def homes(self):
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'home']
        except:
            return []

    @property
    def markets(self):
        try:
            return [n for n, attr in self.G.nodes(data=True) if attr.get('type') == 'market']
        except:
            return []
    
    @property
    def streets_ids(self):
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'street']
        except:
            return []
        
    @property
    def streets_id(self):
        try:
            return [self.G[u][v]['id'] for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'street']
        except:
            return []
    
    @property
    def streets(self):
        return self.streets_id
    
    @property
    def neighborhood_accesses_ids(self):
        try:
            return [(u, v) for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'neighborhood_access']
        except:
            return []

    @property
    def neighborhood_accesses_id(self):
        try:
            return [self.G[u][v]['id'] for u, v, attr in self.G.edges(data=True) if attr.get('type') == 'neighborhood_access']
        except:
            return []

    @property
    def neighborhood_accesses(self):
        return self.neighborhood_accesses_id

    def add_junction(
        self,
        pos: list,
        id: int = None,
        name: str = '',
        report: bool = False
    ):
        type = 'junction'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1]
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id
    
    def add_home(
        self,
        pos: list,
        id: int = None,
        name: str = '',
        report: bool = False
    ):
        type = 'home'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1]
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id
    
    def add_market(
        self,
        pos: list,
        food: float = 0,
        water: float = 0,
        energy: float = 0,
        id: int = None,
        name: str = '',
        report: bool = False,
    ):
        type = 'market'
        id = self.check_id(id)
        self.G.add_node(
            id,
            name=name,
            type=type,
            x=pos[0],
            y=pos[1],
            food=food,
            water=water,
            energy=energy,
            enough_food=deepcopy(food),
            enough_water=deepcopy(water),
            enough_energy=deepcopy(energy),
            balance=0,
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} node at position {pos} added.")
        return id

    def add_street(
        self,
        pos_1: list,
        pos_2: list,
        id: int = None,
        name: str = '',
        degradation: float = 0,
        report: bool = False
    ):
        type = 'street'
        id_1 = self.add_junction(pos=pos_1)
        id_2 = self.add_junction(pos=pos_2)
        id = self.check_id(id)
        length = ds.point_to_point(pos_1, pos_2)
        self.G.add_edge(
            id_1,
            id_2,
            id=id,
            name=name,
            length=length,
            adjusted_length=self.calculate_adjusted_length(length, degradation),
            type=type,
            degradation=degradation
        )
        self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} edge at positions {pos_1}-{pos_2} added.")
        return id
    
    def add_neighborhood_access(
        self,
        id_1: list,
        id_2: list,
        id: int = None,
        name: str = '',
        degradation: float = 0,
        report: bool = False
    ):
        type = 'neighborhood_access'
        id = self.check_id(id)
        length = ds.point_to_point(self.pos(id_1), self.pos(id_2))
        self.G.add_edge(
            id_1,
            id_2,
            id=id,
            name=name,
            length=length,
            adjusted_length=self.calculate_adjusted_length(length, degradation),
            type=type,
            degradation=degradation
        )
        #self.baked_streets = False
        self.baked_neighborhood = False
        if report is True:
            print(f">>> {type} edge at positions {self.pos(id_1)} - {self.pos(id_2)} added.")
        return id
    
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

    def is_isolate(self, id):
        return nx.is_isolate(self.G, id)

    def filter_nodes_closer_than(self, id: int, nodes: list, distance: float):
        result = []
        for node_id in nodes:
            if distance >= self.heuristic_paths.estimated_distance(id_start=id, id_end=node_id):
                result.append(node_id)
        return result
    
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

    def impact(self, edges_ids: list = []):
        if self.baked is False:
            print("First bake the model")
            raise ValueError
        for edge_ids in edges_ids:
            self.remove_edge(ids=edge_ids)
            id_1 = edge_ids[0]
            id_2 = edge_ids[1]
            if self.node_type(id=id_1) == 'junction' and \
                self.is_isolate(id=id_1):
                self.remove_node(id=id_1)
            if self.node_type(id=id_2) == 'junction' and \
                self.is_isolate(id=id_2):
                self.remove_node(id=id_2)

    def top_degraded_edges(self, percent: float = 0):
        edges_ids = self.streets_ids
        total_length = 0
        edges_info = []
        for edge_ids in edges_ids:
            length = self.edge_length(ids=edge_ids)
            total_length += length
            edge_info = {
                'ids': edge_ids,
                'degradation': self.edge_degradation(ids=edge_ids),
                'length': length
            }
            edges_info.append(edge_info)
        sorted_edges_info = sorted(edges_info, key=lambda x: x['degradation'], reverse=True)
        remaining_length = (percent / 100) * total_length
        result = []
        for edge_info in sorted_edges_info:
            remaining_length -= edge_info['length']
            if remaining_length < 0:
                break
            else:
                result.append(edge_info['ids'])
        return result

    @property
    def stat(self):
        result = {
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
        return result
    
    def __str__(self):
        stat = self.stat
        txt = ''
        for category in stat:
            for name in stat[category]:
                txt += f"# {name}: {str(stat[category][name])}" + "\n"
        txt = txt[:-1]
        return txt
    
    def update(self, duration: float):
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
        
    def serialize(self):
        dictionary = {}
        dictionary['G'] = nx_serialize(self.G)
        dictionary['heuristic_paths'] = self.heuristic_paths.serialize()
        dictionary['baked_streets'] = self.baked_streets
        dictionary['baked_neighborhood'] = self.baked_neighborhood
        dictionary['type'] = self.type
        return dictionary
    
    def deserialize(self, dictionary):
        self.G = nx_deserialize(dictionary['G'])
        self.heuristic_paths.deserialize(dictionary['heuristic_paths'])
        self.baked_streets = dictionary['baked_streets']
        self.baked_neighborhood = dictionary['baked_neighborhood']


if __name__ == "__main__":

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
