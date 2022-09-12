class Entity:
    '''
    A super class for representing cities, remote factories, and even humans.
    '''
    def __init__(self, name, pos, active=True):
        '''
        Create an entity

        Args:
            name: name of the entity, a string
            pos: position of the entity, a list of [x, y]
            active: whether the entity is active, True/False
        '''
        self.name = name
        self.pos = pos
        self.active = active