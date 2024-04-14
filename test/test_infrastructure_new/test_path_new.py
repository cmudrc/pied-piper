import unittest

from piperabm.infrastructure_new.samples import infrastructure_1 as infrastructure
from piperabm.infrastructure_new.paths.paths_new import Paths


class TestPathClass(unittest.TestCase):

    def setUp(self):
        self.paths = Paths(infrastructure)
        self.paths.update()
        
    def test_estiamted_distance(self):
        d_12 = self.paths.estimated_distance(1, 2)
        d_21 = self.paths.estimated_distance(2, 1)
        self.assertEqual(d_12, d_21)
        self.assertAlmostEqual(d_12, 79.05, places=1)

    def test_path(self):
        path = self.paths.path(id_start=1, id_end=2)
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0], 1)
        self.assertEqual(path[-1], 2)

    def test_destinations(self):
        destinations = self.paths.destinations(id_start=1, type='all')
        self.assertListEqual(destinations, [2])
        destinations = self.paths.destinations(id_start=1, type='market')
        self.assertListEqual(destinations, [])
        destinations = self.paths.destinations(id_start=1, type='home')
        self.assertListEqual(destinations, [2])


if __name__ == "__main__":
    unittest.main()