class Query:
    """
    *** Extends Pool Class ***
    Contain methods for query bids
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
        if bids is not None and len(bids) > 0:
            for bid in bids:
                #print(bid)
                if result is None:
                    result = bid
                else:
                    if bid.amount > result.amount:
                        result = bid
        return result
    
    def all_participants(self):
        """
        Return all participants in the pool
        """
        sellers = []
        buyers = []
        for bid in self.source_bids:
            sellers.append(bid.agent)
        for bid in self.demand_bids:
            buyers.append(bid.agent)
        return sellers, buyers

    def add_source(self, bids):
        """
        Add new bids to the source bids
        """
        if not isinstance(bids, list):
            bids = [bids]
        for bid in bids:
            self.source_bids.append(bid)

    def add_demand(self, bid):
        """
        Add new bids to the demand bids
        """
        if isinstance(bid, list):
            for item in bid:
                self.demand_bids.append(item)
        else:
            self.demand_bids.append(bid)

    def size(self):
        """
        Calculate total source and totam demand values within the pool
        """
        size_source = 0
        for bid in self.source_bids:
            size_source += bid.amount
        size_demand = 0
        for bid in self.demand_bids:
            size_demand += bid.amount
        return size_source, size_demand