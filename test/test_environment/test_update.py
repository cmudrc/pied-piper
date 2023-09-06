import unittest
from copy import deepcopy

from piperabm.environment_old.samples import environment_1
from piperabm.unit import Date


class TestEnvironmentUpdateClass(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_run(self):
        env = self.env

        start_date = Date(2020, 1, 1)
        end_date = Date(2020, 1, 2)
        env.update(start_date, end_date)
        current_graph = env.current
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 0)
        self.assertEqual(len(current_graph.G.edges()), 0)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 0)
        self.assertEqual(len(active_graph.G.edges()), 0)

        start_date = Date(2020, 1, 2)
        end_date = Date(2020, 1, 3)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 2)
        self.assertEqual(len(active_graph.G.edges()), 1)

        start_date = Date(2020, 1, 3)
        end_date = Date(2020, 1, 4)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 2)
        self.assertEqual(len(active_graph.G.edges()), 1)

        start_date = Date(2020, 1, 4)
        end_date = Date(2020, 1, 5)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 3)
        self.assertEqual(len(current_graph.G.edges()), 2)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 3)
        self.assertEqual(len(active_graph.G.edges()), 2)

        start_date = Date(2020, 1, 9)
        end_date = Date(2020, 1, 10)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 3)
        self.assertEqual(len(current_graph.G.edges()), 2)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 3)
        self.assertEqual(len(active_graph.G.edges()), 2)

        """
        This case is helpful for large burnout sessions, which may
        surpass the whole life span of object
        """
        start_date = Date(2020, 1, 10)
        end_date = Date(2020, 1, 11)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 3)
        self.assertEqual(len(env.current.G.edges()), 2)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 3)
        self.assertEqual(len(active_graph.G.edges()), 2)

        start_date = Date(2020, 1, 11)
        end_date = Date(2020, 1, 12)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 3)
        self.assertEqual(len(env.current.G.edges()), 2)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 2)
        self.assertEqual(len(active_graph.G.edges()), 1)
    
        start_date = Date(2020, 1, 12)
        end_date = Date(2020, 1, 13)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(env.current.G.edges()), 1)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 2)
        self.assertEqual(len(active_graph.G.edges()), 1)

        start_date = Date(2020, 1, 13)
        end_date = Date(2020, 1, 14)
        env.update(start_date, end_date)
        current_graph = env.current
        self.assertEqual(len(current_graph.G.nodes()), 2)
        self.assertEqual(len(current_graph.G.edges()), 1)
        active_graph = env.current.to_active_graph()
        self.assertEqual(len(active_graph.G.nodes()), 0)
        self.assertEqual(len(active_graph.G.edges()), 0)


if __name__ == "__main__":
    unittest.main()