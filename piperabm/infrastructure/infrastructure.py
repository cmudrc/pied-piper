"""
.. module:: piperabm.infrastructure.infrastructure
:synopsis: Core Infrastructure class composing Query, Generate, Degradation, Path, Update, Serialize, Graphics, and Stat mixins.
"""

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
from piperabm.tools.symbols import SYMBOLS


class Infrastructure(
    Query, Generate, Path, Update, Serialize, Graphics, Stat
):
    """
    Represent infrastructure network. Within the object, a `nx.Graph()` instance is used as backend.

    Parameters
    ----------
    coeff_usage : float, optional
        This is used to calculate the `adjustment_factor` for the elements and acts as the coefficient for amount of usage the element has received.
    coeff_age : float, optional
        This is used to calculate the `adjustment_factor` for the elements and acts as the coefficient for age of the element.
    """

    type = "infrastructure"

    def __init__(self, coeff_usage: float = 0, coeff_age: float = 0):
        self.G = nx.Graph()
        self.model = None  # Binding
        self.coeff_usage = coeff_usage
        self.coeff_age = coeff_age
        self.baked_streets = True
        self.baked_neighborhood = True
        self.heuristic_paths = HeuristicPaths()

        # Bootstraping for Degradation
        self._degradation = Degradation()
        self._degradation.infrastructure = self

    def __getattr__(self, name):
        """
        Forward unknown attributes to the degradation module, if it exists.
        """
        dm = object.__getattribute__(self, "_degradation")
        if hasattr(dm, name):
            return getattr(dm, name)
        raise AttributeError(name)

    def set_degradation(self, cls):
        """
        Set the degradation class to use for this infrastructure. The class must be a subclass of Degradation.
        """
        if not issubclass(cls, Degradation):
            raise TypeError("Must subclass Degradation")

        self._degradation = cls()
        self._degradation.infrastructure = self

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
        if self.baked_streets is True and self.baked_neighborhood is True:
            result = True
        return result

    def bake(
        self,
        report: bool = False,
        proximity_radius: float = SYMBOLS["eps"],
        search_radius: float = None,
    ):
        """
        Bake the network using grammar rules
        """
        if self.baked is False:
            grammar = Grammar(
                infrastructure=self,
                proximity_radius=proximity_radius,
                search_radius=search_radius,
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
    # infrastructure.show()
