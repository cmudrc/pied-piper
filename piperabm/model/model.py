import numpy as np

from piperabm.model.serialize import Serialize
from piperabm.model.file import File
from piperabm.model.update import Update
from piperabm.model.graphics import Graphics
from piperabm.infrastructure import Infrastructure
from piperabm.society import Society
from piperabm.tools.symbols import SYMBOLS


class Model(Serialize, File, Update, Graphics):
    """
    Main class of simulation.

    Parameters
    ----------
    name : str, optional
        A label to distinguish this model and its results when running multiple instances. In single runs, this can left empty.
    prices : dict, optional
        Mapping of resource names to unit costs. FEWS Nexus framework expects `'food'`, `'water'`, `'energy'`.
    path : str, optional
        Directory for saving/loading simulation.
    seed : int, optional
        Integer seed for reproducibility.
    """

    type = "model"

    def __init__(
        self,
        name: str = "",
        prices: dict = {
            "food": 1,
            "water": 1,
            "energy": 1,
        },
        path=None,
        seed: int = None,
    ):
        """
        Initialize the Model.
        """
        super().__init__()
        self.time = 0
        self.step = 0
        self.infrastructure = Infrastructure()
        self.infrastructure.model = self  # Binding
        self.society = Society()
        self.society.model = self  # Binding
        self.name = name
        self.prices = prices
        self.path = path  # File saving
        self.set_seed(seed=seed)

    def set_seed(self, seed: int = None):
        """
        Set random generator seed for result reproducability.
        """
        self.seed = seed
        np.random.seed(seed)

    @property
    def resource_names(self):
        """
        Return name of resources in the model.
        """
        return list(self.prices.keys())

    def bake(
        self,
        save: bool = False,
        proximity_radius: float = SYMBOLS["eps"],
        search_radius: float = None,
        report: bool = False,
    ):
        """
        Prepare the model for the first simulation step.
        This will generate nodes/edges, and compute any necessary initial calculations to create a physically sensinble network.

        Parameters
        ----------
        save : bool, default=False
            If True, immediately serialize the infrastructure state to disk.
        proximity_radius : float, default=0
            The grammar rules use this value (in model units) to determine how close the elements should be to each other to impact each other, such as getting merged or split.
        search_radius : float or None, default=None
            Home and market nodes need to get connected to the street network. This is done using "Neighborhood access" edges. The grammar rule for this process is computationally expensive therefore setting a search radius can speed up the process specially in large and intricate networks. If set to `None`, all possible elements are network are evaluated.
        report : bool, default=False
            If `True`, reports the steps taken during the baking process, which can be useful for debugging or understanding the model.
        """
        self.infrastructure.bake(
            report=report,
            proximity_radius=proximity_radius,
            search_radius=search_radius,
        )
        if save is True:
            self.save(state="infrastructure")

    @property
    def baked(self):
        """
        Return whether the model is baked or not.
        """
        return self.infrastructure.baked


if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.infrastructure.add_street(pos_1=[-5, 0], pos_2=[5, 0])
    model.bake()
    print(model.infrastructure)
