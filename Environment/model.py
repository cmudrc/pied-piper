import numpy as np
import json


class Link():
    ''' represents a connection between two entities for a certain resource '''

    def __init__(
        self,
        start=None,
        end=None,
        active=True,
        chance=1,
        price_factor=1
    ):
        self.start = start  # the starting point
        self.end = end  # the end point
        # whether this connections is active, (True/False)
        self.active = active
        # chance of working properly, (0 <= chance <= 1)
        self.chance = chance
        # shows how hard it is to transfer this resource by this route
        self.price_factor = price_factor


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
        #return result_dict

    def update_step(self):
        pass

    def __str__(self):
        return self.name


if __name__ == "__main__":
    from samples import e_1, e_2

    m = Model(entities=[e_1, e_2])
    m.analyze()
    #print(m.validate_entities_connections())
    print(m.to_json())
