def trade(demands, sources):
    # Calculate excess items for each player
    excess = [sources[i] - demands[i] for i in range(len(demands))]

    # Initialize trade matrix
    trade_matrix = [[0 for _ in range(len(demands))] for _ in range(len(demands))]

    for i in range(len(demands)):
        for j in range(len(demands)):
            if i != j:
                # Determine the trade amount (minimum of excess and demand)
                trade_amount = min(excess[i], demands[j] - sum(trade_matrix[j]))
                trade_matrix[i][j] = trade_amount
                excess[i] -= trade_amount

    return trade_matrix

# Define demands and sources
demands = [3, 4, 5]
sources = [6, 5, 3]

# Perform the trade
trades = trade(demands, sources)

# Display the result
print("Trade Matrix (rows are givers, columns are receivers):")
for row in trades:
    print(row)