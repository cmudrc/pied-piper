import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.infrastructure.grammar.rules import Rule_4


class TestGrammarRule4CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        model.add(item)
        self.model = model
        self.rule = Rule_4(self.model)

    def test_0(self):
        item = Settlement(pos=[5, 4])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [0, -4])

    def test_1(self):
        item = Settlement(pos=[5, 1])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [0, -1])

    def test_2(self):
        item = Settlement(pos=[5, 0])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [0, 0])

    def test_3(self):
        item = Settlement(pos=[-2, 0])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [2, 0])

    def test_4(self):
        item = Settlement(pos=[-1, 0])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertFalse(result)
        self.assertListEqual(smallest_distance_vector, [1, 0])

    def test_4(self):
        item = Settlement(pos=[-2, -2])
        result, smallest_distance_vector = self.rule.check(item)
        self.assertTrue(result)
        self.assertListEqual(smallest_distance_vector, [2, 2])


class TestGrammarRule4ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        model.add(item)
        self.model = model

    def test_apply(self):
        model = deepcopy(self.model)
        item = Settlement(pos=[5, 4])
        model.add(item)
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 1)
        rule = Rule_4(model)
        rule.apply()
        self.assertEqual(len(model.all_environment_nodes), 5)
        self.assertEqual(len(model.all_environment_edges), 2)


if __name__ == "__main__":
    unittest.main()