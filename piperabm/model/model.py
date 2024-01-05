from copy import deepcopy
import random

from piperabm.object import PureObject
from piperabm.model.query import Query
from piperabm.model.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.infrastructure import Infrastructure, Junction, Settlement, Market, Road
from piperabm.society import Society, Agent, Family
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.measure import Measure


valid_items = (
    Junction,
    Settlement,
    Market,
    Road,
    Agent,
    Family,
)


class Model(PureObject, Query, Graphics):

    def __init__(
        self,
        proximity_radius: float = 0,
        step_size=None,
        current_date: Date = Date.today(),
        exchange_rate: ExchangeRate = None
    ):
        super().__init__()
        self.library = {}
        self.proximity_radius = proximity_radius
        self.set_step_size(step_size)
        self.current_date = current_date
        if exchange_rate is None:
            exchange_rate = deepcopy(exchange_rate_0)  # default
        self.exchange_rate = exchange_rate
        self.measure = Measure(self)
        self.valid_types = Model.extract_valid_types(valid_items)  # recognizable items list

    def extract_valid_types(valid_items):
        valid_types = {
            "infrastructure": {
                "node": [],
                "edge": [],
            },
            "society": {
                "node": [],
                "edge": [],
            },
        }
        for item in valid_items:
            valid_types[item().section][item().category].append(item().type)
        return valid_types

    def set_step_size(self, step_size):
        """
        Set step size
        """
        if step_size is None:
            step_size = DeltaTime(hours=1)  # default
        if isinstance(step_size, (float, int)):
            step_size = DeltaTime(seconds=step_size)
        if isinstance(step_size, DeltaTime):
            self.step_size = step_size
        else:
            raise ValueError

    def add(self, *items) -> None:
        """
        Add new item(s) to library
        """

        def add_infrastructure_item(self, item) -> None:
            """
            Add new infrastructure item to library
            """
            if item.category == "node":
                item.index = self.new_index  # new index
                item.model = self  # binding
                self.library[item.index] = item  # add to library
            elif item.category == "edge":
                junction_1 = Junction(pos=item.pos_1)
                junction_2 = Junction(pos=item.pos_2)
                self.add(junction_1)
                self.add(junction_2)
                item.index = self.new_index  # new index
                item.model = self  # binding
                self.library[item.index] = item  # add to library

        def add_society_item(self, item) -> None:
            """
            Add new society item to library
            """
            if item.category == "node":
                item.index = self.new_index  # new index
                item.model = self  # binding
                settlements = self.filter(types="settlement")
                if item.home is None:
                    item.home = random.choice(settlements)
                    home = self.get(item.home)
                    item.pos = home.pos
                else:
                    if item.home not in settlements:
                        raise ValueError
                families = self.find_agents_in_same_home(item.home)
                self.library[item.index] = item  # adding to library
                for family in families:
                    relationship = Family(
                        index_1=item.index,
                        index_2=family,
                        home_index=item.home
                    )
                    self.add(relationship)
            elif item.category == "edge":
                item.index = self.new_index  # new index
                item.model = self  # binding
                self.library[item.index] = item  # adding to library

        for item in items:
            if isinstance(item, list):
                for element in item:
                    self.add(element)
            elif isinstance(item, valid_items):
                if item.section == "infrastructure":
                    add_infrastructure_item(self, item)
                elif item.section == "society":
                    add_society_item(self, item)
            else:  # item not recognized
                raise ValueError

    def update(self):
        agents = self.all_alive_agents
        date_start = self.current_date
        date_end = date_start + self.step_size
        for index in agents:
            agent = self.get(index)
            agent.update(date_start, date_end)
        self.current_date = date_end

    def run(self, n: int = 1):
        for _ in range(n):
            self.update()

    @property
    def infrastructure(self):
        """
        Return infrastructure graph of items
        """
        grammar = Grammar(model=self)
        grammar.apply()
        return Infrastructure(model=self)
    
    @property
    def society(self):
        """
        Return society graph of items
        """
        return Society(model=self)
    
    def show(self):
        graphics = Graphics(self)
        graphics.show()

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["proximity radius"] = self.proximity_radius
        """ serialize library items """
        library_serialized = {}
        for index in self.library:
            item = self.get(index)
            library_serialized[index] = item.serialize()
        dictionary["library"] = library_serialized
        dictionary["step_size"] = self.step_size.total_seconds()
        dictionary["current_date"] = date_serialize(self.current_date)
        dictionary["exchange_rate"] = self.exchange_rate.serialize()
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.proximity_radius = dictionary["proximity radius"]
        """ Deserialize library items """
        library_dictionary = dictionary["library"]
        for index in library_dictionary:
            item_dictionary = library_dictionary[index]
            type = item_dictionary["type"]
            if type == "junction":
                item = Junction()
                item.deserialize(item_dictionary)
            elif type == "settlement":
                item = Settlement()
                item.deserialize(item_dictionary)
            elif type == "road":
                item = Road()
                item.deserialize(item_dictionary)
            self.library[index] = item
        self.step_size = DeltaTime(seconds=dictionary["step_size"])
        self.current_date = date_deserialize(dictionary["current_date"])
        self.exchange_rate = ExchangeRate()
        self.exchange_rate.deserialize(dictionary["exchange_rate"])


if __name__ == "__main__":
    model = Model()
    item = Junction(name="sample", pos=[0, 0])
    model.add(item)
    #model.show()
    model.print
