from main import Entity
from graph import Node

''' sample entities '''
e_1 = Entity(
    name = 'city_1',
    location = [0.7, -0.5],
    source = {
        'water' : 0.5,
        'energy' : 2.5,
        'food' : 2.5
        },
    demand = {
        'water' : 1.5,
        'energy' : 2,
        'food' : 3.5
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
        'water' : 10,
        'energy' : 20,
        'food' : 10,
        },
    neighbors = [
        'city_2'
        ],
    )

e_2 = Entity(
    name = 'city_2',
    location = [-0.4, 0.3],
    source = {
        'water' : 0.5,
        'energy' : 2.5,
        'food' : 2.5
        },
    demand = {
        'water' : 1,
        'energy' : 2,
        'food' : 2.5,
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
        'water' : 15,
        'energy' : 10,
        'food' : 50,
        },
    neighbors = [
        'city_1'
        ],
    )


''' sample nodes '''
n_1 = Node(name='node_1', neighbors={'node_2' : 1.5})
n_2 = Node(name='node_2')
n_3 = Node(name='node_3', neighbors={
    'node_1' : 2,
    'node_2' : 1,
    })