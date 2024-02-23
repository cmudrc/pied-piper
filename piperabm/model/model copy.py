from copy import deepcopy
import random


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

    def add_infrastructure_object(self, object) -> None:
        """
        Add new infrastructure object to model
        """
        if object.category == "node":
            id = self.add_object_to_library(object)
            #self.infrastructure.add_node(id)
            return id
        elif object.category == "edge":
            junction_1 = Junction(pos=object.pos_1)
            junction_2 = Junction(pos=object.pos_2)
            id_1 = self.add_infrastructure_object(junction_1)
            id_2 = self.add_infrastructure_object(junction_2)
            id = self.add_object_to_library(object)
            #self.infrastructure.add_edge(id_1, id_2, id)
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


if __name__ == "__main__":
    model = Model()
    object_1 = Junction(name="sample", pos=[0, 0])
    object_2 = Road(name="sample", pos_1=[0, 0], pos_2=[1, 1])
    model.add(object_1, object_2)
    #model.show()
    #model.print
    print(model.infrastructure)
