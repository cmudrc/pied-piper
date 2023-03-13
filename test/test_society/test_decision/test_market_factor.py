import unittest
from copy import deepcopy

from piperabm.society.decision.factors import MarketFactor
from piperabm.society.sample import soc_1 as soc


class TestMarketFactor(unittest.TestCase):

    def setUp(self):
        self.soc = deepcopy(soc)
        agents = soc.all_agents()
        agent = agents[0]
        #start_date = Date.today() + DT(days=1)
        #end_date = start_date + DT(days=1)
        #path_graph = soc.env.to_path_graph(start_date, end_date)
        #path_graph.show()
        route = (0, 1)

        market_factor_calculator = MarketFactor(
            society=soc,
            agent=agent,
            route=route
        )

        #participants = market_factor_calculator.participants
        #print(participants)
        #source_factor = market_factor_calculator.calculate_source_factor()
        #demand_factor = market_factor_calculator.calculate_demand_factor()
        #print(source_factor, demand_factor)
        market_factor = market_factor_calculator.calculate()
        #print(market_factor)
        self.market_factor_calculator = market_factor_calculator

    def test_market_factor_calculate(self):
        market_factor = self.market_factor_calculator.calculate()


if __name__ == "__main__":
    unittest.main()