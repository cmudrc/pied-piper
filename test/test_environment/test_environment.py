import unittest
from copy import deepcopy

from piperabm.environment import Environment
from piperabm.environment.samples import environment_0


class TestInfrastructureClass(unittest.TestCase):

    def setUp(self):
        self.environment = deepcopy(environment_0)

    def test_serialization(self):
        dictionary = self.environment.serialize()
        #print(dictionary)
        environment_new = Environment()
        environment_new.deserialize(dictionary)
        dictionary_new = environment_new.serialize()
        self.assertDictEqual(dictionary, dictionary_new)


if __name__ == '__main__':
    unittest.main()