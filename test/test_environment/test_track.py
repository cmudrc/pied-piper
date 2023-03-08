import unittest
from copy import deepcopy

from piperabm.environment.sample import env_0
from piperabm.environment.path_graph.track import Track
from piperabm.unit import Date


class TestTrackClass(unittest.TestCase):

    def setUp(self):
        self.env = env_0

    def test_to_path_graph_6(self):
        env = deepcopy(self.env)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 7)
        env.update_elements(start_date, end_date)
        path_graph = env.to_path_graph(start_date, end_date)
        nodes_count = path_graph.G.number_of_nodes()
        self.assertEqual(nodes_count, 2)
        edges_count = path_graph.G.number_of_edges()
        self.assertEqual(edges_count, 2)


if __name__ == "__main__":
    unittest.main()