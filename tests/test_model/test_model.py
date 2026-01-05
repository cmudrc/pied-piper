import unittest

from piperabm.model import Model
from piperabm.exceptions import ModelNotBakedError


class TestModelClass(unittest.TestCase):
    """
    Test Model
    """

    def setUp(self) -> None:
        model = Model()
        model.infrastructure.coeff_usage = 1
        model.infrastructure.coeff_age = 1
        model.infrastructure.add_street(pos_1=[0, 0], pos_2=[-60, 40], name="road")
        model.infrastructure.add_home(pos=[5, 0], id=1, name="home")
        model.infrastructure.add_market(
            pos=[-60, 45],
            id=2,
            name="market",
            resources={"food": 100, "water": 100, "energy": 100},
        )
        model.society.average_income = 1
        self.model = model
        self.agent_id = 1
        self.home_id = self.model.infrastructure.homes[0]

    def test_add_to_baked_infrastructure(self):
        """
        Test that adding elements to a baked infrastructure raises an error.
        """
        with self.assertRaises(ModelNotBakedError):
            self.model.society.add_agent(
                id=self.agent_id,
                home_id=self.home_id,
                socioeconomic_status=1,
                resources={
                    "food": 1,
                    "water": 1,
                    "energy": 1,
                },
                balance=100,
            )
        
        # Now bake the model and try again
        self.model.bake()
        self.model.society.add_agent(
            id=self.agent_id,
            home_id=self.home_id,
            socioeconomic_status=1,
            resources={
                "food": 1,
                "water": 1,
                "energy": 1,
            },
            balance=100,
        )
    
    def test_change_infrastructure_after_baking(self):
        """
        Test that adding elements to a baked infrastructure raises an error.
        """
        self.assertFalse(self.model.baked)
        self.model.bake()
        self.assertTrue(self.model.baked)
        self.model.infrastructure.add_home(pos=[10, 10])
        self.assertFalse(self.model.baked)

    def test_running_unbaked_model(self):
        """
        Test that running an unbaked model raises an error.
        """
        try:
            self.model.run(n=1)
        except ValueError as e:
            self.assertIn("Model is not baked", str(e))
            return


if __name__ == "__main__":
    unittest.main()
