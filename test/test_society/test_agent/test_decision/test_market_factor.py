import unittest
from copy import deepcopy

from piperabm.unit import Date
from piperabm.society.agent.decision.factors import MarketFactor
from piperabm.society.sample import sample_society_0


class TestMarketFactor(unittest.TestCase):

    def setUp(self):
        society = deepcopy(sample_society_0)
        start_date = Date(2020, 1, 5)
        end_date = Date(2020, 1, 10)
        society.env.update_elements(start_date, end_date)
        
        agent_0 = society.find_agent(agent_info=0)
        #print(agent_0)
        agent_0.observe(society)
        agent_0_route = (0, 1)
        self.market_factor_calculator_0 = MarketFactor(
            agent=agent_0,
            route=agent_0_route
        )

        agent_1 = society.find_agent(agent_info=1)
        #print(agent_1)
        agent_1.observe(society)
        agent_1_route = (1, 0)
        self.market_factor_calculator_1 = MarketFactor(
            agent=agent_1,
            route=agent_1_route
        )

    def test_trade_participants(self):
        participants_0 = self.market_factor_calculator_0.trade_participants(target=0)
        #print(participants_0)
        self.assertListEqual(participants_0, [0])
        participants_1 = self.market_factor_calculator_1.trade_participants(target=1)
        #print(participants_1)
        self.assertListEqual(participants_1, [1])

    def test_calculate_source_factor(self):
        source_factor_0 = self.market_factor_calculator_0.calculate_source_factor()
        #print(source_factor_0)
        source_factor_1 = self.market_factor_calculator_1.calculate_source_factor()
        #print(source_factor_1)

    def test_calculate_demand_factor(self):
        demand_factor_0 = self.market_factor_calculator_0.calculate_demand_factor()
        #print(demand_factor_0)
        demand_factor_1 = self.market_factor_calculator_1.calculate_demand_factor()
        #print(demand_factor_1)

    def test_calculate(self):
        market_factor_0 = self.market_factor_calculator_0.calculate()
        #print(market_factor_0)
        market_factor_1 = self.market_factor_calculator_1.calculate()
        #print(market_factor_1)


if __name__ == "__main__":
    unittest.main()