import unittest

from piperabm.infrastructure.items import Market


class TestMarketClass(unittest.TestCase):

    def setUp(self):
        self.market = Market(
            pos=[0, 0],
            name='Sample',
            index=0
        )
        self.maxDiff = None

    def test_serialization(self):
        dictionary = self.market.serialize()
        expected_result = {
            'pos': [0, 0],
            'name': 'Sample',
            'resources': {'food': {'name': 'food', 'max': 'inf', 'min': 0, 'amount': 0}, 'water': {'name': 'water', 'max': 'inf', 'min': 0, 'amount': 0}, 'energy': {'name': 'energy', 'max': 'inf', 'min': 0, 'amount': 0}},
            'degradation': {'current': 0, 'total': 'inf'},
            'index': 0,
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