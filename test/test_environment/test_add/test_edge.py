import unittest
from copy import deepcopy

from piperabm.environment_old import Environment
from piperabm.infrastructure.road.samples import road_0
from piperabm.infrastructure.settlement.samples import settlement_0, settlement_1
from piperabm.boundary.rectangular import Rectangular
from piperabm.tools.coordinate import slope, euclidean_distance, center


class TestEnvironmentAddLink(unittest.TestCase):

    def setUp(self) -> None:
        self.env = Environment()

    def test_add_edge(self):
        self.env.add_edge_object(
            _from=[0, 0],
            _to=[1, 0],
            structure=deepcopy(road_0)
        )
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 1)
        self.assertListEqual(list(edges), [(0, 1)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 2)
        self.assertListEqual(list(nodes), [0, 1])

    def test_create_boundary(self):
        width = 1
        boundary = Rectangular(height=width)
        start_pos = [1, 1]
        end_pos = [2, 2]
        boundary = self.env.modify_boundary(
            length=euclidean_distance(start_pos, end_pos),
            slope=slope(start_pos, end_pos),
            boundary=boundary
        )
        dictionary = boundary.to_dict()
        expected_result = {
            'shape': {
                'type': 'rectangle',
                'width': 1.4142135623730951,
                'height': 1,
                'angle': 0.7853981633974484
            }
        }
        self.assertDictEqual(dictionary, expected_result)


if __name__ == "__main__":
    unittest.main()