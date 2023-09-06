import unittest
from copy import deepcopy

from piperabm.unit import Date
from piperabm.environment_old import Environment
from piperabm.infrastructure.settlement.samples import settlement_0


class TestEnvironmentAddNode(unittest.TestCase):

    def setUp(self):
        self.env = Environment()

    def test_add_node(self):
        self.env.append_node(
            pos=[0, 0],
            structure=settlement_0
        )
        nodes = self.env.G.nodes()
        self.assertListEqual(list(nodes), [0])
        self.assertEqual(settlement_0, self.env.get_node_object(0))
        
    def test_input_to_index(self):
        index = self.env.input_to_index_node(name='John', pos=[0, 0])
        self.assertEqual(index, 0)
        
    def test_add_settlement(self):
        self.env.add_settlement(
            name='',
            pos=[0, 0],
            boundary=None,
            active=True,
            start_date=None,
            end_date=None,
            sudden_degradation_dist=None,
            sudden_degradation_unit_size=None,
            progressive_degradation_formula=None,
            progressive_degradation_current=None,
            progressive_degradation_max=None
        )
        nodes = self.env.G.nodes()
        self.assertListEqual(list(nodes), [0])


if __name__ == "__main__":
    unittest.main()