from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Containers
from piperabm.degradation import Degradation
from piperabm.society.agent.config import *


class Market(PureObject):

    section = 'infrastructure'
    category = 'node'
    type = 'market'

    def __init__(
        self,
        pos: list = None,
        name: str = '',
        resources: Containers = None,
        degradation: Degradation = None,
        id: int = None
    ):
        super().__init__()
        
        self.model = None  # to access model

        self.pos = pos
        self.name = name
        if resources is None:
            resources = deepcopy(RESOURCES_DEFAULT)
        self.resources = resources
        if degradation is None:
            degradation = Degradation()
        self.degradation = degradation
        self.id = id

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['pos'] = self.pos
        dictionary['name'] = self.name
        dictionary['resources'] = self.resources.serialize()
        dictionary['degradation'] = self.degradation.serialize()
        dictionary['id'] = self.id
        dictionary['section'] = self.section
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        if dictionary['type'] != self.type:
            raise ValueError
        self.pos = dictionary['pos']
        self.name = dictionary['name']
        self.resources = Containers()
        self.resources.deserialize(dictionary['resources'])
        self.degradation = Degradation()
        self.degradation.deserialize(dictionary['degradation'])
        self.id = dictionary['id']


if __name__ == '__main__':
    object = Market(
        name='Sample',
        pos=[0, 0]
    )
    print(object)