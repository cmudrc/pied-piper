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

        self.baked = True
        self.library = {}
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
            return id
        elif object.category == "edge":
            junction_1 = Junction(pos=object.pos_1)
            junction_2 = Junction(pos=object.pos_2)
            id_1 = self.add_infrastructure_object(junction_1)
            id_2 = self.add_infrastructure_object(junction_2)
            object.id_1 = id_1
            object.id_2 = id_2
            id = self.add_object_to_library(object)
            return id

    def add(self, *objects) -> None:
        """
        Add new item(s) to model
        """
        for object in objects:
            if object.section == "infrastructure":
                self.add_infrastructure_object(object)
            elif object.section == "society":
                pass
            #    self.add_society_object(object)
            else:  # Onject not recognized
                raise ValueError
            self.baked = False

    @property
    def infrastructure(self):
        if self.baked is True:
            return Infrastructure(model=self)
        else:
            print("First bake the model")
            return None

    def bake(self):
        grammar = Grammar(model=self)
        grammar.apply()
        self.baked = True


if __name__ == "__main__":
    model = Model()
    object_1 = Junction(name="sample", pos=[0, 0])
    object_2 = Road(name="sample", pos_1=[0, 0], pos_2=[1, 1])
    model.add(object_1, object_2)
    #model.show()
    #model.print
    model.bake()
    print(model.baked)
