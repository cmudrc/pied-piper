import numpy as np

try:
    from .degradation import DegradationProperty
except:
    from degradation import DegradationProperty


class Entity(DegradationProperty):
    """
    A super class for representing cities, remote factories, and even humans.    
    """

    def __init__(
        self,
        name=None,
        pos=[0, 0],
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
        ):
        """
        Args:
            name: name of the entity, a string
            pos: position of the entity, a list of [x, y]
        """

        super().__init__(
            active=active,
            initial_cost=initial_cost,
            initiation_date=initiation_date,
            distribution=distribution,
            seed=seed
        )
        self.name = name
        self.pos = pos

    def distance(self, other):
        return np.sum(np.square(np.array(self.pos) - np.array(other.pos)))


""" for easier class inheritence """
entity_kwargs = {
    'name': None,
    'pos': [0, 0],
    'active': True,
    'initial_cost': None,
    'initiation_date': None,
    'distribution': None,
    'seed': None,
}


if __name__ == "__main__":
    e_1 = Entity(pos=[0, 0])
    e_2 = Entity(pos=[0, 1])
    d = e_1.distance(e_2)
    print(d)