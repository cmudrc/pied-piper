import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.infrastructure import Junction, Road
from piperabm.infrastructure.grammar_new.rules import Rule_2


class TestGrammarRule2CheckClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        self.rule = Rule_2(self.model)
        self.item = Road(pos_1=[0, 0], pos_2=[10, 0])

    def test_0(self):
        item = Road(pos_1=[0, 5], pos_2=[0, -5])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_1(self):
        item = Road(pos_1=[-2, 5], pos_2=[-2, -5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_2(self):
        item = Road(pos_1=[0.5, 5], pos_2=[0.5, -5])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_3(self):
        item = Road(pos_1=[-0.5, 5], pos_2=[-0.5, -5])
        result = self.rule.check(item, self.item)
        self.assertTrue(result)

    def test_4(self):
        item = Road(pos_1=[1, 5], pos_2=[1, -5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)

    def test_5(self):
        item = Road(pos_1=[-1, 5], pos_2=[-1, -5])
        result = self.rule.check(item, self.item)
        self.assertFalse(result)


class TestGrammarRule2ApplyClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        self.model.add(item)


if __name__ == "__main__":
    unittest.main()