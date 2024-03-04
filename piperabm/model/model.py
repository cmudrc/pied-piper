from copy import deepcopy
import random

from piperabm.object import PureObject
from piperabm.model.query import Query
from piperabm.graphics import Graphics
from piperabm.infrastructure.grammar import Grammar
from piperabm.time import DeltaTime, Date, date_serialize, date_deserialize
from piperabm.infrastructure import Infrastructure, Junction, Road, Settlement
from piperabm.infrastructure.items.deserialize import infrastructure_deserialize
from piperabm.society import Society, Agent, Family
from piperabm.society.deserialize import society_deserialize
from piperabm.economy import ExchangeRate
from piperabm.economy.exchange_rate.samples import exchange_rate_0
from piperabm.matter import Containers
#from piperabm.measure import Measure
#from piperabm.tools.file_manager import JsonHandler as jsh
from piperabm.tools.file_manager import JsonFile
from piperabm.tools.stats import gini
#from piperabm.config.settings import *
from piperabm.society.agent.config import *
from piperabm.tools import Delta


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
        self.average_income = average_income
        self.average_balance = average_balance
        self.average_resources = average_resources
        self.name = name
        self.path = path
        self.baked = True
        self.library = {}
        self.infrastructure = None
        self.society = None
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
        if self.baked is False:
            print("First, bake the model.")
            raise ValueError
        if object.category == "node":
            """ Home """
            settlements = self.settlement_nodes
            if object.home is None:
                object.home = random.choice(settlements)
            else:
                if object.home not in settlements:
                    raise ValueError
            object.current_node = deepcopy(object.home)
            home = self.get(object.home)
            object.pos = deepcopy(home.pos)

            """ Socio-economic status """
            distribution = gini.lognorm(self.gini_index)
            object.socioeconomic_status = distribution.rvs()
            object.set_balance(self.average_balance)
            object.set_resources(self.average_resources)
            id = self.add_object_to_library(object)

            """ Relationships """
            familiy_members = self.find_agents_in_same_home(object.home)
            for family_id in familiy_members:
                if family_id != object.id:
                    relationship = Family(
                        id_1=object.id,
                        id_2=family_id,
                        home_id=object.home
                    )
                    self.add(relationship)
            return id
                
        elif object.category == "edge":
            self.add_object_to_library(object)

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

    def create_infrastructure(self):
        """
        Create infrastructure graph
        """
        if self.baked is True:
            self.infrastructure = Infrastructure(model=self)
        else:
            print("First, bake the model.")
        
    def create_society(self):
        """
        Create society graph
        """
        if self.baked is True:
            self.society = Society(model=self)
        else:
            print("First, bake the model.")
        
    def generate_agents(self, num: int = 1):
        """
        Generate agents
        """
        for _ in range(num):
            agent = Agent()
            self.add(agent)

    def update(self, save=False):
        """
        Update model for single step in time
        """
        # Delta handling
        if save is True:
            old = self.serialize()

        # Prepare model
        self.create_infrastructure()
        self.create_society()
        duration = self.step_size

        # Update elements
        for id in self.agents:
            agent = self.get(id)
            agent.update(duration)
        self.current_date += duration

        # Delta handling
        if save is True:
            current = self.serialize()
            delta = Delta.create(old, current)
            self.append_delta(delta)

    def run(self, n: int = 1, save=False, report=True):
        """
        Update model for multiple steps in time
        """
        for i in range(n):
            if report is True and n is not None:
                print(f"Progress: {i / n * 100:.1f}% complete")
            self.update(save=save)

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
        """
        Save model as initial state
        """
        data = self.serialize()
        filename = self.name + "_" + "initial"
        file = JsonFile(self.path, filename)
        file.save(data)
        #print(Date.today())

    def load_initial(self):
        """
        Load model as initial state
        """
        filename = self.name + "_" + "initial"
        file = JsonFile(self.path, filename)
        data = file.load()
        self.deserialize(data)
        self.create_infrastructure()
        self.create_society()

    def append_delta(self, delta):
        """
        Create and append new delta to file
        """
        filename = self.name + "_" + "deltas"
        deltas_file = JsonFile(self.path, filename)
        if deltas_file.exists() is False:
            deltas = []
            deltas_file.save(deltas)
        deltas_file.append(delta)

    def load_deltas(self):
        """
        Load deltas from file
        """
        filename = self.name + "_" + "deltas"
        deltas_file = JsonFile(self.path, filename)
        return deltas_file.load()
    
    def apply_delta(self, delta) -> None:
        """
        Apply the *delta* to the *self*
        """
        dictionary = self.serialize()
        dictionary_new = Delta.apply(dictionary, delta)
        self.deserialize(dictionary_new)
    
    def apply_deltas(self):
        """
        Load deltas from file and apply them all
        """
        deltas = self.load_deltas()
        for delta in deltas:
            self.apply_delta(delta)
        
    def fig(self):
        result = None
        if self.baked is True:
            graphics = Graphics(
                infrastructure=self.infrastructure,
                society=self.society
            )
            result = graphics.fig()
        return result

    def show(self):
        """
        Show the model
        """
        if self.baked is True:
            graphics = Graphics(
                infrastructure=self.infrastructure,
                society=self.society
            )
            graphics.show()
    
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
                self.library[int(id)] = infrastructure_deserialize(object_dictionary, model=self)
            elif object_dictionary["section"] == "society":
                self.library[int(id)] = society_deserialize(object_dictionary, model=self)


if __name__ == "__main__":
    model = Model(proximity_radius=1)
    object_1 = Settlement(name="sample", pos=[0, 0])
    object_2 = Road(name="sample", pos_1=[0, 0], pos_2=[10, 10])
    model.add(object_1, object_2)
    model.bake(save=False)
    agent = Agent()
    agent.id = 0
    model.add(agent)
    #model.show()
    print(model)
