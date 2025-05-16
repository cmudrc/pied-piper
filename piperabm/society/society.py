import networkx as nx

from piperabm.society.query import Query
from piperabm.society.generate import Generate
from piperabm.society.decision_making import DecisionMaking
from piperabm.society.update import Update
from piperabm.society.serialize import Serialize
from piperabm.society.graphics import Graphics
from piperabm.society.stat import Stat
from piperabm.tools.gini import gini
from piperabm.economy import accessibility
from piperabm.society.info import *


class Society(
    Query,
    Generate,
    DecisionMaking,
    Update,
    Serialize,
    Graphics,
    Stat
):
    """
    Represent society network
    """

    type = "society"

    def __init__(
            self,
            average_income: float = 1000,
            neighbor_radius: float = 0,
            max_time_outside: float = 8 * (60 * 60), # 8 hours
            activity_cycle: float = 24 * (60 * 60), # 24 hours
            transportation_resource_rates: dict = transportation_resource_rates,
            idle_resource_rates: dict = idle_resource_rates,
            speed: float = speed,
            transportation_degradation: float = 1,
        ):
        self.G = nx.MultiGraph()
        self.model = None # Binding
        self.actions = {}
        self.average_income = average_income
        self.neighbor_radius = neighbor_radius
        if max_time_outside > activity_cycle:
            raise ValueError('"max_time_outside" should be less than "activity_cycle"')
        self.max_time_outside = max_time_outside
        self.activity_cycle = activity_cycle
        self.idle_resource_rates = idle_resource_rates
        self.transportation_resource_rates = transportation_resource_rates
        self.speed = speed
        self.transportation_degradation = transportation_degradation

    @property
    def infrastructure(self):
        """
        Alias
        """
        if self.model is not None:
            result = self.model.infrastructure
        else:
            result = None
        return result
    
    @property
    def resource_names(self) -> list:
        """
        Alias
        """
        return self.model.resource_names
    
    @property
    def prices(self) -> dict:
        """
        Alias
        """
        return self.model.prices

    @property
    def gini_index(self) -> float:
        """
        Calculate the current gini index of society
        """
        data = []
        for id in self.agents:
            data.append(self.wealth(id))
        return gini.coefficient(data)

    def accessibility_resource(self, id: int, name: str):
        """
        Calculate accessibility for certain resource
        """
        amount = self.get_resource(id=id, name=name)
        enough_amount = self.get_enough_resource(id=id, name=name)
        return accessibility(resource=amount, enough_resource=enough_amount)
    
    def accessibility(self, id: int) -> dict:
        """
        Calculate accessibility for all resources
        """
        result = {}
        for name in self.resource_names:
            result[name] = self.accessibility_resource(id=id, name=name)
        return result
    

if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate(num=1)

    print(model.society)