import unittest
from copy import deepcopy

from piperabm.model import Model
from piperabm.model.samples import model_0


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.model = deepcopy(model_0)

    def test_serialization(self):
        dictionary = self.model.serialize()
        #print(dictionary)
        environment_new = Model()
        environment_new.deserialize(dictionary)
        dictionary_new = environment_new.serialize()
        self.assertDictEqual(dictionary, dictionary_new)


if __name__ == "__main__":
    unittest.main()