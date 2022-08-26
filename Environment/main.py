from graphics import *

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
        ''' variables for summations and totals '''
        self.all_entities_names = list() # a list containing names of self.Entitys elements
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
            ''' totals for water '''
            self.total_source['water'] += entity.source['water']
            self.total_demand['water'] += entity.demand['water']
            self.total_deficiency_current['water'] += entity.deficiency_current['water']
            self.total_deficiency_max['water'] += entity.deficiency_max['water']
            self.total_storage_current['water'] += entity.storage_current['water']
            self.total_storage_max['water'] += entity.storage_max['water']
            ''' totals for energy '''
            self.total_source['energy'] += entity.source['energy']
            self.total_demand['energy'] += entity.demand['energy']
            self.total_deficiency_current['energy'] += entity.deficiency_current['energy']
            self.total_deficiency_max['energy'] += entity.deficiency_max['energy']
            self.total_storage_current['energy'] += entity.storage_current['energy']
            self.total_storage_max['energy'] += entity.storage_max['energy']
            ''' totals for food '''
            self.total_source['food'] += entity.source['food']
            self.total_demand['food'] += entity.demand['food']
            self.total_deficiency_current['food'] += entity.deficiency_current['food']
            self.total_deficiency_max['food'] += entity.deficiency_max['food']
            self.total_storage_current['food'] += entity.storage_current['food']
            self.total_storage_max['food'] += entity.storage_max['food']

    def show(self):
        ''' shows graph representation of state '''
        x = list()
        y = list()
        for entity in self.entities:
            x.append(entity.location[0])
            y.append(entity.location[1])
        show_graph(x, y)    

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
