class Solver:

    def solve_step(self):
        biggest_source_bid = self.find_biggest_bid(self.source_bids)
        biggest_demand_bid = self.find_biggest_bid(self.demand_bids)
        if biggest_source_bid is not None and biggest_demand_bid is not None:
            diff = biggest_source_bid.new_amount - biggest_demand_bid.new_amount
            volume = min([biggest_source_bid.new_amount, biggest_demand_bid.new_amount])
            if volume > 0:
                if diff >= 0:
                    biggest_source_bid.new_amount = diff
                    biggest_demand_bid.new_amount = 0
                else:
                    biggest_source_bid.new_amount = 0
                    biggest_demand_bid.new_amount = -diff
                ## log
                msg = self.log.message__transaction(
                    from_agent_index=biggest_source_bid.agent,
                    to_agent_index=biggest_demand_bid.agent,
                    amount=volume
                )
                #print(msg)
        else:
            volume = 0
        return volume

    def solve(self):
        #self.log.message__pool_started()
        volume = None
        while volume is None or volume != 0:
            volume = self.solve_step()
            self.total_volume += volume
        #self.log.message__pool_complete()
        stat = {
            'total_volume': self.total_volume,
        }
        return stat