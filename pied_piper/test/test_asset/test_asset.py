import unittest

from asset import Asset
from asset import Resource
from asset import Produce, Use, Deficiency, Storage


class TestAssetClass(unittest.TestCase):

    food = Resource(
        name='food',
        use=Use(rate=5),
        produce=Produce(rate=1),
        storage=Storage(current_amount=10, max_amount=20),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )
    water = Resource(
        name='water',
        use=Use(rate=0.1),
        storage=Storage(current_amount=10, max_amount=10),
        deficiency=Deficiency(current_amount=0, max_amount=20)
    )
    a = Asset()
    a.add(food, water)

    def test_(self):
        pass