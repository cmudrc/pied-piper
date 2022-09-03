# pied-piper
PIPER Agent-Based Model


![Pied Piper of Hamelin](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Pied_Piper2.jpg/593px-Pied_Piper2.jpg)

Named after "Pied Piper of Hamelin," the title character of a legend from the town of Hamelin in Germany

## 0. Introduction
Whenever environments condition change for species, the living entities start to react to the new new condition. This projects aims at modeling the Alaskan communities that are heavily affected by the global warming. There are two distinct sides to this project: Environment, and Agents.

## 1. Environment
Environment consists of entities, which use/produce/store resources. These entities, similar to cities, interact with each other through links. These links are specific to each resource, such as water pipeline.

### class Link():
It represents a connection between two entities for a certain resource and its instances have to be added to instances of Resource class.

Includes:
- start: starting entity's name
- end: destination entity's name
- active: state of the link as being active or not
- chance: chance of working properly
- price_factor: shows how hard it is to transfer this resource by this route
- max_discharge: maximum amount for discharge allowed in the link per timestep

### class Resource():
It represents resources and has to be added to an instance of entity class.

Includes:
- name: Resource name, such as 'water' or 'food'.
- source: The amount of source in each timestep.
- demand: The amount of demand in each timestep.
- deficiency_current: Current deficiency of resource.
- deficiency_max: Maximum deficiency of resource that can be handled by the entity.
- storage_current: Current amount of storage for the resource.
- storage_max: Maximum amount of storage possible.
- connections: A list of instances of Link class, representing the connection between neighboring entities.

functions:
- is_alive(): If current deficiency for a certain resource surpasses the maximum deficiency, the entity will cease to exit. This function returns True/False.

### class Entity():
An entity represents a major producer/user/storer of resources, such as cities. It even can represent living creatures, but it is not in the scope of this project. An entity holds three important nodes: source, demand, storage. Instances of Resource class gets added to the entity.

Includes:
- name: Entity's name, such as 'city_1'.
- location: A list in form of [x, y].
- resources: A list of resources that the elements are instances of Resource class.

### class Model():
The main class for representing environment. It accepts instances of Entity class to represent the whole network of resources in that environment.

Includes:
- name: Environment's name, such 'region_1'.
- entities: A list containing the instances of Entity class, representing all entities in the region.
- distance: According to the dynamic programming methodology, this matrix is holding the physical distance values between nodes to faciliate the computations.

functions:
- distance_matrix_calculate(): Generates the distance matrix.
- analyze(): The pre-simulation step to do all the required tasks to start running, such as validate entities connections.
- validate_entities_connections(): Checks for the validity of entities connections.
- to_json(): Converts all information within the model into json
- from_json(txt): Loads model information from json text

### class Node():
Represents nodes of a graph. This is a simple way to show different units within an entity (demand node, source node, storage node) and the relationship between all the nodes from all entities.

Includes:
- name: Name of the node. It has to be identical.
- neighbors: A list containing name of other connected nodes

### class Graph():
Represents a mathematical directed graph. Instances of Node class can be added to the graph.

Includes:
- name: Name of the graph. Optional.
- nodes: A list of instances of Node class, representing the nodes within the graph.

functions:
- validate_node_connections(): Checks for the validity of the connections between nodes of the graph.
- to_matrix(): Converts the information about graph into matrix.
- from_matrix(m): Loads the information about graph from matrix.

### Economic Model:
At each timestep, the source node of each entity looks at all demands from all other demand sources. Satisfying demands from nearest entities is at priorety. Afterwards, it will try to fill nearest storages. Anything beyond their capacity will be wasted.

## 2. Agent