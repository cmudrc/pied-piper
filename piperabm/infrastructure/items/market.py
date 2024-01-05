from copy import deepcopy

from piperabm.object import PureObject
from piperabm.resources import Resources
from piperabm.degradation import Degradation
from piperabm.society.agent.config import *


class Market(PureObject):

    def __init__(
        self,
        pos: list = None,
        name: str = "",
        resources: Resources = None,
        degradation=Degradation()
    ):
        super().__init__()
        
        self.model = None  # to access model

        self.pos = pos
        self.name = name
        if resources is None:
            resources = deepcopy(RESOURCES_DEFAULT)
        self.resources = resources
        self.degradation = degradation

        self.section = "infrastructure"
        self.category = "node"
        self.type = "market"