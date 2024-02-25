import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.infrastructure.grammar.rules import Rule_2


class TestGrammarRule2CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_in(self):
        object = Road(pos_1=[5, 5], pos_2=[5, -5])
        object.id = 1
        self.model.add(object)
        rule = Rule_2(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertTrue(result)

    def test_passing_ends(self):
        object = Road(pos_1=[0.5, 5], pos_2=[0.5, -5])
        object.id = 1
        self.model.add(object)
        rule = Rule_2(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)

    def test_out(self):
        object = Road(pos_1=[-2, 5], pos_2=[-2, -5])
        object.id = 1
        self.model.add(object)
        rule = Rule_2(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)

    def test_parallel(self):
        object = Road(pos_1=[2, -1], pos_2=[2, 11])
        object.id = 1
        self.model.add(object)
        rule = Rule_2(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)

    def test_on(self):
        object = Road(pos_1=[2, 0], pos_2=[8, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_2(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)


class TestGrammarRule2ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_apply(self):
        object = Road(pos_1=[5, 5], pos_2=[5, -5])
        object.id = 1
        self.model.add(object)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 2)
        rule = Rule_2(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 12)
        self.assertEqual(len(self.model.infrastructure_edges), 4)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 12)
        self.assertEqual(len(self.model.infrastructure_edges), 4)


if __name__ == "__main__":
    unittest.main()