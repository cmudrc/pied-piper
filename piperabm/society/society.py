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
#from piperabm.economy import utility, trade_solver
#from piperabm.data.agents_info import *
#from piperabm.data.utqiavik.info import *


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
            food_price: float = 1,
            water_price: float = 1,
            energy_price: float = 1,
            average_income: float = 1000,
            neighbor_radius: float = 0
        ):
        self.G = nx.MultiGraph()
        self.model = None # Binding
        self.actions = {}
        self.food_price = food_price
        self.water_price = water_price
        self.energy_price = energy_price
        self.average_income = average_income
        self.neighbor_radius = neighbor_radius

    @property
    def infrastructure(self):
        result = None
        if self.model is not None:
            result = self.model.infrastructure
        return result

    @property
    def gini_index(self) -> float:
        """
        Calculate the current gini index of society
        """
        data = []
        for id in self.agents:
            data.append(self.wealth(id))
        return gini.coefficient(data)

    '''
    def trade(self, agents: list, market: int = None):
        # Load data to solver
        info = []
        if market is not None:
            market_info = {
                'id': market,
                'resources': {
                    'food': self.infrastructure.food(market),
                    'water': self.infrastructure.water(market),
                    'energy': self.infrastructure.energy(market),
                },
                'enough_resources': {
                    'food': self.infrastructure.enough_food(market),
                    'water': self.infrastructure.enough_water(market),
                    'energy': self.infrastructure.enough_energy(market),
                },
                'balance': self.infrastructure.balance(market)
            }
            info.append(market_info)
        for agent_id in agents:
            agent_info = {
                'id': agent_id,
                'resources': {
                    'food': self.food(agent_id),
                    'water': self.water(agent_id),
                    'energy': self.energy(agent_id),
                },
                'enough_resources': {
                    'food': self.enough_food(agent_id),
                    'water': self.enough_water(agent_id),
                    'energy': self.enough_energy(agent_id),
                },
                'balance': self.balance(agent_id)
            }
            info.append(agent_info)
        prices = {
            'food': self.food_price,
            'water': self.water_price,
            'energy': self.energy_price
        }
        # Solve
        result = trade_solver(info, prices)
        #log = []
        # Apply results to the model
        for i, info in enumerate(result):
            id = info['id']
            if market is not None and i == 0:
                self.infrastructure.food(market, new_val=info['resources']['food'])
                self.infrastructure.water(market, new_val=info['resources']['water'])
                self.infrastructure.energy(market, new_val=info['resources']['energy'])
                self.infrastructure.balance(market, new_val=info['balance'])
            else:
                self.food(id, new_val=info['resources']['food'])
                self.water(id, new_val=info['resources']['water'])
                self.energy(id, new_val=info['resources']['energy'])
                self.balance(id, new_val=info['balance'])
        #return log

    
    '''
    def accessibility_resource(self, id: int, name: str):
        amount = self.get_resource(id=id, name=name)
        enough_amount = self.get_enough_resource(id=id, name=name)
        return accessibility(resource=amount, enough_resource=enough_amount)
    
    def accessibility(self, id: int) -> dict:
        return {
            'food': self.accessibility_resource(id=id, name='food'),
            'water': self.accessibility_resource(id=id, name='water'),
            'energy': self.accessibility_resource(id=id, name='energy')
        }
    


if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate_agents(num=1)
    print(model.society)