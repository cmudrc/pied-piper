import unittest

from piperabm.infrastructure.items import Junction


class TestJunctionClass(unittest.TestCase):

    def setUp(self):
        self.junction = Junction(
            pos=[0, 0],
            name='Sample'
        )
        self.maxDiff = None

    def test_serialization(self):
        dictionary = self.junction.serialize()
        expected_result = {
            'pos': [0, 0],
            'name': 'Sample',
            'section': 'infrastructure',
            'category': 'node',
            'type': 'junction'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_junction = Junction()
        new_junction.deserialize(dictionary)
        self.assertEqual(self.junction, new_junction)


if __name__ == '__main__':
    unittest.main()