import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Junction, Road
from piperabm.infrastructure.grammar.rules import Rule_1


class TestGrammarRule1CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        self.rule = Rule_1(self.model)
        self.item = Road(pos_1=[0, 0], pos_2=[10, 0])

    def test_0(self):
        item = Junction(pos=[-0.5, 0.5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_1(self):
        item = Junction(pos=[0.5, 0.5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_2(self):
        item = Junction(pos=[3, 0.5])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_3(self):
        item = Junction(pos=[3, 3])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_4(self):
        item = Junction(pos=[-3, 3])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_5(self):
        item = Junction(pos=[3, 1])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)


class TestGrammarRule1ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        self.model.add(item)

    def test_apply_0(self):
        model = deepcopy(self.model)
        item = Junction(pos=[3, 0.5])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 1)
        rule = Rule_1(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 7)
        self.assertEqual(len(model.all_environment_edges), 2)

    def test_apply_1(self):
        model = deepcopy(self.model)
        item = Junction(pos=[3, 0.5])
        model.add(item)
        item = Junction(pos=[7, -0.5])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 1)
        rule = Rule_1(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 8)
        self.assertEqual(len(model.all_environment_edges), 2)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 12)
        self.assertEqual(len(model.all_environment_edges), 3)

if __name__ == "__main__":
    unittest.main()