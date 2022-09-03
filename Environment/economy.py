from distutils.log import info


class Economy():
    ''' used for placing an order '''
    def __init__(self, orders=None, info=None):
        if orders is None:
            self.orders = list()
        else:
            self.orders = orders
        self.info = info # stores the volume of source and demand for each point

        self.start_name_list = None
        self.end_name_list = None

    def analyze(self):
        ''' dynamic programming '''
        start_name_list = list()
        end_name_list = list()
        for order in self.orders:
            if order.start not in start_name_list:
                start_name_list.append(order.start)
            if order.end not in end_name_list:
                end_name_list.append(order.end)
        self.start_name_list = start_name_list
        self.end_name_list = end_name_list
        self.all_orders_same_start = self.categorize_orders_same_start()
        self.all_orders_same_end = self.categorize_orders_same_end()

    def categorize_orders_same_end(self):
        ''' creates a dictionary of end_point, categorizes all orders based on end point '''
        all_orders_same_end = dict()
        for end_name in self.end_name_list:
            orders_same_end_list = list()
            for order in self.orders:
                if order.end == end_name:
                    orders_same_end_list.append(order)
            all_orders_same_end[end_name] = orders_same_end_list
        #for end_name in list(all_orders_same_end.keys()):
        #    print(end_name, [order.start for order in all_orders_same_end[end_name]])
        return all_orders_same_end

    def categorize_orders_same_start(self):
        ''' creates a dictionary of start_point, categorizes all orders based on start point '''
        all_orders_same_start = dict()
        for start_name in self.start_name_list:
            orders_same_start_list = list()
            for order in self.orders:
                if order.start == start_name:
                    orders_same_start_list.append(order)
            all_orders_same_start[start_name] = orders_same_start_list
        #for start_name in list(all_orders_same_start.keys()):
        #    print(start_name, [order.end for order in all_orders_same_start[start_name]])
        return all_orders_same_start

    def run_step(self):
        self.analyze()
        def score_calculate(distance, price_factor):
            return distance * price_factor
        all_orders = self.all_orders_same_end
        transaction_list = list()
        for end_name in self.end_name_list:
            orders = all_orders[end_name]
            scores = list()
            for order in orders: # sorting orders based on score
                if self.info[order.start]['source'] > 0 and self.info[order.end]['demand'] > 0:
                    order.score = score_calculate(order.distance, order.price_factor)
                    scores.append(order.score) # used for sorting
                    orders = [x for _,x in sorted(zip(scores, orders), reverse=True)]
            #print([order for order in orders])
                    #print([(order.start, order.end, order.score, order.volume) for order in orders])
            transaction_list.append(orders[0]) # best fit
            #print(orders[0].start, orders[0].end)
        #print([[x.start, x.end] for x in transaction_list])
        
        def make_transactions(transaction_list):
            if len(transaction_list) > 0:
                for order in transaction_list:
                    make_transaction(self, order=order)
            else:
                print("Done")

        def make_transaction(self, order):
            source = self.info[order.start]['source']
            demand = self.info[order.end]['demand']
            #print(self.info[order.start]['source'], self.info[order.end]['demand'])
            if source >= demand:
                self.info[order.start]['source'] = source - demand
                self.info[order.end]['demand'] = 0
            else:
                self.info[order.start]['source'] = 0
                self.info[order.end]['demand'] = demand - source 
            #print(self.info[order.start]['source'], self.info[order.end]['demand'])   
            
        make_transactions(transaction_list=transaction_list)
        print(self.info)

    def run(self):
        self.run_step()
        info_first = self.info.copy()
        while True:
            self.run_step()
            if self.info == info_first:
                break


class Order():
    ''' used for placing an order '''
    def __init__(self, start, end, distance, price_factor):
        self.start = start # start-node name
        self.end = end # end-node name
        self.distance = distance # distance between two nodes
        self.price_factor = price_factor # price factor, will be multiplied by score to result in final score
        self.score = None # will be defined by calculations in Economy class.
    
    def __str__(self):
        return (self.start, ' to ', self.end)


if __name__ == "__main__":
    order_1 = Order(start='city_1', end='city_2', distance=1, price_factor=1.2)
    order_2 = Order(start='city_1', end='city_1', distance=0.1, price_factor=1)
    order_3 = Order(start='city_3', end='city_2', distance=2, price_factor=0.9)
    order_4 = Order(start='city_4', end='city_2', distance=1.5, price_factor=1)
    order_5 = Order(start='city_3', end='city_4', distance=1.5, price_factor=1)

    info = {
        'city_1': {
            'source' : 15,
            'demand' : 6
        },
        'city_2': {
            'source' : 0,
            'demand' : 5
        },
        'city_3': {
            'source' : 3,
            'demand' : 1
        },
        'city_4': {
            'source' : 1,
            'demand' : 6
        },
    }
    eco = Economy(
        orders=[order_1, order_2, order_3, order_4, order_5],
        info=info
        )

    print(eco.info)
    eco.run()