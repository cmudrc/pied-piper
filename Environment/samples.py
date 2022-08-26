from main import Entity

''' sample entities '''
e_1 = Entity(
    name = 'city_1',
    location = [0.1, 0.2],
    source = {
        'water' : 0.5,
        'energy' : 2.5,
        'food' : 2.5
        },
    demand = {
        'water' : 1,
        'energy' : 2,
        'food' : 2.5
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
        'water' : 0,
        'energy' : 0,
        'food' : 0,
        },
    neighbors = [
        'city_1'
        ],
    )