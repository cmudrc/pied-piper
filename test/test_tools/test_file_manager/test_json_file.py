import unittest
from copy import deepcopy
import os

from piperabm.tools.file_manager import JsonFile
from piperabm.model.samples import model_0 as model


class TestJsonFileClass_Delta(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)
        self.model.path = os.path.dirname(os.path.realpath(__file__))

    def test_delta(self):
        model = deepcopy(self.model)
        # Delta 0
        model.old = model.serialize() #######
        object = model.get(0)
        object.pos = [1, 0]
        model.append_delta()
        # Delta 1
        model.old = model.serialize() ########
        object = model.get(0)
        object.pos = [1, 2]
        model.append_delta()
        # Apply deltas
        model_old = deepcopy(self.model)
        model_old.apply_deltas()
        object = model_old.get(0)
        self.assertListEqual(object.pos, [1, 2])

        deltas_file = JsonFile(path=self.model.path, filename='sample_deltas')
        deltas_file.remove()


if __name__ == '__main__':
    unittest.main()