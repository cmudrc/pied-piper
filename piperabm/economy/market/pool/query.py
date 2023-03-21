class Query:
    """
    Contains methods for Pool class
    """

    def _find_source_bid(self, agent):
        """
        Find the proposed source bid by *agent*
        """
        result = None
        for bid in self.source_bids:
            if bid.agent == agent:
                result = bid
                break
        return result

    def _find_demand_bid(self, agent):
        """
        Find the proposed demand bid by *agent*
        """
        result = None
        for bid in self.demand_bids:
            if bid.agent == agent:
                result = bid
                break
        return result

    def find_bid(self, agent):
        """
        Find the proposed bid by *agent*
        """
        result = None
        bid_type = None
        bid = self._find_source_bid(agent)
        if bid is not None:
            result = bid
            bid_type = "source"
        bid = self._find_demand_bid(agent)
        if bid is not None:
            result = bid
            bid_type = "demand"
        return result, bid_type

    def find_biggest_bid(self, bids):
        """
        Find the biggest bid between *bids*
        """
        result = None
        for bid in bids:
            #print(bid)
            if result is None:
                result = bid
            else:
                if bid.new_amount > result.new_amount:
                    result = bid
        return result