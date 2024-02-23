import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.infrastructure.grammar.rules import Rule_3


class TestGrammarRule3CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[10, 0])
        object.id = 0
        self.model.add(object)

    def test_on(self):
        object = Road(pos_1=[0.5, 0], pos_2=[9.5, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_3(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertTrue(result)

    def test_out(self):
        object = Road(pos_1=[-3, 0], pos_2=[13, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_3(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)

    def test_in(self):
        object = Road(pos_1=[3, 0], pos_2=[7, 0])
        object.id = 1
        self.model.add(object)
        rule = Rule_3(self.model)
        result = rule.check(edge_id=0, other_edge_id=1)
        self.assertFalse(result)


class TestGrammarRule3ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        self.model.add(item)

    def test_apply(self):
        object = Road(pos_1=[0.5, 0], pos_2=[9.5, 0])
        object.id = 1
        self.model.add(object)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 2)
        rule = Rule_3(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 1)


if __name__ == "__main__":
    unittest.main()