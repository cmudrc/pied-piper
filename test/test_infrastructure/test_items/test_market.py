import unittest

from piperabm.infrastructure.items import Market


class TestMarketClass(unittest.TestCase):

    def setUp(self):
        self.market = Market(
            pos=[0, 0],
            name='Sample'
        )
        self.maxDiff = None

    def test_serialization(self):
        dictionary = self.market.serialize()
        expected_result = {
            'pos': [0, 0],
            'name': 'Sample',
            'degradation': {'current': 0, 'total': 'inf'},
            'section': 'infrastructure',
            'category': 'node',
            'type': 'market'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_market = Market()
        new_market.deserialize(dictionary)
        self.assertEqual(self.market, new_market)


if __name__ == '__main__':
    unittest.main()