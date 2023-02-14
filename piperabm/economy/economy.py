from copy import deepcopy

from piperabm.resource import DeltaResource
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

    def all_agents(self):
        result = []
        for transaction in self.transactions:
            agent = transaction.agent
            if agent not in result:
                result.append(agent)
        return result

    def find_transaction(self, agent):
        result = None
        for transaction in self.transactions:
            if transaction.agent == agent:
                result = transaction
        return result

    def agents_demand(self, agents):
        if not isinstance(agents, list):
            agents = [agents]
        result = DeltaResource(
            {'food': 0, 'water': 0, 'energy': 0,}
        )
        for agent in agents:
            transaction = self.find_transaction(agent)
            demand = transaction.demand()
            result = result + demand
        return result

    def agents_source(self, agents):
        if not isinstance(agents, list):
            agents = [agents]
        result = DeltaResource(
            {'food': 0, 'water': 0, 'energy': 0,}
        )
        for agent in agents:
            transaction = self.find_transaction(agent)
            source = transaction.source()
            result = result + source
        return result

    def solve(self):
        def priority_score():
            """
            Calculate the score to sort agents based on priority
            """
            for agent in self.all_agents():
                others = deepcopy(self.all_agents())
                others.remove(agent)
                agent_demand = self.agents_demand(agent)
                agent_source = self.agents_source(agent)
                others_demand = self.agents_demand(others)
                others_source = self.agents_source(others)
                others_source - agent_demand
                agent_source - others_demand
                score = None
                transaction = self.find_transaction(agent)
                transaction.score = score

        def sort_transactions():
            """
            Sort transactions based on their scores
            """
            pass