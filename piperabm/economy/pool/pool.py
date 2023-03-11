try: from .bid import Bid
except: from bid import Bid
try: from .query import Query
except: from query import Query
try: from .solver import Solver
except: from solver import Solver
try: from .log import Log
except: from log import Log


class Pool(Solver, Query):
    """
    Solve pool as a single-resource allocation problem
    """

    def __init__(self):
        self.source_bids = []
        self.demand_bids = []
        self.total_volume = 0
        self.log = Log(prefix="POOL", indentation_depth=3)
        super().__init__()

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
            size_source += bid.new_amount
        size_demand = 0
        for bid in self.demand_bids:
            size_demand += bid.new_amount
        return size_source, size_demand

    def __str__(self):
        txt_source = '## sources: \n'
        if len(self.source_bids) > 0:
            for bid in self.source_bids:
                txt_source += bid.__str__() + '\n'
        txt_demand = '## demands: \n'
        if len(self.demand_bids) > 0:
            for bid in self.demand_bids:
                txt_demand += bid.__str__() + '\n'
        return txt_source + '\n' + txt_demand
    
    def __eq__(self, other):
        result = True
        for bid_s in self.source_bids:
            for bid_o in other.source_bids:
                if not bid_s == bid_o:
                    result = False
        for bid_s in self.demand_bids:
            for bid_o in other.demand_bids:
                if not bid_s == bid_o:
                    result = False
        return result


if __name__ == "__main__":
    b1 = Bid(1, 5)
    b2 = Bid(2, 8)
    b3 = Bid(3, 2)
    b4 = Bid(4, 1)

    p = Pool()
    p.add_source([b2, b4])
    p.add_demand([b1, b3])
    print("_________ initial __________")
    print(p)
    p.solve()
    print("__________ final ___________")
    print(p)
    