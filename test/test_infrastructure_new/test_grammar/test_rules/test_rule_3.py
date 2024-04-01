import unittest

from piperabm.infrastructure_new import Infrastructure, Street, Home
from piperabm.infrastructure_new.grammar.rules import Rule_3


class TestGrammarRule4Class(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure()
        object = Street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add(object)

    def test_0(self):
        object = Home(pos=[5, 4])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)
    
    def test_1(self):
        object = Home(pos=[5, 4])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)

   
    def test_2(self):
        object = Home(pos=[5, 0])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)

    def test_3(self):
        object = Home(pos=[-2, 0])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)

    def test_4(self):
        object = Home(pos=[-1, 0])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)

    def test_5(self):
        object = Home(pos=[-2, -2])
        self.infrastructure.add(object, id=1)
        rule = Rule_3(self.infrastructure, proximity_radius=1)
        # Check
        result = rule.check(node_id=1)
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 3)
        self.assertEqual(len(self.infrastructure.edges_id), 1)
        rule.apply(node_id=1)
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 3)


if __name__ == "__main__":
    unittest.main()