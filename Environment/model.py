import numpy as np
import json

from graph import Node, Graph
from economy import Order, Economy


class Link():
    ''' represents a connection between two entities for a certain resource '''

    def __init__(
        self,
        start=None,
        end=None,
        active=True,
        chance=1,
        price_factor=1,
        max_discharge=None
    ):
        self.start = start  # the starting point
        self.end = end  # the end point
        # whether this connections is active, (True/False)
        self.active = active
        # chance of working properly, (0 <= chance <= 1)
        self.chance = chance
        # shows how hard it is to transfer this resource by this route
        self.price_factor = price_factor
        # maximum amount for discharge allowed in the link per timestep
        self.max_discharge = max_discharge


class Resource():
    ''' represents resources, has to be added to an instance of entity class '''

    def __init__(
        self,
        name,
        source=0,
        demand=0,
        deficiency_current=0,
        deficiency_max=0,
        storage_current=0,
        storage_max=0,
        connections=None
    ):
        self.name = name  # resource name
        self.source = source  # the amount of source in each timestep
        self.demand = demand  # the amount of demand in each timestep
        # current deficiency of resource
        self.deficiency_current = deficiency_current
        # maximum deficiency of resource that can be handled by the entity
        self.deficiency_max = deficiency_max
        # current amount of storage for the resource
        self.storage_current = storage_current
        self.storage_max = storage_max  # maximum amount of storage possible

        self.connections = list()  # list of instances of Connection class
        if connections is not None:
            for connection in connections:
                self.connections.append(connection)

    def is_alive(self):
        ''' checks whether the owner of this resource is still alive or not '''
        result = False
        if float(self.deficiency_current) <= float(self.deficiency_max):
            result = True
        return result


class Entity():
    ''' An entity represents a major producer/user/storer of resources, such as cities '''

    def __init__(
        self,
        name,
        location=[0, 0],
        resources=None
    ):
        self.name = name
        self.location = location
        self.resources = list()

        if resources is not None:  # expects list instance
            for resource in resources:
                self.add_resource(new_resource=resource)

    def add_resource(self, new_resource):
        ''' adds an instance of resource to the entity '''
        for link in new_resource.connections:
            link.start = self.name
        self.resources.append(new_resource)

    def is_alive(self):
        ''' checks whether the entity is still alive or not '''
        result = True
        for resource in self.resources:
            if not resource.is_alive():
                result = False
        return result

    def __str__(self):
        return self.name


class Model():
    ''' main class for representing environment '''

    def __init__(
        self,
        name=None,
        entities=None
    ):
        self.name = name

        self.entities = list()
        if entities is not None:
            if isinstance(entities, list):
                for entity in entities:
                    self.entities.append(entity)
            else:
                self.entities.append(entities)

        self.distance = None
        self.all_resources_names = None

    def distance_matrix_calculate(self):
        ''' generates the distance matrix '''
        size = len(self.entities)
        distance_matrix = np.zeros((size, size))
        for i, entity_i in enumerate(self.entities):
            for j, entity_j in enumerate(self.entities):
                x_1 = entity_i.location[0]
                y_1 = entity_i.location[1]
                x_2 = entity_j.location[0]
                y_2 = entity_j.location[1]
                dist = np.sqrt(
                    np.power((x_1 - x_2), 2)
                    + np.power((y_1 - y_2), 2)
                )
                distance_matrix[i, j] = dist
        self.distance = distance_matrix

    def analyze(self):
        ''' it analyzes the model '''

        ''' dynamic programming reutines '''
        self.distance_matrix_calculate()
        self.find_all_resources_names()

        ''' running checkups '''
        final_result = True
        if not self.validate_entities_connections():
            final_result = False

        return final_result

    def validate_entities_connections(self):
        ''' checks for the validity of entities connections '''
        final_result = True
        #result_list = list() # if all elements are True, the final result will be True
        all_entity_names = [x.name for x in self.entities]
        for entity in self.entities:
            for resource in entity.resources:
                for link in resource.connections:
                    if link.end not in all_entity_names:
                        print(
                            "for "
                            + resource.name
                            + ":\n"
                            + link.end
                            + " is not a valid neighbor for "
                            + entity.name
                        )
                        final_result = False
        return final_result

    def to_json(self):
        ''' converts all the information within the model to json '''
        entities_list = list()
        if self.entities is None or len(self.entities) == 0:
            pass
        else:
            for entity in self.entities:
                entity_dict = dict()
                entity_dict['name'] = entity.name
                entity_dict['location'] = entity.location

                resources_list = list()
                if entity.resources is None or len(entity.resources) == 0:
                    pass
                else:
                    for resource in entity.resources:
                        resource_dict = dict()
                        resource_dict['name'] = resource.name
                        resource_dict['source'] = resource.source
                        resource_dict['demand'] = resource.demand
                        resource_dict['deficiency_current'] = resource.deficiency_current
                        resource_dict['deficiency_max'] = resource.deficiency_max
                        resource_dict['storage_current'] = resource.storage_current
                        resource_dict['storage_max'] = resource.storage_max

                        connections_list = list()
                        if resource.connections is None or len(resource.connections) == 0:
                            pass
                        else:
                            for link in resource.connections:
                                link_dict = dict()
                                link_dict['start'] = link.start
                                link_dict['end'] = link.end
                                link_dict['active'] = link.active
                                link_dict['chance'] = link.chance
                                link_dict['price_factor'] = link.price_factor
                                connections_list.append(link_dict)

                        resource_dict['connections'] = connections_list
                        resources_list.append(resource_dict)

                entity_dict['resources'] = resources_list
                entities_list.append(entity_dict)

        result_dict = {
            "name": self.name,
            "entities": entities_list
        }
        return json.dumps(result_dict)

    def from_json(self, txt):
        ''' loads all the model information from json '''
        j = json.loads(txt)
        self.name = j['name']
        self.entities = list()
        for entity in j['entities']:
            resources_list = list()
            for resource in entity['resources']:
                links_list = list()
                for link in resource['connections']:
                    new_link = Link(
                        start=link['start'],
                        end=link['end'],
                        active=link['active'],
                        chance=link['chance'],
                        price_factor=link['price_factor']
                    )
                    links_list.append(new_link)
                r = Resource(
                    name=resource['name'],
                    source=resource['source'],
                    demand=resource['demand'],
                    deficiency_current=resource['deficiency_current'],
                    deficiency_max=resource['deficiency_max'],
                    storage_current=resource['storage_current'],
                    storage_max=resource['storage_max'],
                    connections=links_list
                )
                resources_list.append(r)
            e = Entity(
                name=entity['name'],
                location=entity['location'],
                resources=resources_list
            )
            self.entities.append(e)

    def find_all_resources_names(self):
        ''' list names for all resources '''
        all_resources_names = list()
        for entity in self.entities:
            for resource in entity.resources:
                if resource.name not in all_resources_names:
                    all_resources_names.append(resource.name)
        self.all_resources_names = all_resources_names

    def to_graph(self, resource_name):
        ''' converts entites into source/demand/storage nodes '''
        g = Graph()
        for entity in self.entities:
            for resource in entity.resources:
                if resource.name == resource_name:
                    ''' nodes within the entity '''
                    inner_node_source = Node(
                        name=entity.name + '_' + 'source',
                        type='source',
                        neighbors={
                            entity.name + '_' + 'demand': None,
                            entity.name + '_' + 'storage': None
                        }
                    )
                    g.add_node(inner_node_source)
                    inner_node_demand = Node(
                        name=entity.name + '_' + 'demand',
                        type='demand'
                    )
                    g.add_node(inner_node_demand)
                    inner_node_storage = Node(
                        name=entity.name + '_' + 'storage',
                        type='storage',
                        neighbors={
                            entity.name + '_' + 'demand': None
                        }
                    )
                    g.add_node(inner_node_storage)

        for entity in self.entities:
            for resource in entity.resources:
                if resource.name == resource_name:
                    ''' nodes out of the entity '''
                    for link in resource.connections:
                        for node in g.nodes:
                            if entity.name + '_' + 'source' == node.name:  # same starting point
                                # value to be saved in graph
                                node.neighbors[link.end +
                                               '_' + 'demand'] = None
                                node.neighbors[link.end +
                                               '_' + 'storage'] = None
                            elif entity.name + '_' + 'demand' == node.name:
                                pass
                            elif entity.name + '_' + 'storage' == node.name:
                                node.neighbors[link.end +
                                               '_' + 'demand'] = None
        return g

    def update_step(self):
        eco = Economy()
        eco.orders = list()
        eco.info = dict()
        # sources and demands added to economy
        # results are readed and updated
        # add storage units as sources and demands
        # results are readed and updated
        def list_all_demands_from_sources(self):
            for entity in self.entities:
                for resource in entity.resources:
                    for link in resource.connections:
                        pass

    def __str__(self):
        return self.name


if __name__ == "__main__":
    from samples import e_1, e_2

    m = Model(entities=[e_1, e_2])
    m.analyze()
    #print(m.validate_entities_connections())
    #print([node.name for node in m.to_graph('water').nodes])
    print(m.to_graph('water').to_matrix())