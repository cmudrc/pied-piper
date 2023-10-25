import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.model.samples import model_0, model_3


class TestModelClass_0(unittest.TestCase):

    def setUp(self):
        self.model = deepcopy(model_0)

    def test_serialization(self):
        dictionary = self.model.serialize()
        #print(dictionary)
        environment_new = Model()
        environment_new.deserialize(dictionary)
        dictionary_new = environment_new.serialize()
        self.assertDictEqual(dictionary, dictionary_new)


class TestModelClass_3(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model_3)

    def test_find_nearest_node(self):
        items = self.model.all_environment_nodes
        pos = [0, 1]
        index, distance = self.model.find_nearest_node(pos, items)
        item = self.model.get(index)
        self.assertListEqual(item.pos, [0, 0])
        self.assertEqual(distance, 1)

    def test_run(self):
        self.model.run(100)
        self.assertEqual(len(self.model.all_alive_agents), 2)
        self.model.run(900)
        self.assertEqual(len(self.model.all_alive_agents), 0)



if __name__ == "__main__":
    unittest.main()