import numpy as np

from piperabm.model.serialize import Serialize
from piperabm.model.file import File
from piperabm.model.update import Update
from piperabm.model.graphics import Graphics
from piperabm.infrastructure import Infrastructure
from piperabm.society import Society


class Model(
    Serialize,
    File,
    Update,
    Graphics
):
    """
    Main class of simulation
    """

    type = "model"

    def __init__(
        self,
        name: str = '',
        prices: dict = {
                'food': 1,
                'water': 1,
                'energy': 1,
            },
        path=None,
        seed=None
    ):
        super().__init__()
        self.time = 0
        self.step = 0
        self.infrastructure = Infrastructure()
        self.infrastructure.model = self # Binding
        self.society = Society()
        self.society.model = self # Binding
        self.name = name
        self.prices = prices
        self.path = path # File saving
        self.set_seed(seed=seed)

    def set_seed(self, seed: int = None):
        """
        Set random generator seed for result reproducability
        """
        self.seed = seed
        np.random.seed(seed)

    @property
    def resource_names(self):
        """
        Return name of resources in the model
        """
        return list(self.prices.keys())

    def bake(
            self,
            save: bool = False,
            proximity_radius: float = 0,
            search_radius: float = None,
            report: bool = False
        ):
        """
        Bake model
        """
        self.infrastructure.bake(
            report=report,
            proximity_radius=proximity_radius,
            search_radius=search_radius
        )
        if save is True:
            self.save(state='infrastructure')
    

if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.infrastructure.add_street(pos_1=[-5, 0], pos_2=[5, 0])
    model.bake()
    print(model.infrastructure)
