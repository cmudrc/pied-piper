import unittest

from piperabm.infrastructure.items import Road


class TestRoadClass(unittest.TestCase):

    def setUp(self):
        self.road = Road(
            pos_1=[0, 0],
            pos_2=[3, 4],
            name='Sample',
            index=0
        )
        self.maxDiff = None

    def test_serialization(self):
        dictionary = self.road.serialize()
        expected_result = {
            'pos_1': [0, 0],
            'pos_2': [3, 4],
            'name': 'Sample',
            'length_actual': None,
            'roughness': 1,
            'degradation': {'current': 0, 'total': 'inf'},
            'index': 0,
            'section': 'infrastructure',
            'category': 'edge',
            'type': 'road'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_market = Road()
        new_market.deserialize(dictionary)
        self.assertEqual(self.road, new_market)

    def test_length(self):
        length = self.road.length
        self.assertEqual(length, 5)


if __name__ == '__main__':
    unittest.main()