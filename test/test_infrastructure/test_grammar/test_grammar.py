import unittest

from piperabm.model import Model
from piperabm.infrastructure import Road, Settlement
from piperabm.infrastructure.grammar import Grammar


class TestInfrastructureGrammarClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
        object_2 = Road(pos_1=[0, 5], pos_2=[10, 5])
        object_3 = Road(pos_1=[5, 0], pos_2=[5, 10])
        self.model.add(object_1, object_2, object_3)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 6)
        self.assertEqual(len(self.model.infrastructure_edges), 3)
        grammar.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 7)
        self.assertEqual(len(self.model.infrastructure_edges), 6)
        #self.model.show()


class TestInfrastructureGrammarClass_1(unittest.TestCase):

    def setUp(self) -> None:
        eps = 0.5
        a = 100
        self.model = Model(proximity_radius=1)
        object_1 = Road(pos_1=[0, 0+eps], pos_2=[a, 0])
        object_2 = Road(pos_1=[a, 0+eps], pos_2=[a, a])
        object_3 = Road(pos_1=[a, a+eps], pos_2=[0, a])
        object_4 = Road(pos_1=[0, a+eps], pos_2=[0, 0])
        self.model.add(object_1, object_2, object_3, object_4)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 8)
        self.assertEqual(len(self.model.infrastructure_edges), 4)
        grammar.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 4)
        #self.model.show()


class TestInfrastructureGrammarClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        a = 5
        b = 2 * a
        object_1 = Road(pos_1=[0, -b], pos_2=[0, b])
        object_2 = Road(pos_1=[-b, 0], pos_2=[b, 0])
        object_3 = Road(pos_1=[a, a], pos_2=[a, -a])
        object_4 = Road(pos_1=[a, -a], pos_2=[-a, -a])
        object_5 = Road(pos_1=[-a, -a], pos_2=[-a, a])
        object_6 = Road(pos_1=[-a, a], pos_2=[a, a])
        self.model.add(object_1, object_2, object_3, object_4, object_5, object_6)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 4+8)
        self.assertEqual(len(self.model.infrastructure_edges), 6)
        grammar.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 13)
        self.assertEqual(len(self.model.infrastructure_edges), 16)
        #self.model.show()


class TestInfrastructureGrammarClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
        object_1.id = 1
        object_2 = Settlement(pos=[5, 0.5])
        object_2.id = 2
        self.model.add(object_1, object_2)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 3)
        self.assertEqual(len(self.model.infrastructure_edges), 1)
        grammar.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 3)
        #self.model.show()


class TestInfrastructureGrammarClass_4(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object_1 = Road(pos_1=[0, 0], pos_2=[10, 0])
        object_1.id = 1
        object_2 = Settlement(pos=[5, 0.5])
        object_2.id = 2
        object_3 = Settlement(pos=[4.5, 1])
        object_3.id = 3
        self.model.add(object_1, object_2, object_3)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 1)
        grammar.apply()
        self.assertEqual(len(self.model.infrastructure_nodes), 5)
        self.assertEqual(len(self.model.infrastructure_edges), 4)
        #self.model.show()


class TestInfrastructureGrammarClass_5(unittest.TestCase):

    def setUp(self) -> None:
        self.model = Model(proximity_radius=1)
        object_1 = Road(pos_1=[0, 0], pos_2=[0, 10])
        object_1.id = 1
        object_2 = Settlement(pos=[-5, 5])
        object_2.id = 2
        object_3 = Settlement(pos=[-0.9, 4.5])
        object_3.id = 4
        self.model.add(object_1, object_2, object_3)

    def test_apply(self):
        grammar = Grammar(self.model, save=False)
        self.assertEqual(len(self.model.infrastructure_nodes), 4)
        self.assertEqual(len(self.model.infrastructure_edges), 1)
        grammar.apply(report=True)
        self.assertEqual(len(self.model.infrastructure_nodes), 5)
        self.assertEqual(len(self.model.infrastructure_edges), 4)
        self.model.show()


if __name__ == "__main__":
    unittest.main()