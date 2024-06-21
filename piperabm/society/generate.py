import random
from copy import deepcopy

from piperabm.tools.gini import gini


class Generate:
    """
    Generate agents
    """

    def generate_agents(
            self,
            num: int = 1,
            gini_index: float = 0,
            average_food: float = 10,
            average_water: float = 10,
            average_energy: float = 10,
            average_balance: float = 0,
        ):
        """
        Generate agents
        """
        distribution = gini.lognorm(gini_index)
        homes_id = self.infrastructure.homes
        for _ in range(num):
            home_id = random.choice(homes_id)
            socioeconomic_status = distribution.rvs()
            food = average_food * socioeconomic_status
            water = average_water * socioeconomic_status
            energy = average_energy * socioeconomic_status
            balance = average_balance * socioeconomic_status 
            self.add_agent(
                home_id=home_id,
                socioeconomic_status=socioeconomic_status,
                food=food,
                water=water,
                energy=energy,
                enough_food=deepcopy(food),
                enough_water=deepcopy(water),
                enough_energy=deepcopy(energy),
                balance=balance
            )