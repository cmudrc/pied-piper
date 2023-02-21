from copy import deepcopy


class Pool:

    def __init__(self):
        self.source_bids = []
        self.demand_bids = []

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

    def solve_step(self):
        biggest_source = self.find_biggest(self.source_bids)
        biggest_demand = self.find_biggest(self.demand_bids)
        #print(biggest_source, biggest_demand)
        if biggest_source is not None and biggest_demand is not None:
            diff = biggest_source.new_amount - biggest_demand.new_amount
            volume = min([biggest_source.new_amount, biggest_demand.new_amount])
            if diff > 0:
                biggest_source.new_amount = diff
                biggest_demand.new_amount = 0
            else:
                biggest_source.new_amount = 0
                biggest_demand.new_amount = -diff
            log_txt = "from: " + str(biggest_source.agent)
            log_txt += ", to: " + str(biggest_demand.agent)
            log_txt += ", amount: " + str(volume)
            #print(log_txt)
        else:
            volume = 0
        
        return volume

    def solve(self):
        volume = None
        while volume is None or volume != 0:
            volume = self.solve_step()

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
            size_source += bid.amount
        size_demand = 0
        for bid in self.demand_bids:
            size_demand += bid.amount
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
        bid = self._find_source_bid(agent)
        if bid is not None:
            result = bid
        bid = self._find_demand_bid(agent)
        if bid is not None:
            result = bid
        return result

    def find_biggest(self, bids):
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


class Bid:

    def __init__(self, agent: int, amount: float):
        self.agent = agent
        self.amount = amount
        self.new_amount = deepcopy(amount)

    def __str__(self):
        txt = '>>> agent: ' + str(self.agent) + ' amount: ' + str(self.amount) + ' new_amount: ' + str(self.new_amount)
        return txt


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
    p.add_source([Bid(1, 8)])
    p.add_demand([Bid(2, 8), Bid(3, 5)])
    #print("_________ initial __________ \n", p)
    p.solve()
    print("__________ final ___________ \n", p)
    

    
    