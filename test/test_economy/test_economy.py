import unittest
from copy import deepcopy

from piperabm.economy import Player, Economy, Exchange


class TestEconomyClass1(unittest.TestCase):

    p1 = Player(
        1,
        source={
            'food': 4,
        },
        demand={
            'food': 6,
        },
        wallet=10
    )
    p2 = Player(
        2,
        source={
            'food': 2,
        },
        demand={
            'food': 8,
        },
        wallet=20
        )

    exchange = Exchange()
    exchange.add('food', 'wealth', 5)

    econ = Economy(exchange)
    econ.add([p1, p2])

    def test_solve(self):
        econ = deepcopy(self.econ)
        econ.solve()
        #print(econ)


class TestEconomyClass(unittest.TestCase):

    p1 = Player(
        1,
        source={
            'food': 4,
            'water': 5,
        },
        demand={
            'food': 6,
            'water': 5,
        },
        wallet=10
    )
    p2 = Player(
        2,
        source={
            'food': 2,
            'water': 5,
        },
        demand={
            'food': 8,
            'water': 5,
        },
        wallet=20
        )
    p3 = Player(
        3,
        source={
            'food': 5,
            'water': 5,
        },
        demand={
            'food': 5,
            'water': 5,
        },
        wallet=20
        )

    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)

    econ = Economy(exchange)
    econ.add([p1, p2, p3])

    def test_solve(self):
        econ = deepcopy(self.econ)
        econ.solve()
        #print(econ)



if __name__ == "__main__":
    unittest.main()