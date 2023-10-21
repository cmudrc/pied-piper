import uuid

from piperabm.object import PureObject
from piperabm.economy import GiniGenerator, ExchangeRate


class Society(PureObject):
    """
    Represent society
    Manage agents and their relationships
    """

    def __init__(
            self,
            gini: float = 0,
            gdp_per_capita: float = 0,
            exchange_rate: ExchangeRate = None
        ):
        super().__init__()
        self.environment = None  # used for binding
        self.gini = gini
        self.gdp_per_capita = gdp_per_capita
        self.library = {}
        self.gini_gen = GiniGenerator(gini, gdp_per_capita)
        self.exchange = exchange_rate
        self.type = 'society'

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
        

if __name__ == "__main__":
    society = Society()
    society.print
