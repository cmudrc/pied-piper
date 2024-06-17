import unittest

from piperabm.infrastructure import Infrastructure
from piperabm.infrastructure.grammar import Grammar


class TestInfrastructureGrammarClass_0(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_street(pos_1=[0, 5], pos_2=[10, 5])
        self.infrastructure.add_street(pos_1=[5, 0], pos_2=[5, 10])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 6)
        self.assertEqual(len(self.infrastructure.edges_id), 3)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 7)
        self.assertEqual(len(self.infrastructure.edges_id), 6)


class TestInfrastructureGrammarClass_1(unittest.TestCase):

    def setUp(self) -> None:
        eps = 0.5
        a = 100
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0+eps], pos_2=[a, 0])
        self.infrastructure.add_street(pos_1=[a, 0+eps], pos_2=[a, a])
        self.infrastructure.add_street(pos_1=[a, a+eps], pos_2=[0, a])
        self.infrastructure.add_street(pos_1=[0, a+eps], pos_2=[0, 0])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 8)
        self.assertEqual(len(self.infrastructure.edges_id), 4)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 4)


class TestInfrastructureGrammarClass_2(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        a = 5
        b = 2 * a
        self.infrastructure.add_street(pos_1=[0, -b], pos_2=[0, b])
        self.infrastructure.add_street(pos_1=[-b, 0], pos_2=[b, 0])
        self.infrastructure.add_street(pos_1=[a, a], pos_2=[a, -a])
        self.infrastructure.add_street(pos_1=[a, -a], pos_2=[-a, -a])
        self.infrastructure.add_street(pos_1=[-a, -a], pos_2=[-a, a])
        self.infrastructure.add_street(pos_1=[-a, a], pos_2=[a, a])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 12)
        self.assertEqual(len(self.infrastructure.edges_id), 6)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 13)
        self.assertEqual(len(self.infrastructure.edges_id), 16)


class TestInfrastructureGrammarClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[5, 0.5])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply(report=False)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)
        #self.infrastructure.show()


class TestInfrastructureGrammarClass_4(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add_home(pos=[5, 0.5])
        self.infrastructure.add_home(pos=[4.5, 1])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 5)
        self.assertEqual(len(self.infrastructure.edges_id), 4)
        self.infrastructure.show()


class TestInfrastructureGrammarClass_5(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        self.infrastructure.add_street(pos_1=[0, 0], pos_2=[0, 10])
        self.infrastructure.add_home(pos=[-5, 5])
        self.infrastructure.add_home(pos=[-0.9, 4.5])

    def test_apply(self):
        grammar = Grammar(self.infrastructure, proximity_radius=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        grammar.apply()
        self.assertEqual(len(self.infrastructure.nodes_id), 6)
        self.assertEqual(len(self.infrastructure.edges_id), 5)
        #self.infrastructure.show()


if __name__ == "__main__":
    unittest.main()