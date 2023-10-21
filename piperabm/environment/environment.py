import uuid

from piperabm.object import PureObject
from piperabm.environment.query import Query
from piperabm.environment.grammar import Grammar
from piperabm.environment.infrastructure import Infrastructure
from piperabm.environment.items import Junction, Settlement, Road


class Environment(PureObject, Query, Grammar):

    def __init__(
        self,
        proximity_radius: float = 0
    ):
        super().__init__()
        self.society = None  # used for binding
        self.library = {}  # {index: item} pairs
        # distance less than this amount is equivalent to zero
        self.proximity_radius = proximity_radius

    @property
    def new_index(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        return uuid.uuid4().int

    def add(self, item) -> None:
        """
        Add new item to library
        """
        if item.category == 'node':
            item.index = self.new_index
            self.library[item.index] = item
        elif item.category == 'edge':
            junction_1 = Junction(pos=item.pos_1)
            junction_2 = Junction(pos=item.pos_2)
            self.add(junction_1)
            self.add(junction_2)
            item.index = self.new_index
            self.library[item.index] = item
        else:
            print('item not recognized')
            raise ValueError

    @property
    def infrastrucure(self):
        """
        Return infrastructure graph of items
        """
        return Infrastructure(environment=self)

    def show(self):
        """
        Show environment (infrastructure)
        """
        infrastructure = self.infrastrucure
        infrastructure.show()

    def serialize(self) -> dict:
        dictionary = {}
        dictionary['proximity radius'] = self.proximity_radius

        ''' serialize library items '''
        library_serialized = {}
        for index in self.library:
            item = self.get_item(index)
            library_serialized[index] = item.serialize()
        dictionary['library'] = library_serialized

        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.proximity_radius = dictionary['proximity radius']

        ''' deserialize library items '''
        library_dictionary = dictionary['library']
        for index in library_dictionary:
            item_dictionary = library_dictionary[index]
            type = item_dictionary['type']
            if type == 'junction':
                item = Junction()
                item.deserialize(item_dictionary)
            elif type == 'settlement':
                item = Settlement()
                item.deserialize(item_dictionary)
            elif type == 'road':
                item = Road()
                item.deserialize(item_dictionary)
            self.library[index] = item


if __name__ == '__main__':
    from items import Junction

    env = Environment(proximity_radius=0.1)
    item = Junction(name='sample', pos=[0, 0])
    env.add(item)
    other = Junction(pos=[0.05, 0])
    env.add(other)
    env.show()
