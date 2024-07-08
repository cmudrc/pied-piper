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
        self.maxDiff = None
        path = os.path.dirname(os.path.realpath(__file__))
        self.model.path = path
        model_initial = deepcopy(self.model) # Copy of initial state

        self.model.run(n=1, report=False, save=True, step_size=50) # Run

        self.assertNotEqual(model_initial.serialize(), self.model.serialize()) # Model changed
        
        # Load initial state from file
        new_model_initial = Model(path=path)
        new_model_initial.load_initial()
        self.assertEqual(new_model_initial.serialize(), model_initial.serialize()) # State saving

        # Load final state from file
        final_model = Model(path=path)
        final_model.load_final()
        #print(final_model.serialize())
        self.assertEqual(final_model.serialize(), self.model.serialize()) # Final
        
        # Push model forward using deltas
        deltas = new_model_initial.load_deltas()
        self.assertEqual(len(deltas), 1)
        new_model_initial.apply_delta(deltas[0])
        model_initial.push(steps=1)
        self.assertEqual(new_model_initial.serialize(), model_initial.serialize()) # Final

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