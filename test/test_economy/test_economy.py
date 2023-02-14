import unittest
from copy import deepcopy

from piperabm.resource import Resource, DeltaResource
from piperabm.economy import Exchange, Transaction, Economy


class TestEconomyClass(unittest.TestCase):

    t0 = Transaction(
        agent=0,
        wallet=100,
        resource=Resource(
            current_resource={
                'food': 2,
                'water': 5,
            },
            max_resource={
                'food': 10,
                'water': 10,
            }
        )
    )
    t1 = Transaction(
        agent=1,
        wallet=200,
        resource=Resource(
            current_resource={
                'food': 18,
                'water': 10,
            },
            max_resource={
                'food': 20,
                'water': 20,
            }
        )
    )
    transactions = [t0, t1]
    exchange = Exchange()
    exchange.add('food', 'wealth', 10)
    exchange.add('water', 'wealth', 2)
    exchange.add('energy', 'wealth', 5)
    eco = Economy(transactions, exchange)

    def test_economy(self):
        eco = deepcopy(self.eco)
        eco.solve()


if __name__ == "__main__":
    unittest.main()