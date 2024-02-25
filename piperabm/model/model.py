from copy import deepcopy
import random


from piperabm.object import PureObject
from piperabm.model.query import Query
from piperabm.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.infrastructure import Infrastructure, Junction, Road, Settlement
from piperabm.infrastructure.items.deserialize import infrastructure_deserialize
#from piperabm.society import Society, Family
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.matter import Containers
#from piperabm.measure import Measure
from piperabm.tools.file_manager import JsonHandler as jsh
from piperabm.tools.stats import gini
#from piperabm.config.settings import *
from piperabm.society.agent.config import *
import os


class Model(PureObject, Query):

    type = "model"

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
        name: str = "sample",
        path: str = None
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
        self.path = path

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

    def add_infrastructure_object(self, object):
        """
        Add new infrastructure object to model
        """
        if object.category == "node":
            id = self.add_object_to_library(object)
        elif object.category == "edge":
            junction_1 = Junction(pos=object.pos_1)
            junction_2 = Junction(pos=object.pos_2)
            id_1 = self.add_infrastructure_object(junction_1)
            id_2 = self.add_infrastructure_object(junction_2)
            object.id_1 = id_1
            object.id_2 = id_2
            id = self.add_object_to_library(object)
        else:
            print("Object type not recognized.")
            raise ValueError
        self.baked = False
        return id
        
    def add_society_object(self, object):
        """
        Add new society object to model
        """
        pass

    def add(self, *objects) -> None:
        """
        Add new item(s) to model
        """
        for object in objects:
            if object.section == "infrastructure":
                self.add_infrastructure_object(object)
            elif object.section == "society":
                self.add_society_object(object)
            else:  # Onject not recognized
                raise ValueError

    @property
    def infrastructure(self):
        if self.baked is True:
            return Infrastructure(model=self)
        else:
            print("First, bake the model.")
            return None

    def bake(self, save=True):
        """
        Apply all grammars.
        If save is True, the initial state of model will be saved to file after each change.
        """
        if self.baked is False:
            grammar = Grammar(model=self, save=save)
            grammar.apply()
            self.baked = True
        else:
            print("Already baked.")

    def save_initial(self):
        data = self.serialize()
        filename = self.name + "_" + "initial"
        jsh.save(data, self.path, filename)
        print(Date.today())
        #print(filename + " saved.")

    def load_initial(self):
        filename = self.name + "_" + "initial"
        data = jsh.load(self.path, filename)
        self.deserialize(data)
    
    def serialize(self) -> dict:
        dictionary = {}
        dictionary["type"] = self.type
        dictionary["proximity radius"] = self.proximity_radius
        dictionary["step_size"] = self.step_size.total_seconds()
        dictionary["current_date"] = date_serialize(self.current_date)
        dictionary["exchange_rate"] = self.exchange_rate.serialize()
        dictionary["gini_index"] = self.gini_index
        dictionary["average_income"] = self.average_income
        dictionary["average_balance"] = self.average_balance
        dictionary["average_resources"] = self.average_resources.serialize()
        dictionary["name"] = self.name
        dictionary["baked"] = self.baked
        # Library
        library_serialized = {}
        for id in self.library:
            object = self.get(id)
            library_serialized[str(id)] = object.serialize()
        dictionary["library"] = library_serialized
        return dictionary
    
    def deserialize(self, dictionary: dict) -> None:
        if dictionary["type"] != self.type:
            raise ValueError
        self.proximity_radius = dictionary["proximity radius"]
        self.step_size = DeltaTime(seconds=dictionary["step_size"])
        self.current_date = date_deserialize(dictionary["current_date"])
        self.exchange_rate = ExchangeRate()
        self.exchange_rate.deserialize(dictionary["exchange_rate"])
        self.gini_index = dictionary["gini_index"]
        self.average_income = dictionary["average_income"]
        self.average_balance = dictionary["average_balance"]
        self.average_resources = Containers()
        self.average_resources.deserialize(dictionary["average_resources"])
        self.name = dictionary["name"]
        self.baked = dictionary["baked"]
        # Library
        library_dictionary = dictionary["library"]
        for id in library_dictionary:
            object_dictionary = library_dictionary[id]
            if object_dictionary["section"] == "infrastructure":
                self.library[int(id)] = infrastructure_deserialize(object_dictionary)
            #elif object_dictionary["section"] == "society":
            #    self.library[int(id)] = society_deserialize(object_dictionary)


if __name__ == "__main__":
    model = Model(proximity_radius=1)
    object_1 = Settlement(name="sample", pos=[0, 0])
    object_2 = Road(name="sample", pos_1=[0, 0], pos_2=[10, 10])
    model.add(object_1, object_2)
    #model.save_initial()
    #model.show()
    #model.print    
    #model.bake(save=True)
    #print(model.baked)
