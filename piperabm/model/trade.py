from copy import deepcopy

from piperabm.economy.trade import MultiResourceTrade
from piperabm.economy.trade.allocation import find_exchanges


class Trade:
    """
    Manage trade between players when updating
    """

    def trade(self, agents: list = [], markets: list = []):
        """
        Trade
        """
        names = self.resource_names
        players = []

        # Load agent players into solver
        for agent in agents:
            resources = {}
            enough_resources = {}
            for name in names:
                resources[name] = self.society.get_resource(id=agent, name=name)
                enough_resources[name] = self.society.get_enough_resource(id=agent, name=name)
            player = {
                'id': agent,
                'type': 'agent',
                'resources': resources,
                'enough_resources': enough_resources,
                'balance': self.society.get_balance(id=agent),
            }
            players.append(player)

        # Load market players into solver
        for market in markets:
            resources = {}
            enough_resources = {}
            for name in names:
                resources[name] = self.infrastructure.get_resource(id=market, name=name)
                enough_resources[name] = self.infrastructure.get_enough_resource(id=market, name=name)
            player = {
                'id': market,
                'type': 'market',
                'resources': resources,
                'enough_resources': enough_resources,
                'balance': self.infrastructure.get_balance(id=market)
            }
            players.append(player)

        # Solve
        players_initial = deepcopy(players)
        players = MultiResourceTrade.solve(players=players, prices=self.prices)
        transactions = find_exchanges(players_initial=players_initial, players_final=players)

        # Update values
        for player in players:
            # Update agent players
            if player['type'] == 'agent':
                for name in names:
                    self.society.set_resource(
                        id=player['id'],
                        name=name,
                        value=player['resources'][name]
                    )
                self.society.set_balance(
                    id=player['id'],
                    value=player['balance']
                )
            # Update market players
            elif player['type'] == 'market':
                for name in names:
                    self.infrastructure.set_resource(
                        id=player['id'],
                        name=name,
                        value=player['resources'][name]
                    )
                self.infrastructure.set_balance(
                    id=player['id'],
                    value=player['balance']
                )
        #print(transactions)
        return flatten_transactions(transactions)
    

def flatten_transactions(transactions):
    results = []
    for resource_name in transactions:
        for transaction in transactions[resource_name]:
            result = [
                transaction[0], # from
                transaction[1], # to
                transaction[2], # amount
                resource_name, # resource name
            ]
            results.append(result)
    #print(results)
    return results
    

if __name__ == "__main__":
    
    from piperabm.society.samples.society_0 import model

    model.society.average_income = 0
    agents = model.society.agents

    wealth_0 = model.society.wealth(agents[0])
    wealth_1 = model.society.wealth(agents[1])
    if wealth_0 < wealth_1:
        id_low = agents[0]  # Agent with lower wealth
        id_high = agents[1]  # Agent with higher wealth
    food = model.society.get_resource(id_low, 'food')
    model.society.set_resource(id_low, 'food', value=food/10)
    water = model.society.get_resource(id_low, 'water')
    model.society.set_resource(id_low, 'water', value=water/5)

    print("\n" + ">>> Initial:")
    for agent in agents:
        balance = model.society.get_balance(agent)
        food = model.society.get_resource(agent, 'food')
        water = model.society.get_resource(agent, 'water')
        energy = model.society.get_resource(agent, 'energy')
        print(f"id: {agent}, balance: {balance}, food: {food}, water: {water}, energy: {energy}")

    transactions = model.update(duration=1)

    print("\n" + ">>> " + "Exchanges: ")
    for transaction in transactions:
        print(f"from: {transaction[0]}, to: {transaction[1]}, amount: {transaction[2]}, resource: {transaction[3]}")

    print("\n" + ">>> Final:")
    for agent in agents:
        balance = model.society.get_balance(agent)
        food = model.society.get_resource(agent, 'food')
        water = model.society.get_resource(agent, 'water')
        energy = model.society.get_resource(agent, 'energy')
        print(f"id: {agent}, balance: {balance}, food: {food}, water: {water}, energy: {energy}")