import networkx as nx
import uuid

from piperabm.infrastructure_new import Junction
from piperabm.tools.coordinate import distance as ds


class Query:

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
    
    def object_type(self, id):
        object = self.get(id)
        return object.type
    
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