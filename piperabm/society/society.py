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
            neighbor_radius: float = 0
        ):
        self.G = nx.MultiGraph()
        self.model = None # Binding
        self.actions = {}
        self.average_income = average_income
        self.neighbor_radius = neighbor_radius

    @property
    def infrastructure(self):
        result = None
        if self.model is not None:
            result = self.model.infrastructure
        return result
    
    @property
    def resource_names(self):
        return self.model.resource_names
    
    @property
    def prices(self):
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