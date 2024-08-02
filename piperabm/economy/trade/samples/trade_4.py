from piperabm.economy.trade.trade_solver import MultiResourceTrade as mrt


prices = {
    'food': 10,
    'water': 10,
    'energy': 10
}
player_1 = {
    'id': 1,
    'type': 'market',
    'resources': {
        'food': 100,
        'water': 100,
        'energy': 100
    },
    'enough_resources': {
        'food': 100,
        'water': 100,
        'energy': 100
    },
    'balance': 0,
}
player_2 = {
    'id': 2,
    'type': 'agent',
    'resources': {
        'food': 10,
        'water': 3,
        'energy': 10
    },
    'enough_resources': {
        'food': 10,
        'water': 10,
        'energy': 10
    },
    'balance': 100,
}
player_3 = {
    'id': 3,
    'type': 'agent',
    'resources': {
        'food': 1,
        'water': 2,
        'energy': 3
    },
    'enough_resources': {
        'food': 10,
        'water': 10,
        'energy': 10
    },
    'balance': 10,
}
players = [player_1, player_2, player_3]

players = mrt.solve(players=players, prices=prices)


if __name__ == "__main__":
    for player in players:
        print(f"resources: {player['resources']}, balance: {player['balance']}")
