from copy import deepcopy

from piperabm.object import PureObject
#from piperabm.resources import Resources
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
        resources: Resources = None,
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
        dictionary['index'] = self.index
        dictionary['section'] = self.section
        dictionary['category'] = self.category
        dictionary['type'] = self.type
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.pos = dictionary['pos']
        self.name = dictionary['name']
        self.resources = Resources()
        self.resources.deserialize(dictionary['resources'])
        self.degradation = Degradation()
        self.degradation.deserialize(dictionary['degradation'])
        self.index = dictionary['index']
        self.section = dictionary['section']
        self.category = dictionary['category']
        self.type = dictionary['type']


if __name__ == '__main__':
    item = Market(
        name='Sample',
        pos=[0, 0]
    )
    item.print