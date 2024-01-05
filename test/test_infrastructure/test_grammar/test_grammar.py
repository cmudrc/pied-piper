import unittest

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.infrastructure.grammar import Grammar


class TestInfrastructureGrammarClass_0(unittest.TestCase):

    def setUp(self) -> None:
        model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[10, 0])
        model.add(item)
        item = Road(pos_1=[0, 5], pos_2=[10, 5])
        model.add(item)
        item = Road(pos_1=[5, 0], pos_2=[5, 10])
        model.add(item)
        self.grammar = Grammar(model)

    def test_apply(self):
        model = self.grammar.model
        self.assertEqual(len(model.all_environment_nodes), 6)
        self.assertEqual(len(model.all_environment_edges), 3)
        self.grammar.apply()
        self.assertEqual(len(model.all_environment_nodes), 7)
        self.assertEqual(len(model.all_environment_edges), 6)


class TestInfrastructureGrammarClass_1(unittest.TestCase):

    def setUp(self) -> None:
        eps = 0.5
        model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0+eps], pos_2=[10, 0])
        model.add(item)
        item = Road(pos_1=[10, 0+eps], pos_2=[10, 10])
        model.add(item)
        item = Road(pos_1=[10, 10+eps], pos_2=[0, 10])
        model.add(item)
        item = Road(pos_1=[0, 10+eps], pos_2=[0, 0])
        model.add(item)
        self.grammar = Grammar(model)

    def test_apply(self):
        model = self.grammar.model
        self.assertEqual(len(model.all_environment_nodes), 8)
        self.assertEqual(len(model.all_environment_edges), 4)
        self.grammar.apply()
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 4)


class TestInfrastructureGrammarClass_2(unittest.TestCase):

    def setUp(self) -> None:
        model = Model(proximity_radius=1)
        a = 5
        b = 2 * a
        item = Road(pos_1=[0, -b], pos_2=[0, b])
        model.add(item)
        item = Road(pos_1=[-b, 0], pos_2=[b, 0])
        model.add(item)
        item = Road(pos_1=[a, a], pos_2=[a, -a])
        model.add(item)
        item = Road(pos_1=[a, -a], pos_2=[-a, -a])
        model.add(item)
        item = Road(pos_1=[-a, -a], pos_2=[-a, a])
        model.add(item)
        item = Road(pos_1=[-a, a], pos_2=[a, a])
        model.add(item)
        self.grammar = Grammar(model)

    def test_apply(self):
        model = self.grammar.model
        self.assertEqual(len(model.all_environment_nodes), 4+8)
        self.assertEqual(len(model.all_environment_edges), 6)
        self.grammar.apply()
        self.assertEqual(len(model.all_environment_nodes), 13)
        self.assertEqual(len(model.all_environment_edges), 16)


class TestInfrastructureGrammarClass_3(unittest.TestCase):

    def setUp(self) -> None:
        model = Model(proximity_radius=1)
        item = Road(pos_1=[0, 0], pos_2=[0, 10])
        model.add(item)
        item = Settlement(pos=[5, 4])
        model.add(item)
        self.grammar = Grammar(model)

    def test_apply(self):
        model = self.grammar.model
        self.assertEqual(len(model.all_environment_nodes), 3)
        self.assertEqual(len(model.all_environment_edges), 1)
        self.grammar.apply()
        self.assertEqual(len(model.all_environment_nodes), 4)
        self.assertEqual(len(model.all_environment_edges), 3)


if __name__ == "__main__":
    unittest.main()