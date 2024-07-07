import networkx as nx

from piperabm.infrastructure.query import Query
from piperabm.infrastructure.generate import Generate
from piperabm.infrastructure.degradation import Degradation
from piperabm.infrastructure.path import Path
from piperabm.infrastructure.update import Update
from piperabm.infrastructure.serialize import Serialize
from piperabm.infrastructure.graphics import Graphics
from piperabm.infrastructure.stat import Stat
from piperabm.infrastructure.grammar import Grammar
from piperabm.infrastructure.heuristic_paths import HeuristicPaths


class Infrastructure(
    Query,
    Generate,
    Degradation,
    Path,
    Update,
    Serialize,
    Graphics,
    Stat
):
    """
    Represent infrastructure network
    """

    type = 'infrastructure'

    def __init__(
            self,
            coeff_usage: float = 0,
            coeff_weather: float = 0
        ):
        self.G = nx.Graph()
        self.model = None # Binding
        self.coeff_usage = coeff_usage
        self.coeff_weather = coeff_weather
        self.baked_streets = True
        self.baked_neighborhood = True
        self.heuristic_paths = HeuristicPaths()

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
    def baked(self) -> bool:
        """
        Check if the network is fully baked
        """
        result = False
        if self.baked_streets is True and \
        self.baked_neighborhood is True:
            result = True
        return result
    
    def bake(
            self,
            report: bool = False,
            proximity_radius: float = 1,
            search_radius: float = None
        ):
        """
        Bake the network using grammar rules
        """
        if self.baked is False:
            grammar = Grammar(
                infrastructure=self,
                proximity_radius=proximity_radius,
                search_radius=search_radius
            )
            grammar.apply(report=report)
            if report is True:
                print("baking is done.")
            self.heuristic_paths.create(infrastructure=self)
        else:
            print("already baked.")


if __name__ == "__main__":
    infrastructure = Infrastructure()
    infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 10])
    infrastructure.bake()
    print(infrastructure)
    #infrastructure.show()
