import unittest

from piperabm.model import Model
from piperabm.infrastructure import Junction, Settlement, Road
from piperabm.infrastructure.grammar.rules import Rule_0


class TestGrammarRule0CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Settlement(pos=[0, 0])
        object.id = 0
        self.model.add(object)

    def test_0(self):
        object = Junction(pos=[0, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model.infrastructure)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertTrue(result)

    def test_1(self):
        object = Junction(pos=[1, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model.infrastructure)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertFalse(result)
    
    def test_2(self):
        object = Settlement(pos=[0.5, 0.5])
        object.id = 1
        self.model.add(object)
        rule = Rule_0(self.model.infrastructure)
        result = rule.check(node_id=0, other_node_id=1)
        self.assertFalse(result)


class TestGrammarRule0ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Settlement(pos=[0, 0])
        object.id = 0
        self.model.add(object)

    def test_apply_0(self):
        """
        Two nodes close to each other
        """
        object = Junction(pos=[0, 0])
        object.id = 1
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure.nodes_id, [0, 1])
        rule = Rule_0(self.model.infrastructure)
        rule.apply()
        self.assertListEqual(self.model.infrastructure.nodes_id, [0])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 1)
        rule.apply()
        self.assertListEqual(self.model.infrastructure.nodes_id, [0])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 1)

    def test_apply_1(self):
        """
        Two nodes far from each other
        """
        object = Junction(pos=[2, 2])
        object.id = 1
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure.nodes_id, [0, 1])
        self.assertEqual(len(self.model.all), 2)
        rule = Rule_0(self.model.infrastructure)
        rule.apply()
        self.assertListEqual(self.model.infrastructure.nodes_id, [0, 1])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 2)
        rule.apply()
        self.assertListEqual(self.model.infrastructure.nodes_id, [0, 1])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 2)

    def test_apply_2(self):
        """
        Three nodes close to each other.
        """
        object = Junction(pos=[0.1, 0])
        object.id = 1
        self.model.add(object)
        object = Junction(pos=[0, 0.1])
        object.id = 2
        self.model.add(object)
        self.assertListEqual(self.model.infrastructure.nodes_id, [0, 1, 2])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 3)
        rule = Rule_0(self.model.infrastructure)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure.nodes_id), 2)
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 2)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure.nodes_id), 1)
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 1)
        rule.apply()
        self.assertListEqual(self.model.infrastructure.nodes_id, [0])
        self.assertEqual(len(self.model.infrastructure.edges_id), 0)
        self.assertEqual(len(self.model.all), 1)


if __name__ == "__main__":
    unittest.main()