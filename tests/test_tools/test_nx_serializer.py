import unittest
import networkx as nx
import os

from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize
from piperabm.tools.json_file import JsonFile


class TestNXSerializers_Graph(unittest.TestCase):

    def setUp(self) -> None:
        self.G = nx.Graph()
        self.G.add_node(1, weight=1)
        self.G.add_node(2, weight=2)
        self.G.add_node(3, weight=3)
        self.G.add_edge(1, 2, weight=4)
        self.G.add_edge(2, 3, weight=5)
        self.G.add_edge(1, 3, weight=6)
  
    def test_conversion(self):
        data = nx_serialize(self.G)
        G_new = nx_deserialize(data)
        self.assertListEqual(list(self.G.nodes), list(G_new.nodes))
        self.assertListEqual(list(self.G.edges), list(G_new.edges))
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)

    def test_json(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = JsonFile(path=path, filename='G')
        data = nx_serialize(self.G)
        file.save(data)
        G_new = nx_deserialize(file.load())
        file.remove()
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)


class TestNXSerializers_DiGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.G = nx.DiGraph()
        self.G.add_node(1, weight=1)
        self.G.add_node(2, weight=2)
        self.G.add_node(3, weight=3)
        self.G.add_edge(1, 2, weight=4)
        self.G.add_edge(2, 1, weight=5)
        self.G.add_edge(1, 3, weight=6)

    def test_conversion(self):
        data = nx_serialize(self.G)
        G_new = nx_deserialize(data)
        self.assertListEqual(list(self.G.nodes), list(G_new.nodes))
        self.assertListEqual(list(self.G.edges), list(G_new.edges))
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)

    def test_json(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = JsonFile(path=path, filename='G')
        data = nx_serialize(self.G)
        file.save(data)
        G_new = nx_deserialize(file.load())
        file.remove()
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)


class TestNXSerializers_MultiGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.G = nx.MultiGraph()
        self.G.add_node(1, weight=1)
        self.G.add_node(2, weight=2)
        self.G.add_node(3, weight=3)
        self.G.add_edge(1, 2, weight=4)
        self.G.add_edge(1, 2, weight=5)
        self.G.add_edge(2, 1, weight=6)
    
    def test_conversion(self):
        data = nx_serialize(self.G)
        G_new = nx_deserialize(data)
        self.assertListEqual(list(self.G.nodes), list(G_new.nodes))
        self.assertListEqual(list(self.G.edges), list(G_new.edges))
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)

    def test_json(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = JsonFile(path=path, filename='G')
        data = nx_serialize(self.G)
        file.save(data)
        G_new = nx_deserialize(file.load())
        file.remove()
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)


class TestNXSerializers_MultiDiGraph(unittest.TestCase):

    def setUp(self) -> None:
        self.G = nx.MultiDiGraph()
        self.G.add_node(1, weight=1)
        self.G.add_node(2, weight=2)
        self.G.add_node(3, weight=3)
        self.G.add_edge(1, 2, weight=4)
        self.G.add_edge(1, 2, weight=5)
        self.G.add_edge(2, 1, weight=6)
    
    def test_conversion(self):
        data = nx_serialize(self.G)
        G_new = nx_deserialize(data)
        self.assertListEqual(list(self.G.nodes), list(G_new.nodes))
        self.assertListEqual(list(self.G.edges), list(G_new.edges))
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)

    def test_json(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = JsonFile(path=path, filename='G')
        data = nx_serialize(self.G)
        file.save(data)
        G_new = nx_deserialize(file.load())
        file.remove()
        data_new = nx_serialize(G_new)
        self.assertDictEqual(data, data_new)


if __name__ == "__main__":
    unittest.main()