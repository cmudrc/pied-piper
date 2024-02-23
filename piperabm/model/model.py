from copy import deepcopy
import random
import uuid

from piperabm.object import PureObject
from piperabm.model.query import Query
from piperabm.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.infrastructure import Infrastructure, Junction, Road
from piperabm.society import Society, Family
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.matter import Containers
from piperabm.measure import Measure
from piperabm.tools.file_manager import JsonHandler as jsh
from piperabm.tools.stats import gini
from piperabm.config.settings import *
from piperabm.society.agent.config import *



class Model(PureObject, Query):

    def __init__(
        self,
        proximity_radius: float = 0,
        step_size = DeltaTime(hours=1),
        current_date: Date = Date(year=2000, month=1, day=1),
        exchange_rate: ExchangeRate = deepcopy(exchange_rate_0),
        gini_index: float = 0,
        average_income: float = 0,  # Currency / month
        average_balance: float = deepcopy(BALANCE_DEFUALT),
        average_resources: Containers = deepcopy(RESOURCES_DEFAULT),
        name: str = "sample"
    ):
        super().__init__()

        self.proximity_radius = proximity_radius
        self.set_step_size(step_size)
        self.current_date = current_date
        self.exchange_rate = exchange_rate
        self.gini_index = gini_index
        #self.socio_economic_status_distribution = gini.lognorm(gini_index)
        self.average_income = average_income
        self.average_balance = average_balance
        self.average_resources = average_resources
        self.name = name

        self.library = {}
        self.infrastructure = Infrastructure(model=self)
        #self.measure = Measure(self)

    def set_step_size(self, step_size):
        """
        Set step size
        """
        if isinstance(step_size, (float, int)):
            self.step_size = DeltaTime(seconds=step_size)
        elif isinstance(step_size, DeltaTime):
            self.step_size = step_size
        else:
            raise ValueError
        
    def has_id(self, id) -> bool:
        """
        Check if the id already exists
        """
        result = False
        if id in self.all:
            result = True
        return result

    @property
    def new_id(self) -> int:
        """
        Generate a new unique integer as id for graph items
        """
        result = None
        while True:
            new_id = uuid.uuid4().int
            if self.has_id(new_id) is False:
                result = new_id
                break
        return result

    def add_object_to_library(self, object):
        """
        Add new object to library
        """
        # ID
        if object.id is None:
            object.id = self.new_id
        else:
            if self.has_id(object.id) is True:
                object.id = self.new_id
        # Binding
        object.model = self
        # Add to library
        self.library[object.id] = object
        return object.id

    def add_infrastructure_object(self, object) -> None:
        """
        Add new infrastructure object to model
        """
        if object.category == "node":
            id = self.add_object_to_library(object)
            self.infrastructure.add_node(id)
            return id
        elif object.category == "edge":
            junction_1 = Junction(pos=object.pos_1)
            junction_2 = Junction(pos=object.pos_2)
            id_1 = self.add_infrastructure_object(junction_1)
            id_2 = self.add_infrastructure_object(junction_2)
            id = self.add_object_to_library(object)
            self.infrastructure.add_edge(id_1, id_2, id)
            return id

    def add(self, *items) -> None:
        """
        Add new item(s) to model
        """
        for item in items:
            if isinstance(item, list):
                for element in item:
                    self.add(element)
            else:
                if item.section == "infrastructure":
                    self.add_infrastructure_object(item)
                #elif item.section == "society":
                #    add_society_item(self, item)
                else:  # item not recognized
                    raise ValueError

    '''
    def add(self, *items) -> None:
        """
        Add new item(s) to model
        """

        def add_society_item(self, item) -> None:
            """
            Add new society item to model
            """
            if item.category == "node":
                """ Home """
                settlements = self.filter(types="settlement")
                if item.home is None:
                    item.home = random.choice(settlements)
                else:
                    if item.home not in settlements:
                        raise ValueError
                home = self.get(item.home)
                item.pos = deepcopy(home.pos)

                """ Socio-economic status """
                distribution = gini.lognorm(self.gini_index)
                item.socioeconomic_status = distribution.rvs()
                item.set_balance(self.average_balance)
                item.set_resources(self.average_resources)

                """ Relationships """
                families = self.find_agents_in_same_home(item.home)
                add_to_library(self, item)
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
    '''


if __name__ == "__main__":
    model = Model()
    object = Junction(name="sample", pos=[0, 0])
    model.add_infrastructure_object(object)
    object = Road(name="sample", pos_1=[0, 0], pos_2=[1, 1])
    model.add_infrastructure_object(object)
    #model.show()
    #model.print
    print(model.infrastructure)
