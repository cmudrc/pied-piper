from piperabm.economy.market.pool.bid import Bid
from piperabm.economy.market.pool.query import Query
from piperabm.economy.market.pool.solver import Solver


class Pool(Solver, Query):
    """
    Solve pool as a single-resource allocation problem
    """

    def __init__(self):
        self.source_bids = []
        self.demand_bids = []
        super().__init__()

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
    
    '''
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
    '''


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
    stat = p.solve()
    print("__________ final ___________")
    print(p)
    print("__________ stat ___________")
    print(stat)
    