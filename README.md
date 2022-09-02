# pied-piper
PIPER Agent-Based Model


![Pied Piper of Hamelin](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Pied_Piper2.jpg/593px-Pied_Piper2.jpg)

Named after "Pied Piper of Hamelin," the title character of a legend from the town of Hamelin in Germany

## Introduction
Whenever environments condition change for species, the living entities start to react to the new new condition. This projects aims at modeling the Alaskan communities that are heavily affected by the global warming. There are two distinct sides to this project: Environment, and Agents.

## Environment:

### classes:

#### model.py
class Link():
It represents a connection between two entities for a certain resource and its instances have to be added to instances of Resource class.
Includes:
- start: starting entity's name
- end: destination entity's name
- active: state of the link as being active or not
- chance: chance of working properly

class Resource():
It represents resources and has to be added to an instance of entity class.
Includes:
- name: resource name, such as 'water' or 'food'.
- source: the amount of source in each timestep
- demand: the amount of demand in each timestep
- deficiency_current: current deficiency of resource
- deficiency_max: maximum deficiency of resource that can be handled by the entity
- storage_current: current amount of storage for the resource
- storage_max: maximum amount of storage possible
- connections: a list of instances of Link class, representing the connection between neighboring entities.

class Entity():
class Model():


#### graph.py
class Graph():
class Node():

### Economic Model:
At each timestep, the source node of each entity looks at all demands from all other demand sources. Satisfying demands from nearest entities is at priorety. Afterwards, it will try to fill nearest storages. Anything beyond their capacity will be wasted.

## Agent: