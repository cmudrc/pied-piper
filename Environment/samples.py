from model import Link, Resource, Entity
from graph import Node, Graph


''' sample entities '''
r1_1 = Resource(
    name = 'water',
    source = 5,
    demand = 4,
    deficiency_current = 0,
    deficiency_max = 10,
    storage_current = 2,
    storage_max = 10,
    connections = [Link(end='city_2')]
    )
r2_1 = Resource(
    name = 'energy',
    source = 7,
    demand = 4,
    deficiency_current = 0,
    deficiency_max = 12,
    storage_current = 0,
    storage_max = 8,
    connections = []
    )
r3_1 = Resource(
    name = 'food',
    source = 4,
    demand = 5,
    deficiency_current = 0,
    deficiency_max = 8,
    storage_current = 3,
    storage_max = 15,
    connections = [Link(end='city_2')]
    )
e_1 = Entity(
name = 'city_1',
location = [0.7, -0.5],
resources=[r1_1, r2_1, r3_1]
    )

r1_2 = Resource(
    name = 'water',
    source = 7,
    demand = 4,
    deficiency_current = 0,
    deficiency_max = 12,
    storage_current = 0,
    storage_max = 8,
    connections = [Link(end='city_1')]
    )
r2_2 = Resource(
    name = 'energy',
    source = 4,
    demand = 5,
    deficiency_current = 0,
    deficiency_max = 8,
    storage_current = 3,
    storage_max = 15
    )
r3_2 = Resource(
    name = 'food',
    source = 5,
    demand = 4,
    deficiency_current = 0,
    deficiency_max = 10,
    storage_current = 2,
    storage_max = 10
    )
e_2 = Entity(
name = 'city_2',
location = [-0.3, 0.4],
resources=[r1_2, r2_2, r3_2]
    )

e_3 = Entity(
name = 'city_3'
    )


''' sample nodes '''
n_1 = Node(name='node_1', neighbors={'node_2' : 1.5})
n_2 = Node(name='node_2')
n_3 = Node(name='node_3', neighbors={
    'node_1' : 2,
    'node_2' : 1,
    })