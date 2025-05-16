import numpy as np

from piperabm.tools.gini import gini
from piperabm.society.info import *


class Generate:
    """
    Generate agents
    """

    def generate(
            self,
            num: int = 1,
            gini_index: float = 0,
            average_resources: dict = {
                'food': 10,
                'water': 10,
                'energy': 10,
            },
            average_balance: float = 0
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
        for value in socioeconomic_status_values:
            socioeconomic_status = float(value)
            home_id = int(np.random.choice(homes_id))
            resources = {}
            for name in average_resources:
                resources[name] = average_resources[name] * socioeconomic_status
            balance = average_balance * socioeconomic_status 
            self.add_agent(
                home_id=home_id,
                socioeconomic_status=socioeconomic_status,
                resources=resources,
                balance=balance
            )


if __name__ == "__main__":

    from piperabm.infrastructure.samples.infrastructure_0 import model

    model.set_seed(2)
    model.society.generate(
        gini_index=0.45,
        num=2,
        average_balance=1000
    )
    model.set_seed(None)

    print("gini index: ", model.society.gini_index)
    print("society serialized:\n", model.society.serialize())
    