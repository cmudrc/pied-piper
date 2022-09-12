''' importing from parent folder '''
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from core.entity import Entity


class Agent(Entity):
    def __init__(self, name, pos, active=True):
        super().__init__(
            name=name,
            pos=pos,
            active=active
        )