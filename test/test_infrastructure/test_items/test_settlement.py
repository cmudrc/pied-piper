import unittest

from piperabm.infrastructure.items import Settlement


class TestSettlementClass(unittest.TestCase):

    def setUp(self):
        self.settlement = Settlement(
            pos=[0, 0],
            name='Sample',
            index=0
        )
        self.maxDiff = None

    def test_serialization(self):
        dictionary = self.settlement.serialize()
        expected_result = {
            'pos': [0, 0],
            'name': 'Sample',
            'degradation': {'current': 0, 'total': 'inf'},
            'index': 0,
            'section': 'infrastructure',
            'category': 'node',
            'type': 'settlement'
        }
        self.assertDictEqual(dictionary, expected_result)
        new_settlement = Settlement()
        new_settlement.deserialize(dictionary)
        self.assertEqual(self.settlement, new_settlement)


if __name__ == '__main__':
    unittest.main()