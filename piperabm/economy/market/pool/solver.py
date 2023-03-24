class Solver:
    """
    Contains methods for Pool class
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
            diff = biggest_source_bid.new_amount - biggest_demand_bid.new_amount
            volume = min([biggest_source_bid.new_amount,
                         biggest_demand_bid.new_amount])
            if volume > 0:
                if diff >= 0:
                    biggest_source_bid.new_amount = diff
                    biggest_demand_bid.new_amount = 0
                else:
                    biggest_source_bid.new_amount = 0
                    biggest_demand_bid.new_amount = -diff

                from_agent_index = biggest_source_bid.agent
                to_agent_index = biggest_demand_bid.agent
                ''' log '''
                msg = self.log.message__transaction(
                    from_agent_index,
                    to_agent_index,
                    amount=volume
                )
                #print(msg)
        else:
            volume = 0
        
        transaction = {}
        transaction['volume'] = volume
        if volume > 0:
            transaction['from_agent_index'] = from_agent_index
            transaction['to_agent_index'] = to_agent_index
            self.stat['transactions'].append(transaction)
            self.stat['total_volume'] += volume
        return transaction

    def solve(self):
        ''' log '''
        #msg = self.log.message__pool_started()
        #print(msg)
        
        def check_stagnation(transaction):
            result = True
            volume = transaction['volume']
            if volume > 0 or transaction is None:
                result = False
            return result

        transaction = None
        while transaction is None or check_stagnation(transaction) is False:
            transaction = self.solve_step()

        ''' log '''
        #msg = self.log.message__pool_complete()
        #print(msg)
        return self.stat
