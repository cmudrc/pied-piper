from copy import deepcopy

from piperabm.model.trade import Trade
from piperabm.tools.json_file import JsonFile
from piperabm.tools.delta import Delta


class Update(Trade):
    """
    Manage running simulation
    """

    def run(
            self,
            n: int = None,
            step_size: float = 3600,
            save: bool = False,
            save_transactions: bool = False,
            resume: bool = False,
            report: bool = False
        ):
        """
        Run model for multiple steps
        """
        # Remove previous save file if exists
        if self.path is not None:
            path = self.result_directory
            if resume is False:
                # Remove deltas
                simulation_file = JsonFile(path, 'simulation')
                simulation_file.remove()
                # Remove final state
                final_file = JsonFile(path, 'final')
                final_file.remove()
                # Load initial state if exists
                initial_file = JsonFile(path, 'initial')
                if initial_file.exists():
                    self.load_initial()
                else:
                    if save is True:
                        self.save_initial()
            else:
                # Load final state if exists
                final_file = JsonFile(path, 'final')
                if final_file.exists() is True:
                    self.load_final()
                else:
                    # Load initial state if final state doesn't exists
                    initial_file = JsonFile(path, 'initial')
                    if initial_file.exists() is True:
                        self.load_initial()
                        # Apply deltas if exists
                        simulation_file = JsonFile(path, 'simulation')
                        if simulation_file.exists() is True:
                            self.apply_deltas()

        # Run until all agents die
        if n is None:
            while True:
                self.update(
                    duration=step_size,
                    save=save,
                    save_transactions=save_transactions
                )
                if len(self.society.alive_agents) == 0:
                    break

        # Run for certain steps
        else:
            for i in range(n):
                if report is True:
                    print(f"Progress: {(i + 1) / n * 100:.1f}% complete")
                self.update(
                    duration=step_size,
                    save=save,
                    save_transactions=save_transactions
                )

    def update(self, duration: float, save: bool = False, save_transactions: bool = False):
        """
        Update model for a single steps
        """
        # Delta
        if save is True:
            # Create current state
            previous_serialized = deepcopy(self.serialize())

        # Trade
        for market_id in self.infrastructure.markets:  # Agents in market
            agents = self.society.agents_in(id=market_id)
            if len(agents) >= 1:
                transactions = self.trade(agents=agents, markets=[market_id])
        for home_id in self.infrastructure.homes:  # Agents in home
            agents = self.society.agents_in(id=home_id)
            if len(agents) >= 2:
                transactions = self.trade(agents=agents)
        #transactions
        for transaction in transactions:
            transaction.append(self.time)

        # Agents activity impact
        self.society.update(duration)

        # Climate impact
        self.infrastructure.update(duration)

        # Charge Markets (resource influx)
        markets = self.infrastructure.markets
        for id in markets:
            # Reset balance
            self.infrastructure.set_balance(id=id, value=0)
            # Reset resources
            for name in self.resource_names:
                enough_amount = self.infrastructure.get_enough_resource(id=id, name=name)
                self.infrastructure.set_resource(id=id, name=name, value=enough_amount)

        # General
        self.step += 1
        self.time += duration    
        '''
            current_balance = self.infrastructure.balance(id=id)
            current_food = self.infrastructure.food(id=id)
            needed_food = enough_food - current_food
            if needed_food > 0:
                needed_food_value = food_price * needed_food
            else:
                needed_food_value = 0

            current_water = self.infrastructure.water(id=id)
            needed_water = enough_water - current_water
            if needed_water > 0:
                needed_water_value = water_price * needed_water
            else:
                needed_water_value = 0
            current_energy = self.infrastructure.energy(id=id)
            
            needed_energy = enough_energy - current_energy
            if needed_energy > 0:
                needed_energy_value = energy_price * needed_energy
            else:
                needed_energy_value = 0
            total_needed = needed_food_value + needed_water_value + needed_energy_value
            if total_needed > 0:
                balance_for_food = (needed_food_value / total_needed) * current_balance
                balance_for_water = (needed_water_value / total_needed) * current_balance
                balance_for_energy = (needed_energy_value / total_needed) * current_balance
                get_food = balance_for_food / food_price
                get_water = balance_for_water / water_price
                get_energy = balance_for_energy / energy_price
                actual_get_food = min(get_food, needed_food)
                actual_get_water = min(get_water, needed_water)
                actual_get_energy = min(get_energy, needed_energy)
                self.infrastructure.food(id=id, new_val=current_food+actual_get_food)
                self.infrastructure.water(id=id, new_val=current_water+actual_get_water)
                self.infrastructure.energy(id=id, new_val=current_energy+actual_get_energy)
                self.infrastructure.balance(
                    id=id,
                    new_val=current_balance-(
                        actual_get_food*food_price + \
                        actual_get_water*water_price + \
                        actual_get_energy*energy_price
                    )
                )
        '''

        # Delta
        if save is True:
            # Create new current state and compare it to the previous one
            current_serialized = self.serialize()
            delta = Delta.create(
                old=previous_serialized,
                new=current_serialized
            )
            self.append_delta(delta)
            self.save_final()

        # Transactions
        if save_transactions is True:
            if transactions is not None and \
            len(transactions) > 0:
                self.append_transactions(transactions)

        return transactions