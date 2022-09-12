import json
from msilib import sequence
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab

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

        self.graph = dict() # a dictionary of {resource_name: graph} pairs
        self.detailed_graph = dict()
        self.all_types = ['source', 'demand', 'storage'] # a list of all node types

        ''' used for dynamic programming '''
        self.distance = None # distance matrix
        self.header_index_dict = None # matrix headers names
        self.price_factor = None # price_factor matrix
        self.max_discharge = None # max_discharge matrix
        self.all_resources_names = None # a list of all resources names

    def analyze(self):
        ''' it analyzes the model '''

        ''' dynamic programming reutines '''
        def find_all_resources_names(self):
            ''' list names for all resources '''
            all_resources_names = list()
            for entity in self.entities:
                for resource in entity.resources:
                    if resource.name not in all_resources_names:
                        all_resources_names.append(resource.name)
            self.all_resources_names = all_resources_names

        def distance_matrix_calculate(self):
            ''' generates the distance matrix and header_index_dict '''
            size = len(self.entities)
            distance_matrix = np.zeros((size, size))
            header_index_dict = dict()
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
                header_index_dict[entity_i.name] = i
            self.distance = distance_matrix # a matrix containing distance betnween nodes
            self.header_index_dict = header_index_dict # a dictionary of {name of rows (and column) : index}
        
        def price_factor_matrix_calculate(self):
            ''' generates the price_factor matrix '''
            size = len(self.entities)
            price_factor = dict()
            for index, entity in enumerate(self.entities):
                for resource in entity.resources:
                    price_factor_matrix = np.zeros((size, size))
                    for link in resource.connections:
                        end_index = self.header_index_dict[link.end]
                        price_factor_matrix[index, end_index] = link.price_factor
                    price_factor[resource.name] = price_factor_matrix
            self.price_factor = price_factor

        def max_discharge_matrix_calculate(self):
            ''' generates the max_discharge matrix '''
            size = len(self.entities)
            max_discharge = dict()
            for index, entity in enumerate(self.entities):
                for resource in entity.resources:
                    max_discharge_matrix = np.zeros((size, size))
                    for link in resource.connections:
                        end_index = self.header_index_dict[link.end]
                        max_discharge_matrix[index, end_index] = link.max_discharge
                    max_discharge[resource.name] = max_discharge_matrix
            self.max_discharge = max_discharge         

        distance_matrix_calculate(self) # generates the distance matrix
        find_all_resources_names(self) # list names for all resources
        price_factor_matrix_calculate(self)
        max_discharge_matrix_calculate(self)

        ''' running checkups '''
        def validate_entities_connections(self):
            ''' checks for the validity of entities connections '''
            final_result = True
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
        
        final_result = True
        if not validate_entities_connections(self):
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

    def to_graph(self, resource_name):
        ''' converts entities into nodes '''
        H = nx.MultiDiGraph(directed=True)
        for entity in self.entities:
            for resource in entity.resources:
                if resource.name == resource_name:
                    items = {
                        'location': entity.location,
                        'name': entity.name,
                        'source': resource.source,
                        'demand': resource.demand,
                        'deficiency_current': resource.deficiency_current,
                        'deficiency_max': resource.deficiency_max,
                        'storage_current': resource.storage_current,
                        'storage_max': resource.storage_max
                    }
                    H.add_node(entity.name, **items)
                    for link in resource.connections:
                        items = {
                            'active': link.active,
                            'chance': link.chance,
                            'price_factor': link.price_factor,
                            'max_discharge': link.max_discharge
                        }
                        H.add_edge(entity.name, link.end, **items)
        self.graph[resource_name] = H

    def to_detailed_graph(self, resource_name):
        ''' converts entites into source/demand/storage nodes '''
        G = nx.DiGraph(directed=True)
        H = self.graph[resource_name]
        for node in H.nodes:
            ''' adding the nodes '''
            node_unique_name = self.to_nametype(node, 'source')
            items = {
                'name': node,
                'type': 'source',
                'location': H.nodes[node]['location'],
                'source': H.nodes[node]['source']
            }
            G.add_node(node_unique_name, **items)
            node_unique_name = self.to_nametype(node, 'demand')
            items = {
                'name': node,
                'type': 'demand',
                'location': H.nodes[node]['location'],
                'demand': H.nodes[node]['demand']
            }
            G.add_node(node_unique_name, **items)
            node_unique_name = self.to_nametype(node, 'storage')
            items = {
                'name': node,
                'type': 'storage',
                'location': H.nodes[node]['location'],
                'storage_current': H.nodes[node]['storage_current'],
                'storage_max': H.nodes[node]['storage_max'],
            }
            G.add_node(node_unique_name, **items)

            ''' inner nodes connections within an entity '''
            node_unique_name_start = self.to_nametype(node, 'storage')
            node_unique_name_end = self.to_nametype(node, 'demand')
            items = {
                'active': True,
                'chance': 1,
                'price_factor': 1,
                'max_discharge': None
            }
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
            node_unique_name_start = self.to_nametype(node, 'source')
            node_unique_name_end = self.to_nametype(node, 'storage')
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
            node_unique_name_start = self.to_nametype(node, 'source')
            node_unique_name_end = self.to_nametype(node, 'demand')
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
        
        for edge in H.edges:
            ''' adding edges between nodes of different entities '''
            node_unique_name_start = self.to_nametype(edge[0], 'source')
            node_unique_name_end = self.to_nametype(edge[1], 'demand')
            items = {
                'active': H.edges[edge]['active'],
                'chance': H.edges[edge]['chance'],
                'price_factor': H.edges[edge]['price_factor'],
                'max_discharge': H.edges[edge]['max_discharge']
            }
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
            node_unique_name_start = self.to_nametype(edge[0], 'source')
            node_unique_name_end = self.to_nametype(edge[1], 'storage')
            items = {
                'active': H.edges[edge]['active'],
                'chance': H.edges[edge]['chance'],
                'price_factor': H.edges[edge]['price_factor'],
                'max_discharge': H.edges[edge]['max_discharge']                
            }
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
            node_unique_name_start = self.to_nametype(edge[0], 'storage')
            node_unique_name_end = self.to_nametype(edge[1], 'demand')
            items = {
                'active': H.edges[edge]['active'],
                'chance': H.edges[edge]['chance'],
                'price_factor': H.edges[edge]['price_factor'],
                'max_discharge': H.edges[edge]['max_discharge']                
            }
            G.add_edge(node_unique_name_start, node_unique_name_end, **items)
        self.detailed_graph[resource_name] = G

    def show(self, resource_name, detailed=False):
        options = {
            'node_color': 'blue',
            'node_size': 100,
            'width': 3,
            'arrowstyle': '-|>',
            'arrowsize': 12,
        }
        if not detailed:
            G = self.graph[resource_name]
            pos = nx.spring_layout(G, seed=13649)
            nx.draw_networkx(G, pos=pos, arrows=True, **options)
        else:
            G = self.detailed_graph[resource_name]
            pos = nx.spring_layout(G, seed=13649)
            nx.draw_networkx(G, pos=pos, arrows=True, **options)
        pylab.show()

    def from_nametype(self, nametype):
            ''' ex: "city_1", "storage" = from_nametype("city_1_storage") '''
            n = nametype.split('_')
            if n[-1] in self.all_types:
                name = n[:-1]
                return '_'.join(name), n[-1]
            else:
                return nametype, None

    def to_nametype(self, entity_name, type):
        ''' ex: "city_1_storage" = to_nametype("city_1", "storage") '''
        return entity_name + '_' + type

    def run_step(self, resource_name):
        eco = Economy()
        eco.orders = list()
        eco.info = dict()

        def update_eco(self):
            pass

        def read_result_eco(self):
            pass

        self.to_graph(resource_name)
        self.to_detailed_graph(resource_name)
        self.show(resource_name, detailed=True)
        #print(G.edges)

        # eco.info is updated
        G = self.graph[resource_name]
        for node in G.nodes:
            node_name, _ = self.from_nametype(node)
            index = self.header_index_dict[node_name]
            entity = self.entities[index]
            for resource in entity.resources:
                if resource.name == resource_name:
                    source = resource.source
                    demand = resource.demand
            eco.info[node_name] = {
                'source': source,
                'demand': demand
            }
        print(eco.info)

        # step 1: only sources and demands added to economy and calculate the result
        order_list = list()
        for edge in G.edges:
            name_start, type_start = self.from_nametype(edge[0])
            name_end, type_end = self.from_nametype(edge[1])
            if type_start == 'source' or type_start == 'demand':
                if type_end == 'source' or type_end == 'demand':
                    index_start = self.header_index_dict[name_start]
                    index_end = self.header_index_dict[name_end]
                    price_factor_matrix = self.price_factor[resource_name]
                    max_discharge_matrix = self.max_discharge[resource_name]
                    order = Order(
                        start=edge[0],
                        end=edge[1],
                        distance=self.distance[index_start][index_end],
                        price_factor=price_factor_matrix[index_start][index_end],
                        max_volume=max_discharge_matrix[index_start][index_end]
                    )
                    order_list.append(order)
        eco.order = order_list
        eco.run()
        print(eco.info)   
        # results are readed and updated
        # add storage units to remaining sources and demands
        for node in G.nodes:
            _, type = self.from_nametype(node)
            if type == 'storage':
                pass
        # results are readed and updated

    def __str__(self):
        return self.name


if __name__ == "__main__":
    from samples import e_1, e_2

    m = Model(entities=[e_1, e_2])
    m.analyze()
    #g = m.to_graph('water')
    m.run_step('water')
