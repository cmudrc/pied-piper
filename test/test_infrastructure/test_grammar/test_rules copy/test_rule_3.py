import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.infrastructure.grammar.rules import Rule_3


class TestGrammarRule3CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        self.rule = Rule_3(self.model)
        self.item = Road(pos_1=[0, 0], pos_2=[10, 0])

    def test_on(self):
        item = Road(pos_1=[0.5, 0], pos_2=[9.5, 0])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_out(self):
        item = Road(pos_1=[-3, 0], pos_2=[13, 0])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_in(self):
        item = Road(pos_1=[3, 0], pos_2=[7, 0])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)


class TestGrammarRule3ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        self.model.add(item)

    def test_apply(self):
        model = deepcopy(self.model)
        item = Road(pos_1=[0.5, 0], pos_2=[9.5, 0])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        rule = Rule_3(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 1)


if __name__ == '__main__':
    unittest.main()