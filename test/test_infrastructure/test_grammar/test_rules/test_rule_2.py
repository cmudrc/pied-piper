import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.infrastructure.grammar.rules import Rule_2


class TestGrammarRule2CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        self.rule = Rule_2(self.model)
        self.item = Road(pos_1=[0, 0], pos_2=[10, 0])

    def test_in(self):
        item = Road(pos_1=[5, 5], pos_2=[5, -5])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_passing_ends(self):
        item = Road(pos_1=[0.5, 5], pos_2=[0.5, -5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_out(self):
        item = Road(pos_1=[-2, 5], pos_2=[-2, -5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_parallel(self):
        item = Road(pos_1=[2, -1], pos_2=[2, 11])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_on(self):
        item = Road(pos_1=[2, 0], pos_2=[8, 0])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)


class TestGrammarRule2ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        self.model.add(item)

    def test_apply(self):
        model = deepcopy(self.model)
        item = Road(pos_1=[5, 5], pos_2=[5, -5])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 2)
        rule = Rule_2(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 12)
        self.assertEqual(len(model.all_environment_edges), 4)


if __name__ == "__main__":
    unittest.main()