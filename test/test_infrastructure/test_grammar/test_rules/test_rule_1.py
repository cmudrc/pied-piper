import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Junction, Road, Settlement
from piperabm.infrastructure.grammar.rules import Rule_1


class TestGrammarRule1CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_0(self):
        object = Settlement(pos=[0, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)

    def test_1(self):
        object = Settlement(pos=[-0.5, 0.5])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)
    
    def test_2(self):
        object = Settlement(pos=[0.5, 0.5])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)

    def test_3(self):
        object = Settlement(pos=[3, 0.5])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertTrue(result)

    def test_4(self):
        object = Settlement(pos=[3, 3])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)
    
    def test_5(self):
        object = Settlement(pos=[-3, 3])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)

    def test_5(self):
        object = Settlement(pos=[3, 1])
        object.id = 1
        self.model.add(object)
        rule = Rule_1(self.model)
        result = rule.check(node_id=1, edge_id=0)
        self.assertFalse(result)


class TestGrammarRule1ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_apply_0(self):
        object = Junction(pos=[3, 0.5])
        object.id = 1
        self.model.add(object)
        self.assertEqual(len(self.model.infrastructure_nodes), 3)
        self.assertListEqual(self.model.infrastructure_edges, [0])
        rule = Rule_1(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 7)
        self.assertEqual(len(self.model.infrastructure_edges), 2)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 7)
        self.assertEqual(len(self.model.infrastructure_edges), 2)

    def test_apply_1(self):
        object = Junction(pos=[3, 0.5])
        object.id = 1
        self.model.add(object)
        object = Junction(pos=[7, -0.5])
        object.id = 2
        self.model.add(object)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertListEqual(self.model.infrastructure_edges, [0])
        rule = Rule_1(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 8)
        self.assertEqual(len(self.model.infrastructure_edges), 2)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 12)
        self.assertEqual(len(self.model.infrastructure_edges), 3)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 12)
        self.assertEqual(len(self.model.infrastructure_edges), 3)
    
        
if __name__ == "__main__":
    unittest.main()