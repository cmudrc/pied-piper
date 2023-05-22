from piperabm.agent.brain.decision.decision import Decision
from piperabm.actions import Trade


class TradingDecision(Decision):

    def decide(self, observation: dict):
        action = None
        decision_buy_or_sell = self.buy_or_sell(observation)
        if decision_buy_or_sell == 'buy':
            action = self.how_much_buy(observation)
        elif decision_buy_or_sell == 'sell':
            action = self.how_much_sell(observation)
        return action

    def buy_or_sell(self, observation):
        pass

    def how_much_buy(self, observation):
        start_date = observation['start_date']
        action = Trade(start_date)
        return action

    def how_much_sell(self, observation):
        start_date = observation['start_date']
        action = Trade(start_date)
        return action

    def estimate_market_size(self):
        pass