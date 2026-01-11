import unittest
import os
import shutil
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_1 import model
from piperabm.model import Measurement
from piperabm.society.actions.action import Move


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
                "food": 0.003,
                "water": 0.003,
                "energy": 0.003,
            },
            enough_resources={
                "food": 100,
                "water": 100,
                "energy": 100,
            },
            balance=100,
        )
        action_queue = self.model.society.actions[self.id_agent]
        path = self.model.infrastructure.path(
            id_start=self.model.society.get_current_node(id=self.id_agent),
            id_end=self.id_end,
        )
        move = Move(action_queue=action_queue, path=path, usage=1)
        action_queue.add(move)

        # Build measurement object
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.model.path = self.file_path

        self.model.run(n=2, report=False, save=True, step_size=10)  # Run

        self.measurement = Measurement(path=self.file_path)
        self.measurement.measure(report=False)

    def tearDown(self):
        shutil.rmtree(os.path.join(self.file_path, "result"))

    def test_measurement(self):
        deltas = self.model.load_deltas()
        len_deltas = len(deltas)
        len_times = len(self.measurement.times)
        self.assertEqual(len_deltas + 1, len_times)
        len_travel_distances = len(self.measurement.travel_distance.values)
        self.assertEqual(len_deltas, len_travel_distances)
        len_accessibilities_0 = len(self.measurement.accessibility.values[0])
        self.assertEqual(len_deltas, len_accessibilities_0)

    def test_sum_agents(self):
        result = self.measurement.accessibility.sum_agents()
        self.assertAlmostEqual(sum(result), 0, places=2)


if __name__ == "__main__":
    unittest.main()
