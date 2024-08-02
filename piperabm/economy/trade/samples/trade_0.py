from piperabm.economy.trade.nash_bargaining import NashBargaining as nb


price = 10
player_1 = {
    'id': 1,
    'type': 'agent',
    'resource': 2,
    'enough_resource': 10,
    'balance': 100,
}
player_2 = {
    'id': 2,
    'type': 'agent',
    'resource': 8,
    'enough_resource': 10,
    'balance': 100,
}
players = [player_1, player_2]

transactions = nb.transactions(players, price)
players = nb.apply(players, transactions)


if __name__ == "__main__":
    #print(transactions)
    for player in players:
        print(f"resource: {player['resource']}, balance: {player['balance']}")
