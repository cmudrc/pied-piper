try: from .transaction import Transaction
except: from transaction import Transaction
try: from .exchange import Exchange
except: from exchange import Exchange


class Economy:

    def __init__(self, transactions, exchange: Exchange):
        if isinstance(transactions, list):
            self.transactions = transactions
        elif isinstance(transactions, Transaction):
            self.transactions = [transactions]
        self.exchange = exchange

    def solve(self):
        pass