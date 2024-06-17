import unittest
import networkx as nx
import os

from piperabm.tools.nx_serializer import nx_serialize, nx_deserialize
from piperabm.tools.json_file import JsonFile


class TestNXSerializers(unittest.TestCase):

    def setUp(self) -> None:
        self.G = nx.DiGraph()
        self.G.add_node(1, weight=1)
        self.G.add_node(2, weight=2)
        self.G.add_node(3, weight=3)
        self.G.add_edge(1, 2, weight=4)
        self.G.add_edge(2, 1, weight=5)
        self.G.add_edge(1, 3, weight=6)

    def test_conversion(self):
        G_serialized = nx_serialize(self.G)
        G_new = nx_deserialize(G_serialized)
        G_new_serialized = nx_serialize(G_new)
        self.assertDictEqual(G_serialized, G_new_serialized)

    def test_json(self):
        path = os.path.dirname(os.path.realpath(__file__))
        file = JsonFile(path=path, filename='G')
        G_serialized = nx_serialize(self.G)
        file.save(G_serialized)
        G_new = nx_deserialize(file.load())
        file.remove()
        G_new_serialized = nx_serialize(G_new)
        self.assertDictEqual(G_serialized, G_new_serialized)


if __name__ == "__main__":
    unittest.main()