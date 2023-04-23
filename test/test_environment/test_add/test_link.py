import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.elements.link.samples import link_0
from piperabm.environment.elements.hub.samples import hub_0, hub_1
from piperabm.tools.coordinate import slope, euclidean_distance, center


class TestAddClass_Link_0(unittest.TestCase):

    def setUp(self) -> None:
        environment = Environment()
        self.env = environment
        self.env.add_link_object(
            _from=[0, 0],
            _to=[1, 0],
            link=deepcopy(link_0)
        )
        #link = self.env.get_edge_element(0, 1)
        #print(link)

    def test_add_link_object(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 1)
        self.assertListEqual(list(edges), [(0, 1)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 2)
        self.assertListEqual(list(nodes), [0, 1])

    def test_create_boundary(self):
        start_pos = [1, 1]
        end_pos = [2, 2]
        boundary = self.env.create_boundary(
            length=euclidean_distance(start_pos, end_pos),
            width=1,
            slope=slope(start_pos, end_pos)
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
        

class TestAddClass_Link_1(unittest.TestCase):

    def setUp(self):
        environment = Environment()
        environment.append_node(element=deepcopy(hub_0))
        environment.append_node(element=deepcopy(hub_1))
        environment.add_edge(start_index=0, end_index=1, element=deepcopy(link_0))
        self.env = environment
        #print(environment)

    def test_add_edge(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 1)
        self.assertListEqual(list(edges), [(0, 1)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 2)
        self.assertListEqual(list(nodes), [0, 1])


class TestAddClass_Link_2(unittest.TestCase):

    def setUp(self):
        environment = Environment()
        environment.add_link(
            _from=[0, 0],
            _to=[1, 0],
            structure=link_0.structure
        )
        self.env = environment
        #print(environment)

    def test_add_edge(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 1)
        self.assertListEqual(list(edges), [(0, 1)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 2)
        self.assertListEqual(list(nodes), [0, 1])


class TestAddClass_Link_3(unittest.TestCase):

    def setUp(self):
        environment = Environment()
        environment.add_road(
            _from=[0, 0],
            _to=[1, 0]
        )
        self.env = environment
        #print(environment)

    def test_add_edge(self):
        edges = self.env.G.edges()
        self.assertEqual(len(edges), 1)
        self.assertListEqual(list(edges), [(0, 1)])
        nodes = self.env.G.nodes()
        self.assertEqual(len(nodes), 2)
        self.assertListEqual(list(nodes), [0, 1])


if __name__ == "__main__":
    unittest.main()