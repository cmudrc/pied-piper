#import random
import numpy as np
from copy import deepcopy

from piperabm.tools.gini import gini


class Generate:
    """
    Generate agents
    """

    def generate(
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
        socioeconomic_status_values = distribution.rvs(
            sample_size=num,
            percision=0.03
        )
        homes_id = self.infrastructure.homes
        for socioeconomic_status in socioeconomic_status_values:
            home_id = int(np.random.choice(homes_id))
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


if __name__ == "__main__":

    from piperabm.infrastructure.samples import model_0 as model


    model.set_seed(2)
    model.society.generate(
        gini_index=0.45,
        num=2,
        average_balance=1000
    )
    print(model.society.gini_index)
    print(model.society.serialize())
    