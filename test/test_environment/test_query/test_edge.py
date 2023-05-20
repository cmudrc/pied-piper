import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_1
from piperabm.environment.infrastructure.road.samples import road_0


class TestEnvironmentEdgeQuery(unittest.TestCase):

    def setUp(self) -> None:
        self.env = deepcopy(environment_1)

    def test_all_edges(self):
        edges = self.env.all_edges()
        expected_result = [(0, 2), (1, 2)]
        self.assertListEqual(edges, expected_result)
        self.assertTrue(self.env.G.has_edge(2, 0))

    def test_get_edge_object(self):
        structure = self.env.get_edge_object(2, 0)
        dictionary = structure.to_dict()
        dictionary['boundary'] = None
        road_dictionary = road_0.to_dict()
        road_dictionary['boundary'] = None
        self.assertDictEqual(dictionary, road_dictionary)
        
    def test_get_edge_pos(self):
        pos = self.env.get_edge_pos(2, 0)
        self.assertEqual(pos, [9, -1])  

    def test_oldest_edge(self):
        oldest_edge = self.env.oldest_edge()
        self.assertListEqual(list(oldest_edge), [0, 2])  


if __name__ == "__main__":
    unittest.main()