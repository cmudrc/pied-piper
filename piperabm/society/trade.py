from piperabm.economy.trade import solver


class Trade:

    def trade(self, agents: list, market: int = None):
        # Load data to solver
        info = []
        if market is not None:
            market_info = {
                'id': market,
                'resources': {
                    'food': self.infrastructure.get_resource(id=market, name='food'),
                    'water': self.infrastructure.get_resource(id=market, name='water'),
                    'energy': self.infrastructure.get_resource(id=market, name='energy'),
                },
                'enough_resources': {
                    'food': self.infrastructure.get_enough_resource(id=market, name='food'),
                    'water': self.infrastructure.get_enough_resource(id=market, name='water'),
                    'energy': self.infrastructure.get_enough_resource(id=market, name='energy'),
                },
                'balance': self.infrastructure.get_balance(id=market)
            }
            info.append(market_info)
        for agent_id in agents:
            agent_info = {
                'id': agent_id,
                'resources': {
                    'food': self.get_resource(id=agent_id, name='food'),
                    'water': self.get_resource(id=agent_id, name='water'),
                    'energy': self.get_resource(id=agent_id, name='energy'),
                },
                'enough_resources': {
                    'food': self.get_enough_resource(id=agent_id, name='food'),
                    'water': self.get_enough_resource(id=agent_id, name='water'),
                    'energy': self.get_enough_resource(id=agent_id, name='energy'),
                },
                'balance': self.get_balance(id=agent_id),
            }
            info.append(agent_info)
        prices = {
            'food': self.food_price,
            'water': self.water_price,
            'energy': self.energy_price
        }

        # Solve
        result = solver(players=info, prices=prices)

        # Apply results to the model
        for i, info in enumerate(result):
            id = info['id']
            if market is not None and i == 0:
                self.infrastructure.set_resource(
                    id=id,
                    name='food',
                    value=info['resources']['food']
                )
                self.infrastructure.set_resource(
                    id=id,
                    name='water',
                    value=info['resources']['water']
                )
                self.infrastructure.set_resource(
                    id=id,
                    name='energy',
                    value=info['resources']['energy']
                )
                self.infrastructure.set_balance(
                    id=id,
                    value=info['balance']
                )
            else:
                self.set_resource(
                    id=id,
                    name='food',
                    value=info['resources']['food']
                )
                self.set_resource(
                    id=id,
                    name='water',
                    value=info['resources']['water']
                )
                self.set_resource(
                    id=id,
                    name='energy',
                    value=info['resources']['energy']
                )
                self.set_balance(
                    id=id,
                    value=info['balance']
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

