from copy import deepcopy
import random

from piperabm.object import PureObject
from piperabm.model.query import Query
from piperabm.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.infrastructure import Infrastructure, Junction, Settlement, Market, Road
from piperabm.society import Society, Agent, Family
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.measure import Measure
from piperabm.tools.file_manager import JsonHandler as jsh
from piperabm.config.settings import *


class Model(PureObject, Query, Graphics):

    def __init__(
        self,
        proximity_radius: float = 0,
        step_size=None,
        current_date: Date = None,
        exchange_rate: ExchangeRate = None,
        name: str = "sample"
    ):
        super().__init__()
        self.library = {}
        self.proximity_radius = proximity_radius
        self.set_step_size(step_size)
        if current_date is None:
            current_date = Date(year=2000, month=1, day=1)
        self.current_date = current_date
        if exchange_rate is None:
            exchange_rate = deepcopy(exchange_rate_0)  # default
        self.exchange_rate = exchange_rate
        self.name = name
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
    
    def save(self, path):
        """
        Save the model based on delta creation to a file
        """
        filename = self.name
        if not jsh.exists(path, filename):
            data = [self.serialize()]
            jsh.save(data, path, filename)
        else:
            data = jsh.load(path, filename)
            previous_entry = data[-1]
            delta = self.create_delta(previous_entry)
            jsh.append(delta, path, filename)

    def remove_save(self, path):
        """
        Remove save file
        """
        filename = self.name
        jsh.remove(path, filename)

    def load(self, path, filename):
        """
        Load the model based on deltas in a file
        """
        if jsh.exists(path, filename):
            deltas = jsh.load(path, filename)
        for i, delta in enumerate(deltas):
            if i == 0:
                self.deserialize(delta)
            else:
                self.apply_delta(delta)
    
    def show(self):
        """
        Show the graphical representation of current state of model
        """
        graphics = Graphics(
            infrastructure=self.infrastructure,
            society=self.society
        )
        graphics.show()

    def serialize(self) -> dict:
        dictionary = {}
        dictionary["proximity radius"] = self.proximity_radius
        """ serialize library items """
        library_serialized = {}
        for index in self.library:
            item = self.get(index)
            library_serialized[str(index)] = item.serialize()
        dictionary["library"] = library_serialized
        dictionary["step_size"] = self.step_size.total_seconds()
        dictionary["current_date"] = date_serialize(self.current_date)
        dictionary["exchange_rate"] = self.exchange_rate.serialize()
        dictionary["name"] = self.name
        return dictionary

    def deserialize(self, dictionary: dict) -> None:
        self.proximity_radius = dictionary["proximity radius"]
        # Deserialize library
        library_dictionary = dictionary["library"]
        for index in library_dictionary:
            item_dictionary = library_dictionary[index]
            type = item_dictionary["type"]
            for valid_item in valid_items:
                if valid_item.type == type:
                    item = valid_item()
                    break
            item.deserialize(item_dictionary)
            self.library[int(index)] = item
        self.step_size = DeltaTime(seconds=dictionary["step_size"])
        self.current_date = date_deserialize(dictionary["current_date"])
        self.exchange_rate = ExchangeRate()
        self.exchange_rate.deserialize(dictionary["exchange_rate"])
        self.name = dictionary["name"]


if __name__ == "__main__":
    model = Model()
    item = Junction(name="sample", pos=[0, 0])
    model.add(item)
    #model.show()
    model.print
