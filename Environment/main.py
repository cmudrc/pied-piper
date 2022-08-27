from html import entities
from graphics import *
import numpy as np

''' An entity represents a major producer/user of resources, such as cities '''
class Entity():
    def __init__(
        self,
        name = None,
        location = [0, 0],
        source = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        demand = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        deficiency_current = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        deficiency_max = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        storage_current = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },
        storage_max = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            },    
        neighbors = list()
            ):
        self.name = str(name) # Entity's name
        self.location = location # a list in form of [x, y], representing the location of the entity on the map
        self.source = source # a dictionary containing the amount of source for {water, energy, food} in the entity
        self.demand = demand # a dictionary containing the amount of demand for {water, energy, food} in the entity
        self.deficiency_current = deficiency_current # a dictionary containing the current amount of deficiency for {water, energy, food} in the entity
        self.deficiency_max = deficiency_max # a dictionary containing the maximum deficiency possible for each source {water, energy, food} in the entity
        self.storage_current = storage_current # a dictionary containing the current amount of storage for {water, energy, food} in the entity
        self.storage_max = storage_max # a dictionary containing the maximum amount of storage for {water, energy, food} in the entity

        self.neighbors_list = neighbors # a list of neighboring entities

    def __add__(self, other):
        m = Model()
        m.add_entity(self)
        m.add_entity(other)
        return m

    def __str__(self):
        return self.name

''' main class '''
class Model():
    def __init__(self, name=None):
        self.name = name
        self.entities = list() # a list containing all Entitys of the graph
        self.graph = None # matrix representation of the graph
        ''' variables for summations and totals '''
        self.all_resources_names = ['water', 'energy', 'food']
        self.all_entities_names = list() # a list containing names of self.entities elements
        self.reset_totals()

    def add_entity(self, entity):
        ''' adds single Entity '''
        self.entities.append(entity)
        self.all_entities_names.append(entity.name)
        self.calculate_totals()

    def add_entities(self, entities=list()):
        ''' add entities in batch '''
        for entity in entities:
            self.add_entity(entity)

    def validate_entities(self):
        ''' checks for the validity of Entitys connections '''
        final_result = False
        result_list = list() # if all elements are True, the final result will be True
        for entity in self.entities:
            for entity_neighbor_name in entity.neighbors_list:
                if entity_neighbor_name in self.all_entities_names:
                    result_list.append(True)
                else:
                    print(
                        entity_neighbor_name +
                        " is not a valid neighbor for " +
                        entity.name
                    )
                    result_list.append(False)
        if False in result_list:
            final_result = False
        return final_result

    def reset_totals(self):
        self.total_source = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # total source for all entities in the model
        self.total_demand = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # total demand for all entities in the model
        self.total_deficiency_current = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # total current storage for all entities in the model
        self.total_deficiency_max = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # totam maximum storage for all enitites in the model
        self.total_storage_current = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # total current storage for all entities in the model
        self.total_storage_max = {
            'water' : 0,
            'energy' : 0,
            'food' : 0,
            } # total maximum storage for all enitites in the model

    def calculate_totals(self):
        ''' calculates the total value for resources in the model for all entities '''
        self.reset_totals()
        for entity in self.entities:
            for resource in self.all_resources_names:
                self.total_source[resource] += entity.source[resource]
                self.total_demand[resource] += entity.demand[resource]
                self.total_deficiency_current[resource] += entity.deficiency_current[resource]
                self.total_deficiency_max[resource] += entity.deficiency_max[resource]
                self.total_storage_current[resource] += entity.storage_current[resource]
                self.total_storage_max[resource] += entity.storage_max[resource]

    def to_matrix(self, directed=False):
        ''' calculates the matrix representaion of graph '''
        matrix = None
        if directed:
            matrix = np.zeros(
                (
                    len(self.all_resources_names),
                    len(self.entities)*3,
                    len(self.entities)*3
                )
            ) # each entity is devided into three nodes: source, demand, and storage
            for id, resource in enumerate(self.all_resources_names):
                for pk, entity in enumerate(self.entities):
                    value = entity.source[resource] + entity.storage[resource] - entity.demand[resource]
        else:
            matrix = np.zeros(
                (
                    len(self.all_resources_names),
                    len(self.entities),
                    len(self.entities)
                )
            ) # each entity is devided into three nodes: source, demand, and storage
            for id, resource in enumerate(self.all_resources_names):
                for pk, entity in enumerate(self.entities):
                    value = entity.source[resource] + entity.storage[resource] - entity.demand[resource] ####
        return matrix

    def show(self, directed=False):
        ''' shows graph representation of state '''
        if directed:
            pass
        else:
            x = list()
            y = list()
            titles = list()
            node_sizes = list()
            for entity in self.entities:
                x.append(entity.location[0])
                y.append(entity.location[1])
                titles.append(entity.name)
                node_size = node_size_calculator(
                    entity = entity,
                    total_source = self.total_source,
                    total_demand = self.total_demand,
                    all_resources_names=self.all_resources_names
                    )
                node_sizes.append(node_size)
            show_graph(x, y, titles=titles, node_sizes=node_sizes)

    def __str__(self):
        return self.name

    def save(self, model_name):
        ### to be added
        pass

    def load(self, model_name):
        ### to be added
        pass


if __name__ == "__main__":
    from samples import e_1, e_2
    
    #m = Model()
    #m.add_entity(e_1)
    #m.add_entity(e_2)
    m = e_1 + e_2 # alternative to above

    m.validate_entities()
    m.show()
