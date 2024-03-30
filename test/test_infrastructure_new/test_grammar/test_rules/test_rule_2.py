import unittest

from piperabm.infrastructure_new import Infrastructure, Street, NeighborhoodAccess
from piperabm.infrastructure_new.grammar.rules import Rule_2


class TestGrammarRule2Class(unittest.TestCase):

    def setUp(self) -> None:
        self.infrastructure = Infrastructure(proximity_radius=1)
        object = Street(pos_1=[0, 0], pos_2=[10, 0])
        self.infrastructure.add(object)

    def test_in(self):
        object = NeighborhoodAccess(pos_1=[5, 5], pos_2=[5, -5])
        self.infrastructure.add(object)
        rule = Rule_2(self.infrastructure)
        edges = self.infrastructure.edges_id
        # Check
        result, intersection = rule.check(edge_id=edges[0], other_edge_id=edges[1])
        self.assertTrue(result)
        # Apply
        self.assertEqual(len(self.infrastructure.nodes_id), 4)
        self.assertEqual(len(self.infrastructure.edges_id), 2)
        rule.apply(edge_id=edges[0], other_edge_id=edges[1], intersection=intersection)
        self.assertEqual(len(self.infrastructure.nodes_id), 12)
        self.assertEqual(len(self.infrastructure.edges_id), 4)

    def test_passing_ends(self):
        object = NeighborhoodAccess(pos_1=[0.5, 5], pos_2=[0.5, -5])
        self.infrastructure.add(object)
        rule = Rule_2(self.infrastructure)
        edges = self.infrastructure.edges_id
        # Check
        result, intersection = rule.check(edge_id=edges[0], other_edge_id=edges[1])
        self.assertFalse(result)
    
    def test_out(self):
        object = NeighborhoodAccess(pos_1=[-2, 5], pos_2=[-2, -5])
        self.infrastructure.add(object)
        rule = Rule_2(self.infrastructure)
        edges = self.infrastructure.edges_id
        # Check
        result, intersection = rule.check(edge_id=edges[0], other_edge_id=edges[1])
        self.assertFalse(result)

    def test_parallel(self):
        object = NeighborhoodAccess(pos_1=[2, -1], pos_2=[2, 11])
        self.infrastructure.add(object)
        rule = Rule_2(self.infrastructure)
        edges = self.infrastructure.edges_id
        # Check
        result, intersection = rule.check(edge_id=edges[0], other_edge_id=edges[1])
        self.assertFalse(result)

    def test_on(self):
        object = NeighborhoodAccess(pos_1=[2, 0], pos_2=[8, 0])
        self.infrastructure.add(object)
        rule = Rule_2(self.infrastructure)
        edges = self.infrastructure.edges_id
        # Check
        result, intersection = rule.check(edge_id=edges[0], other_edge_id=edges[1])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()