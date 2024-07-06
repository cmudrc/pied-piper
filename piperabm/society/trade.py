from piperabm.economy.trade import solver


class Trade:

    def trade(self, agents: list = [], markets: list = []):
        """
        Trade
        """
        names = ['food', 'water', 'energy']
        players = []

        # Load agent players into solver
        for agent in agents:
            resources = {}
            enough_resources = {}
            for name in names:
                resources[name] = self.get_resource(id=agent, name=name)
                enough_resources[name] = self.get_enough_resource(id=agent, name=name)
            player = {
                'id': agent,
                'type': 'agent',
                'resources': resources,
                'enough_resources': enough_resources,
                'balance': self.get_balance(id=agent),
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

        prices = {
            'food': self.food_price,
            'water': self.water_price,
            'energy': self.energy_price
        }

        # Solve
        players = solver(players=players, prices=prices)

        # Update values
        for player in players:
            # Update agent players
            if player['type'] == 'agent':
                for name in names:
                    self.set_resource(
                        id=player['id'],
                        name=name,
                        value=player['resources'][name]
                    )
                self.set_balance(
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


if __name__ == "__main__":
    
    from piperabm.society.samples.society_0 import model


    model.society.average_income = 0
    agents = model.society.agents

    wealth_0 = model.society.wealth(agents[0])
    wealth_1 = model.society.wealth(agents[1])
    if wealth_0 < wealth_1:
        id_low = agents[0] # Agent with lower food
        id_high = agents[1]  # Agent with higher food
    food = model.society.get_resource(id_low, 'food')
    model.society.set_resource(id_low, 'food', value=food/10)

    print(">>> Initial:")
    for agent in agents:
        balance = model.society.get_balance(agent)
        food = model.society.get_resource(agent, 'food')
        water = model.society.get_resource(agent, 'water')
        energy = model.society.get_resource(agent, 'energy')
        print(f"{agent} balance: {balance}, food: {food}, water: {water}, energy: {energy}")

    model.update(duration=1)

    print(">>> Final:")
    for agent in agents:
        balance = model.society.get_balance(agent)
        food = model.society.get_resource(agent, 'food')
        water = model.society.get_resource(agent, 'water')
        energy = model.society.get_resource(agent, 'energy')
        print(f"{agent} balance: {balance}, food: {food}, water: {water}, energy: {energy}")

