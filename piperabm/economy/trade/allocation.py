from piperabm.economy.trade.trade_solver import MultiResourceTrade


def find_exchanges(players_initial, players_final):
    resources = ['food', 'water', 'energy']
    num = len(players_initial)
    sources = {}
    demands = {}
    for i in range(num):
        player_initial = players_initial[i]
        player_final = players_final[i]
        for resource in resources:
            player_initial_resource = player_initial['resources'][resource]
            player_final_resource = player_final['resources'][resource]
            diff = player_final_resource - player_initial_resource
            if resource not in sources:
                sources[resource] = []
            if resource not in demands:
                demands[resource] = []
            if diff < 0:
                sources[resource].append(-diff)
                demands[resource].append(0)
            else:
                sources[resource].append(0)
                demands[resource].append(diff)
    #print(sources)
    #print(demands)
    result = {}
    for resource in resources:
        resource_sources = sources[resource]
        resource_demands = demands[resource]
        transactions = resource_exchange(resource_sources, resource_demands)
        #result[resource] = transactions
        result[resource] = index_to_id(transactions, players_final)
    return result

def index_to_id(transactions, players):
    result = []
    #print(transactions[resource])
    for transaction in transactions:
        result.append(
            [
                players[transaction[0]]['id'], # from
                players[transaction[1]]['id'], # to
                transaction[2], # amount
            ]
        )
    return result

def resource_exchange(sources, demands):
    # Create a list of indices for sources and demands to keep track of the original positions
    source_indices = list(range(len(sources)))
    demand_indices = list(range(len(demands)))
    
    # We'll keep a log of transactions to see who gave to whom and how much
    transactions = []
    
    # Continue until we have no more sources or demands to fulfill
    while any(sources) and any(demands):
        # Get the index of the largest source and largest demand
        max_source_index = max(range(len(sources)), key=lambda x: sources[x])
        max_demand_index = max(range(len(demands)), key=lambda x: demands[x])
        
        # Find the maximum amount that can be transferred
        amount = min(sources[max_source_index], demands[max_demand_index])
        
        # Record the transaction
        transactions.append((source_indices[max_source_index], demand_indices[max_demand_index], amount))
        
        # Update the source and demand values
        sources[max_source_index] -= amount
        demands[max_demand_index] -= amount
        
        # If a source or demand is depleted, set it to 0 to avoid negative numbers
        if sources[max_source_index] < 1e-9:
            sources[max_source_index] = 0
        if demands[max_demand_index] < 1e-9:
            demands[max_demand_index] = 0
            
    return transactions


if __name__ == "__main__":

    from copy import deepcopy

    prices = {
        'food': 10,
        'water': 10,
        'energy': 10
    }
    player_1 = {
        'id': 1,
        'type': 'agent',
        'resources': {
            'food': 9,
            'water': 2,
            'energy': 3
        },
        'enough_resources': {
            'food': 10,
            'water': 10,
            'energy': 10
        },
        'balance': 100,
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
            'food': 3,
            'water': 10,
            'energy': 7
        },
        'enough_resources': {
            'food': 10,
            'water': 10,
            'energy': 10
        },
        'balance': 10,
    }
    players = [player_1, player_2, player_3]

    players_initial = deepcopy(players)

    print("Solves multi-resources for multiple players at fixed price.")

    # Initial
    print("\n" + ">>> " + "Initial: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])

    # Solve
    players = MultiResourceTrade.solve(players=players, prices=prices)

    # Final
    print("\n" + ">>> " + "Final: ")
    for player in players:
        print(player['resources'], ', balance:', player['balance'])

    # Echanges
    print("\n" + ">>> " + "Exchanges: ")
    exchanges = find_exchanges(players_initial=players_initial, players_final=players)
    print(exchanges)