"""
Default values
"""

from copy import deepcopy


""" Idle consumption """
idle_food_rate = 2 / (60 * 60 * 24) # kg/day to kg/s
idle_water_rate = 2 / (60 * 60 * 24) # kg/day to kg/s
idle_energy_rate = 2 / (60 * 60 * 24) # kg/day to kg/s

""" Walk """
speed = 5 * ((1000) / (60 * 60)) # km/hour to m/s
transportation_food_rate = 2 / (60 * 60 * 24) # kg/day to kg/s
transportation_water_rate = 1 / (60 * 60 * 24) # kg/day to kg/s
transportation_energy_rate = 1 / (60 * 60 * 24) # kg/day to kg/s

""" Resource """
average_food = 20 # kg
average_water = 20 # kg
average_energy = 20 # kg
average_enough_food = deepcopy(average_food) # kg
average_enough_water = deepcopy(average_water) # kg
average_enough_energy = deepcopy(average_energy) # kg

max_time_outside = 8 * (60 * 60) # hour to seconds