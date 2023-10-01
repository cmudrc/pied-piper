import unittest
from copy import deepcopy

from piperabm.environment.samples import environment_0, environment_1


class TestEnvironmentClass_0(unittest.TestCase):

    def setUp(self):
        self.env = deepcopy(environment_0)

    def test_all_nodes(self):
        self.assertEqual(len(self.env.all_nodes()), 2)
        self.assertEqual(len(self.env.all_nodes(type='junction')), 1)
        self.assertEqual(len(self.env.all_nodes(type='settlement')), 1)
    
    def test_all_edges(self):
        self.assertEqual(len(self.env.all_edges()), 1)


class TestEnvironmentClass_1(unittest.TestCase):       

    def setUp(self):
        self.env = deepcopy(environment_1)

    def test_all_nodes(self):
        result = self.env.all_nodes()
        self.assertEqual(len(result), 5)

    def test_all_edges(self):
        result = self.env.all_edges()
        self.assertEqual(len(result), 4)


if __name__ == '__main__':
    unittest.main()