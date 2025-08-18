import unittest
from copy import deepcopy

from piperabm.infrastructure.samples.infrastructure_3 import model


class TestSerializeClass(unittest.TestCase):

    def setUp(self) -> None:
        self.model = deepcopy(model)

    def test_serialize(self):
        m1 = deepcopy(self.model)
        m2 = deepcopy(self.model)
        data = m1.serialize()
        m2.deserialize(data)
        self.assertDictEqual(m1.serialize(), m2.serialize())
        self.assertEqual(len(m1.infrastructure.streets), len(m2.infrastructure.streets))


if __name__ == "__main__":
    unittest.main()
