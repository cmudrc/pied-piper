import unittest
import os
from copy import deepcopy

from piperabm import Model
from piperabm.infrastructure.samples.infrastructure_1 import model
from piperabm.tools.json_file import JsonFile


class TestFileClass(unittest.TestCase):
    """
    Test file management
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

    def test_file(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.model.path = path
        model_initial = deepcopy(self.model)

        self.model.run(n=1, report=False, save=True, step_size=50) # Run

        self.assertNotEqual(model_initial.serialize(), self.model.serialize()) # Model changed
        new_model = Model(path=path)
        new_model.load_initial()
        self.assertEqual(new_model.serialize(), model_initial.serialize()) # State saving

        deltas = new_model.load_deltas()
        new_model.apply_delta(deltas[0])
        self.assertEqual(new_model.serialize(), self.model.serialize()) # Detla

        model_initial.load_final()
        self.assertEqual(model_initial.serialize(), self.model.serialize()) # Final

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