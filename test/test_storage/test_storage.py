import unittest
from copy import deepcopy

from piperabm.storage import Storage
from piperabm.storage.samples import storage_0


class TestStorageClass(unittest.TestCase):

    def setUp(self) -> None:
        self.storage = storage_0

    def test_mul_0(self):
        storage = deepcopy(self.storage)
        remainder = storage * 2
        expected_storage = {
            'energy': {'amount': 25, 'max': 25, 'min': 0},
            'food': {'amount': 10, 'max': 10, 'min': 0},
            'water': {'amount': 16, 'max': 20, 'min': 0},
        }
        self.assertDictEqual(storage.to_dict(), expected_storage)
        expected_remainder = {'food': 2, 'water': 0, 'energy': 13}
        self.assertDictEqual(remainder, expected_remainder)

    def test_mul_0(self):
        storage = deepcopy(self.storage)
        remainder = storage / 0.5
        expected_storage = {
            'energy': {'amount': 25, 'max': 25, 'min': 0},
            'food': {'amount': 10, 'max': 10, 'min': 0},
            'water': {'amount': 16, 'max': 20, 'min': 0},
        }
        self.assertDictEqual(storage.to_dict(), expected_storage)
        expected_remainder = {'food': 2, 'water': 0, 'energy': 13}
        self.assertDictEqual(remainder, expected_remainder)

    def test_dict(self):
        dictionary = self.storage.to_dict()
        expected_result = {
            'energy': {'amount': 19, 'max': 25, 'min': 0},
            'food': {'amount': 6, 'max': 10, 'min': 0},
            'water': {'amount': 8, 'max': 20, 'min': 0},
        }
        self.assertDictEqual(dictionary, expected_result)
        storage = Storage()
        storage.from_dict(dictionary)
        self.assertEqual(storage, self.storage)

    def test_delta(self):
        storage_previous = deepcopy(self.storage)
        storage = deepcopy(storage_previous)
        storage('food') + 3
        delta = storage - storage_previous
        expected_result = {'food': {'amount': 3}}
        self.assertDictEqual(delta, expected_result)
        storage_previous + delta
        self.assertEqual(storage, storage_previous)


if __name__ == "__main__":
    unittest.main()