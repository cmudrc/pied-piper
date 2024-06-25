class Update:
    """
    Update the network
    """

    def update(self, duration: float, measure: bool = False):
        """
        Update the network
        """
        # Measure accessibility (first entry)
        if measure is True and self.model.accessibility.pristine is True:
            self.model.accessibility.add_date(self.model.date)
            self.model.accessibility.pristine = False

        #print(self.alive_agents)
        # Idle resource consumption & income
        for id in self.alives:
            # Food
            food = self.get_resource(id=id, name='food')
            food_rate = self.get_idle_fuel_rate(id=id, name='food')
            new_food = food - food_rate * duration
            self.set_resource(id=id, name='food', value=new_food)
            # Water
            water = self.get_resource(id=id, name='water')
            water_rate = self.get_idle_fuel_rate(id=id, name='water')
            new_water = water - water_rate * duration
            self.set_resource(id=id, name='water', value=new_water)
            # Energy
            energy = self.get_resource(id=id, name='energy')
            energy_rate = self.get_idle_fuel_rate(id=id, name='energy')
            new_energy = energy - energy_rate * duration
            self.set_resource(id=id, name='energy', value=new_energy)
            # Income
            balance = self.get_balance(id)
            income = self.get_income(id)
            new_balance = balance + income * duration
            self.set_balance(id, value=new_balance)

        # Action update
        for id in self.alives:
            action_queue = self.actions[id]
            if action_queue.done is True:
                action_queue.reset()
                # Decide
                markets = self.infrastructure.markets
                best_destination, _ = self.select_top_destination(agent_id=id, destinations=markets, is_market=True)
                # When market is available
                if best_destination is not None:
                    self.go_and_comeback_and_stay(agent_id=id, destination_id=best_destination)
                else:
                    possible_destinations = self.infrastructure.filter_nodes_closer_than(
                        id=self.get_current_node(id),
                        nodes=self.infrastructure.homes,
                        distace=100
                    )
                    best_destination, _ = self.select_top_destination(agent_id=id, destinations=possible_destinations, is_market=False)
                    self.go_and_comeback_and_stay(agent_id=id, destination_id=best_destination)
            # Execute
            action_queue.update(duration, measure=measure)

        # Trade
        '''
        for market_id in self.infrastructure.markets:
            agents = self.agents_in(id=market_id)
            if len(agents) >= 1:
                self.trade(agents=agents, market=market_id)
        for home_id in self.infrastructure.homes:
            agents = self.agents_in(id=home_id)
            if len(agents) >= 2:
                self.trade(agents=agents)
        '''

        # Measure accessibility
        if measure is True:
            date = self.model.date
            self.model.accessibility.add_date(date)
            for id in self.agents:
                utility_food = self.utility(id, 'food')
                utility_water = self.utility(id, 'water')
                utility_energy = self.utility(id, 'energy')
                utility = {
                    'food': utility_food,
                    'water': utility_water,
                    'energy': utility_energy,
                }
                self.model.accessibility.add_utility(id, utility)


if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate_agents(num=1)
    print(f"deads: {len(model.society.deads)}")
    model.society.update(1000000)
    print(f"deads: {len(model.society.deads)}")