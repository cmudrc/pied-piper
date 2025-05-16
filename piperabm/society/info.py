"""
Default values
"""

from copy import deepcopy


""" Idle consumption """
idle_resource_rates = {
    'food': 2 / (60 * 60 * 24), # kg/day to kg/s
    'water': 2 / (60 * 60 * 24), # kg/day to kg/s
    'energy': 2 / (60 * 60 * 24), # kg/day to kg/s
}

""" Walk """
speed = 5 * ((1000) / (60 * 60)) # km/hour to m/s
transportation_resource_rates = {
    'food': 2 / (60 * 60 * 24), # kg/day to kg/s
    'water': 1 / (60 * 60 * 24), # kg/day to kg/s
    'energy': 1 / (60 * 60 * 24), # kg/day to kg/s
}

""" Resource """
average_resources = {
    'food': 20, # kg
    'water': 20, # kg
    'energy': 20, # kg
}
average_enough_resources = deepcopy(average_resources)
