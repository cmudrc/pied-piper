from copy import deepcopy

from piperabm.model.trade import Trade
from piperabm.tools.json_file import JsonFile
from piperabm.tools.delta import Delta


class Update(Trade):

    def run(
            self,
            n: int = None,
            step_size: float = 3600,
            save: bool = False,
            resume: bool = False,
            report: bool = False
        ):
        """
        Run model for multiple steps
        """
        # Remove previous save file if exists
        if self.path is not None:
            if resume is False:
                # Remove deltas
                simulation_file = JsonFile(self.path, self.name + '_' + 'simulation')
                simulation_file.remove()
                # Remove final state
                final_file = JsonFile(self.path, self.name + '_' + 'final')
                final_file.remove()
                # Load initial state if exists
                initial_file = JsonFile(self.path, self.name + '_' + 'initial')
                if initial_file.exists():
                    self.load_initial()
                else:
                    if save is True:
                        self.save_initial()
            else:
                # Load final state if exists
                final_file = JsonFile(self.path, self.name + '_' + 'final')
                if final_file.exists() is True:
                    self.load_final()
                else:
                    # Load initial state if final state doesn't exists
                    initial_file = JsonFile(self.path, self.name + '_' + 'initial')
                    if initial_file.exists() is True:
                        self.load_initial()
                        # Apply deltas if exists
                        simulation_file = JsonFile(self.path, self.name + '_' + 'simulation')
                        if simulation_file.exists() is True:
                            self.apply_deltas()

        # Run until all agents die
        if n is None:
            while True:
                self.update(
                    duration=step_size,
                    save=save,
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
                    save=save
                )

    def update(self, duration: float, save: bool = False):
        """
        Update model for a single steps
        """
        # Create current state
        if save is True:
            previous_serialized = deepcopy(self.serialize())

        # Update
        self.step += 1
        self.time += duration
        self.infrastructure.update(duration)
        self.society.update(duration)

        # Trade
        for market_id in self.infrastructure.markets:  # Agents in market
            agents = self.society.agents_in(id=market_id)
            if len(agents) >= 1:
                self.trade(agents=agents, market=[market_id])
        for home_id in self.infrastructure.homes:  # Agents in home
            agents = self.society.agents_in(id=home_id)
            if len(agents) >= 2:
                self.trade(agents=agents)
        '''
        markets = self.infrastructure.markets
        for home_id in self.infrastructure.homes:  # Agents in home
            agents = self.society.agents_in(id=home_id)
            if len(agents) >= 2:
                self.trade(agents=agents)
        '''

        # Charge Markets (resource influx)
        '''
        markets = self.infrastructure.markets
        #num = len(markets)
        #food_price = self.society.food_price
        #water_price = self.society.water_price
        #energy_price = self.society.energy_price
        for id in markets:
            enough_food = self.infrastructure.enough_food(id=id)
            enough_water = self.infrastructure.enough_water(id=id)
            enough_energy = self.infrastructure.enough_energy(id=id)
            self.infrastructure.balance(id=id, new_val=0)
            self.infrastructure.food(id=id, new_val=enough_food)
            self.infrastructure.water(id=id, new_val=enough_water)
            self.infrastructure.energy(id=id, new_val=enough_energy)
        '''
            
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

        # Create new current state and compare to previous one
        if save is True:
            current_serialized = self.serialize()
            delta = Delta.create(
                old=previous_serialized,
                new=current_serialized
            )
            self.append_delta(delta)
            self.save(state='final')

    def apply_delta(self, delta):
        """
        Update model by applying a delta
        """
        self.deserialize(
            Delta.apply(
                old=self.serialize(),
                delta=delta
            )
        )

    def apply_deltas(self):
        """
        Update model by applying all deltas
        """
        deltas = self.load_deltas()
        for delta in deltas:
            self.apply_delta(delta)