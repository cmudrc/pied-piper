import unittest
import os
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_1 import model
from piperabm.model import Measurement
from piperabm.tools.json_file import JsonFile


class TestMeasurementClass(unittest.TestCase):
    """
    Test Measurement
    """
    def setUp(self) -> None:
        self.id_agent = 0
        self.id_start = 1
        self.id_end = 2
        self.model = deepcopy(model)
        self.model.society.add_agent(
            socioeconomic_status=1,
            id=self.id_agent,
            home_id=self.id_start,
            resources={
                'food': 0.003,
                'water': 0.003,
                'energy': 0.003,
            },
            enough_resources={
                'food': 100,
                'water': 100,
                'energy': 100,
            },
            balance=100
        )
        self.model.society.go_and_comeback_and_stay(agent_id=self.id_agent, destination_id=self.id_end)

    def test_measurement(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.model.path = path

        self.model.run(n=10, report=False, save=True, step_size=40) # Run
        measurement = Measurement(path=path)
        deltas = self.model.load_deltas()
        #print(len(deltas))
        #print(len(measurement.accessibility.values))

        filenames = [
            'model_final',
            'model_initial',
            'model_simulation',
        ]
        for filename in filenames:
            file = JsonFile(path=path, filename=filename)
            file.remove()


if __name__ == "__main__":
    unittest.main()