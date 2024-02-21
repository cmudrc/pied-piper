import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Junction, Settlement
from piperabm.infrastructure.grammar.rules import Rule_0


class TestGrammarRule0CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        self.rule = Rule_0(self.model)
        self.item = Junction(pos=[0, 0])

    def test_0(self):
        item = Junction(pos=[0, 0])
        result = self.rule.check(self.item, item)
        self.assertTrue(result)

    def test_1(self):
        item = Junction(pos=[0.5, 0.5])
        result = self.rule.check(self.item, item)
        self.assertTrue(result)

    def test_2(self):
        item = Junction(pos=[1, 0])
        result = self.rule.check(self.item, item)
        self.assertFalse(result)

    def test_3(self):
        item = Junction(pos=[1.5, 0])
        result = self.rule.check(self.item, item)
        self.assertFalse(result)

    def test_4(self):
        item = Settlement(pos=[0.5, 0.5])
        result = self.rule.check(self.item, item)
        self.assertTrue(result)

    def test_5(self):
        item_1 = Settlement(pos=[0, 0])
        item_2 = Settlement(pos=[0.5, 0.5])
        rule = Rule_0(self.model)
        result = rule.check(item_1, item_2)
        self.assertFalse(result)


class TestGrammarRule0ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Junction(pos=[0, 0]) 
        self.model.add(item)

    def test_apply_0(self):
        '''
        Two nodes close to each other
        '''
        model = deepcopy(self.model)
        item = Junction(pos=[0, 0])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 2)
        rule = Rule_0(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 1)

    def test_apply_1(self):
        '''
        Two nodes far from each other
        '''
        model = deepcopy(self.model)
        item = Junction(pos=[3, 3])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 2)
        rule = Rule_0(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 2)

    def test_apply_2(self):
        '''
        Three nodes close to each other.
        '''
        model = deepcopy(self.model)
        item = Junction(pos=[0.1, 0])
        model.add(item)
        item = Junction(pos=[0, 0.1])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 3)
        rule = Rule_0(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 2)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 1)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 1)


if __name__ == '__main__':
    unittest.main()