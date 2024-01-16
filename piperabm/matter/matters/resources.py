from copy import deepcopy

from piperabm.object import PureObject
from piperabm.matter import Matter
from piperabm.economy import ExchangeRate


class Matters(PureObject):

    type = 'resources'

    def __init__(self, *args):
        super().__init__()
        self.library = {}
        for arg in args:
            if isinstance(arg, Matter):
                self.add_resource(arg)

    def add_resource(self, resource: Matter):
        """
        Add new resource to the library
        """
        if resource.name != '' and resource.name is not None:
            if resource.name in self.names:
                previous_resource = self.get(resource.name)
                remainder = previous_resource + resource
                if not remainder.is_empty:
                    raise ValueError
            else:
                self.library[resource.name] = resource
        else:
            raise ValueError

    @property
    def names(self):
        """
        Return name of all resources
        """
        return self.library.keys()

    def __call__(self, name):
        return self.library[name].amount
    
    def get(self, name):
        """
        Get the resource object based on its name
        """
        return self.library[name]