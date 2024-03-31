import networkx as nx
import uuid
import matplotlib.pyplot as plt

from piperabm.object import PureObject
from piperabm.infrastructure_new import Junction
from piperabm.tools.coordinate import distance as ds
from piperabm.infrastructure_new.grammar import Grammar
from piperabm.infrastructure_new.items.deserialize import infrastructure_deserialize
from piperabm.infrastructure_new.style import infrastructure_style
#from piperabm.infrastructure.paths import Paths
#from piperabm.graphics import Graphics


class Infrastructure(PureObject):

    def __init__(self, model=None, proximity_radius=1):
        super().__init__()
        self.G = nx.Graph()
        self.model = model # Bind
        self.library = {}
        self.proximity_radius = proximity_radius
        self.baked = True

    def get(self, id: int):
        """
        Get object by its id
        """
        return self.library[id]

    @property
    def all(self):
        """
        Return id of all items
        """
        return self.library.keys()
    
    @property
    def new_id(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        result = None
        while True:
            new_id = uuid.uuid4().int
            if self.has_id(new_id) is False:
                result = new_id
                break
        return result
    
    def has_id(self, id: int) -> bool:
        """
        Check if the id already exists
        """
        result = False
        if id in self.all:
            result = True
        return result
    
    def add(self, object, id: int = None):
        """
        Add new object to infrastructure
        """
        # ID
        if id is None:
            id = self.new_id
        else:
            if self.has_id(id) is True:
                id = self.new_id
        # Add Node
        if object.category == "node":
            self.library[id] = object
            self.G.add_node(id)
        # Add Edge
        elif object.category == "edge":
            junction_1 = Junction(pos=object.pos_1)
            junction_2 = Junction(pos=object.pos_2)
            id_1 = self.add(junction_1)
            id_2 = self.add(junction_2)
            self.G.add_edge(
                id_1,
                id_2,
                id=id
            )
            self.library[id] = object
        else:
            print("Object type not recognized.")
            raise ValueError
        # Baked
        self.baked = False
        return id
    
    def find(self, input, ids: list = None):
        if isinstance(input, list):
            return self.find_node_by_pos(pos=input, ids=ids)
    
    def find_node_by_pos(self, pos: list, ids: list = None):
        min_id = None
        min_distance = None
        if ids is None:  # All nodes
            ids = self.nodes_id
        for id in ids:
            object = self.get(id)
            distance = ds.point_to_point(object.pos, pos)
            if min_distance is None or \
            min_distance > distance:
                min_distance = distance
                min_id = id
        return min_id
    
    def edge_id(self, id_1: int, id_2: int):
        """
        Get edge id based on its id_1 and id_2 (both ends)
        """
        result = None
        if self.G.has_edge(id_1, id_2):
            edge = self.G.edges[id_1, id_2]
            result = edge['id']
        return result
    
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
    
    @property
    def nodes_id(self):
        """
        Return all nodes id
        """
        return list(self.G.nodes())

    @property
    def edges_ids(self):
        """
        Return all edges ids
        """
        return list(self.G.edges())
    
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
    
    def filter_type(self, type, ids: list = None):
        """
        Filter a list of objects id based on their type
        """
        result = []
        if ids is None:  # All nodes
            ids = self.all
        for id in ids:
            object = self.get(id)
            if object.type == type:
                result.append(id)
        return result
    
    def edges_closer_than(self, pos: list, max_distance: float, edges_id: list = None):
        result = []
        if edges_id is None:
            edges_id = self.edges_id
        for edge_id in edges_id:
            edge_object = self.get(edge_id)
            distance = ds.point_to_point(
                point_1=pos,
                point_2=edge_object.pos_1
            )
            if distance <= max_distance:
                result.append(edge_id)
            else:
                distance = ds.point_to_point(
                    point_1=pos,
                    point_2=edge_object.pos_2
                )
                if distance <= max_distance:
                    result.append(edge_id)
        return result
    
    @property
    def nonjunctions(self):
        return self.homes + self.markets
    
    @property
    def junctions(self):
        return self.filter_type(type='junction')
    
    @property
    def homes(self):
        return self.filter_type(type='home')
    
    @property
    def markets(self):
        return self.filter_type(type='market')

    @property
    def streets(self):
        return self.filter_type(type='street')
    
    @property
    def neighborhood_accesses(self):
        return self.filter_type(type='neighborhood_access')
    
    def adjacents_id(self, id):
        """
        All edges from a node
        """
        result = []
        edges_ids = self.adjacents_ids(id)
        for edge_ids in edges_ids:
            edge_id = self.edge_id(*edge_ids)
            result.append(edge_id)
        return result

    def adjacents_ids(self, id):
        """
        All edges from a node
        """
        return list(self.G.edges(id))
    
    def is_isolate(self, id):
        return nx.is_isolate(self.G, id)

    def replace_node(self, id, new_id):
        """
        Replace node id in all edges containing it
        """
        # Find all adjacent edges
        edges_ids = self.adjacents_ids(id)
        # Apply change to adjacent edges
        for edge_ids in edges_ids:
            # Create new edge
            edge_id = self.edge_id(*edge_ids)
            if edge_ids[0] == id:
                new_edge_ids = [new_id, edge_ids[1]]
            else:
                new_edge_ids = [edge_ids[0], new_id]
            self.G.add_edge(
                new_edge_ids[0],
                new_edge_ids[1],
                id=edge_id
            )
            # Update object
            edge_object = self.get(edge_id)
            new_node_object = self.get(new_id)
            node_object = self.get(id)
            if edge_object.pos_1 == node_object.pos:
                edge_object.pos_1 = new_node_object.pos
            elif edge_object.pos_2 == node_object.pos:
                edge_object.pos_2 = new_node_object.pos
            # Remove old edge
            self.G.remove_edge(*edge_ids)
        # Remove old node
        self.remove_node(id)
        self.delete_object(id)

    def delete_object(self, id):
        del self.library[id]

    def remove_node(self, id):
        self.G.remove_node(id)

    def remove_edge(self, id):
        ids = self.edge_ids(id)
        self.G.remove_edge(*ids)

    def bake(self, save=False, report=False):
        grammar = Grammar(infrastructure=self, save=save)
        grammar.apply(report=report)
        print("Baking is done.")

    def to_plt(self):
        # Nodes
        pos_dict = {}
        node_color_list = []
        node_size_list = []
        node_label_dict = {}
        nodes = self.nodes_id
        for node_index in nodes:
            object = self.get(node_index)
            # Position
            pos_dict[node_index] = object.pos
            # Color
            color = infrastructure_style['node'][object.type]['color']
            node_color_list.append(color)
            # Size
            size = infrastructure_style['node'][object.type]['radius']
            node_size_list.append(size)
            # Label
            node_label_dict[node_index] = object.name

        # Edges
        edge_color_list = []
        edges_ids = []
        edges_id = self.edges_id
        for edge_id in edges_id:
            edge_ids = self.edge_ids(edge_id)
            edges_ids.append(edge_ids)
            object = self.get(edge_id)
            # Color
            color = infrastructure_style['edge'][object.type]['color']
            edge_color_list.append(color)

        # Draw
        nx.draw_networkx(
            self.G,
            nodelist=nodes,
            pos=pos_dict,
            node_color=node_color_list,
            node_size=node_size_list,
            labels=node_label_dict,
            font_size=infrastructure_style['font'],
            edgelist=edges_ids,
            edge_color=edge_color_list
        )

    def show(self):
        ax = plt.gca()
        ax.set_aspect("equal")
        self.to_plt()
        plt.show()

    def serialize(self):
        dictionaty = {}
        library_serialized = {}
        for id in self.library:
            library_serialized[id] = self.library[id].serialize()
        dictionaty['library'] = library_serialized
        dictionaty['G'] = nx.to_dict_of_dicts(self.G)
        dictionaty['proximity_radius'] = self.proximity_radius
        dictionaty['baked'] = self.baked
        return dictionaty

    def deserialize(self, dictionaty):
        for id in dictionaty['library']:
            object = infrastructure_deserialize(dictionaty['library'][id])
            self.library[id] = object
        self.G = nx.from_dict_of_dicts(dictionaty['G'])
        self.proximity_radius = dictionaty['proximity_radius']
        self.baked = dictionaty['baked']


if __name__ == "__main__":

    from piperabm.infrastructure_new import Street

    infrastructure = Infrastructure(
        model=None,
        proximity_radius=1
    )
    street = Street(pos_1=[0, 0], pos_2=[10, 10])
    infrastructure.add(street)
    print(infrastructure)