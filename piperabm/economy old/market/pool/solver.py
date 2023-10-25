class Solver:
    """
    *** Extends Pool Class ***
    Contain methods for allocating resource bids
    """

    def __init__(self):
        self.stat = {
            'transactions': [],
            'total_volume': 0
        }

    def solve_step(self):
        """
        Solve a single step
        """
        biggest_source_bid = self.find_biggest_bid(self.source_bids)
        biggest_demand_bid = self.find_biggest_bid(self.demand_bids)
        if biggest_source_bid is not None and biggest_demand_bid is not None:
            diff = biggest_source_bid.amount - biggest_demand_bid.amount
            volume = min([biggest_source_bid.amount,
                         biggest_demand_bid.amount])
            if volume > 0:
                if diff >= 0:
                    biggest_source_bid.amount = diff
                    biggest_demand_bid.amount = 0
                else:
                    biggest_source_bid.amount = 0
                    biggest_demand_bid.amount = -diff
                from_agent_index = biggest_source_bid.agent
                to_agent_index = biggest_demand_bid.agent
        else:
            volume = 0
        
        if volume > 0:
            transaction = {
                'from': from_agent_index,
                'to': to_agent_index,
                'volume': volume,
            }
            self.stat['transactions'].append(transaction)
            self.stat['total_volume'] += volume
        else:
            transaction = None
        return transaction

    def solve(self):
        """
        Solve the pool until reaching stagnation
        """
        transaction = 'value'
        while transaction is not None:
            transaction = self.solve_step()
        return self.stat
    
    @property
    def steps(self):
        """
        Return number of steps taken to solve
        """
        return len(self.transactions)

    @property
    def transactions(self):
        """
        Return total transactions between agents
        """
        return self.stat['transactions']
    
    @property
    def transactions_volume(self):
        """
        Return total transactions value between agents
        """
        return self.stat['total_volume']
