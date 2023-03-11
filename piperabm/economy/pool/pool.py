try: from .bid import Bid
except: from bid import Bid
try: from .solver import Solver
except: from solver import Solver
try: from .log import Log
except: from log import Log


class Pool(Solver):

    def __init__(self):
        self.source_bids = []
        self.demand_bids = []
        self.total_volume = 0
        self.log = Log(prefix="POOL")
        super().__init__()

    def all_participants(self):
        sellers = []
        buyers = []
        for bid in self.source_bids:
            sellers.append(bid.agent)
        for bid in self.demand_bids:
            buyers.append(bid.agent)
        return sellers, buyers

    def add_source(self, bids):
        if not isinstance(bids, list):
            bids = [bids]
        for bid in bids:
            self.source_bids.append(bid)

    def add_demand(self, bid):
        if isinstance(bid, list):
            for item in bid:
                self.demand_bids.append(item)
        else:
            self.demand_bids.append(bid)

    def _find_source_bid(self, agent):
        result = None
        for bid in self.source_bids:
            if bid.agent == agent:
                result = bid
                break
        return result

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

    def _find_demand_bid(self, agent):
        result = None
        for bid in self.demand_bids:
            if bid.agent == agent:
                result = bid
                break
        return result

    def find_bid(self, agent):
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
        result = None
        for bid in bids:
            #print(bid)
            if result is None:
                result = bid
            else:
                if bid.new_amount > result.new_amount:
                    result = bid
        return result

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
    '''
    b1 = Bid(1, 5)
    b2 = Bid(2, 8)
    b3 = Bid(3, 2)
    b4 = Bid(4, 1)

    p = Pool()
    p.add_source([b2, b4])
    p.add_demand([b1, b3])
    #print("_________ initial __________ \n", p)
    p.solve()
    print("__________ final ___________ \n", p)
    '''
    
    b1 = Bid(1, 5)
    b2 = Bid(2, 8)
    b3 = Bid(3, 2)
    b4 = Bid(4, 1)

    p = Pool()
    p.add_source([b1, b2])
    p.add_demand([b3, b4])
    #print("_________ initial __________ \n", p)
    print(p.size())
    p.solve()
    #print("__________ final ___________ \n", p)
    

    
    