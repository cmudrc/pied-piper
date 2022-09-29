import numpy as np


class Entity:
    '''
    A super class for representing cities, remote factories, and even humans.
    '''
    def __init__(self, name, pos):
        '''
        Create an entity

        Args:
            name: name of the entity, a string
            pos: position of the entity, a list of [x, y]
            active: whether the entity is active, True/False
        '''
        self.name = name
        self.pos = pos

    def distance(self, other):
        x_0 = self.pos[0]
        y_0 = self.pos[1]
        x_1 = other.pos[0]
        y_1 = other.pos[1]
        return np.power(np.power(x_0 - x_1, 2) + np.power(y_0 - y_1, 2), 0.5)