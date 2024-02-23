import unittest

from piperabm.model import Model
from piperabm.infrastructure import Road
from piperabm.infrastructure.grammar.rules import Rule_5


class TestGrammarRule0CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[0.5, 0])
        object.id = 0
        self.model.add(object)

    def test_0(self):
        rule = Rule_5(self.model)
        result = rule.check(0)
        self.assertTrue(result)

    def test_1(self):
        object = Road(pos_1=[0, 0], pos_2=[0, 5])
        object.id = 1
        self.model.add(object)
        rule = Rule_5(self.model)
        result = rule.check(1)
        self.assertFalse(result)


class TestGrammarRule0ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object = Road(pos_1=[0, 0], pos_2=[0.5, 0])
        object.id = 0
        self.model.add(object)

    def test_apply_0(self):
        """
        Two nodes close to each other
        """
        rule = Rule_5(self.model)
        self.assertEqual(len(self.model.infrastructure_nodes), 2)
        self.assertEqual(len(self.model.infrastructure_edges), 1)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 2)
        self.assertEqual(len(self.model.infrastructure_edges), 0)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 2)
        self.assertEqual(len(self.model.infrastructure_edges), 0)

    def test_apply_1(self):
        """
        Two nodes far from each other
        """
        object = Road(pos_1=[0, 0], pos_2=[0, 5])
        object.id = 1
        self.model.add(object)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 2)
        rule = Rule_5(self.model)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 1)
        rule.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 1)


if __name__ == "__main__":
    unittest.main()