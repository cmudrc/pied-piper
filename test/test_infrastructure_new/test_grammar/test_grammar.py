import unittest

from piperabm.infrastructure_new import Infrastructure, Street, Home
from piperabm.infrastructure_new.grammar import Grammar


class TestInfrastructureGrammarClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
        object_2 = Street(pos_1=[0, 5], pos_2=[10, 5])
        object_3 = Street(pos_1=[5, 0], pos_2=[5, 10])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 6)
        self.assertEqual(len(self.infrastructure.edges_id), 3)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 7)
        self.assertEqual(len(self.infrastructure.edges_id), 6)


class TestInfrastructureGrammarClass_1(unittest.TestCase):

    def setUp(self) -> None:
        eps = 0.5
        a = 100
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0+eps], pos_2=[a, 0])
        object_2 = Street(pos_1=[a, 0+eps], pos_2=[a, a])
        object_3 = Street(pos_1=[a, a+eps], pos_2=[0, a])
        object_4 = Street(pos_1=[0, a+eps], pos_2=[0, 0])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)
        self.infrastructure.add(object_4)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 8)
        self.assertEqual(len(self.infrastructure.edges_id), 4)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 4)


class TestInfrastructureGrammarClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        a = 5
        b = 2 * a
        object_1 = Street(pos_1=[0, -b], pos_2=[0, b])
        object_2 = Street(pos_1=[-b, 0], pos_2=[b, 0])
        object_3 = Street(pos_1=[a, a], pos_2=[a, -a])
        object_4 = Street(pos_1=[a, -a], pos_2=[-a, -a])
        object_5 = Street(pos_1=[-a, -a], pos_2=[-a, a])
        object_6 = Street(pos_1=[-a, a], pos_2=[a, a])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)
        self.infrastructure.add(object_4)
        self.infrastructure.add(object_5)
        self.infrastructure.add(object_6)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 12)
        self.assertEqual(len(self.infrastructure.edges_id), 6)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 13)
        self.assertEqual(len(self.infrastructure.edges_id), 16)


class TestInfrastructureGrammarClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
        object_2 = Home(pos=[5, 0.5])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)


class TestInfrastructureGrammarClass_4(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0], pos_2=[10, 0])
        object_2 = Home(pos=[5, 0.5])
        object_3 = Home(pos=[4.5, 1])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 5)
        self.assertEqual(len(self.infrastructure.edges_id), 4)


class TestInfrastructureGrammarClass_5(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object_1 = Street(pos_1=[0, 0], pos_2=[0, 10])
        object_2 = Home(pos=[-5, 5])
        object_3 = Home(pos=[-0.9, 4.5])
        self.infrastructure.add(object_1)
        self.infrastructure.add(object_2)
        self.infrastructure.add(object_3)

    def test_apply(self):
        grammar = Grammar(self.infrastructure)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 5)
        self.assertEqual(len(self.infrastructure.edges_id), 4)


if __name__ == "__main__":
    unittest.main()