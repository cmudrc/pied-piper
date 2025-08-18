"""
Manage simulation execution: stepping the model forward and handling persistence.

This mix-in provides:
 - run(): loop over multiple time steps (or until all agents die),
   with optional save/resume behavior.
 - update(): perform a single time‐step update, including trading,
   agent/infrastructure updates, and optional delta‐based serialization.
"""

from copy import deepcopy
import keepdelta as kd

from piperabm.model.trade import Trade
from piperabm.tools.json_file import JsonFile


class Update(Trade):
    """
    Manage running simulation

    Inherits from Trade, so it has access to self.trade(…) for market transactions.
    """

    def run(
        self,
        n: int = None,
        step_size: float = 3600,
        save: bool = False,
        save_transactions: bool = False,
        resume: bool = False,
        report: bool = False,
    ):
        """
        Run model for multiple steps.

        Parameters
        ----------
        n : int or None
            Number of steps to run the model. If set to `None`, model keeps running until no agents remain alive in the society.
        step_size : float
            Time increment for each step (e.g. seconds). If set to large values, the model runs faster but the model may not be able to capture some of the interactions.
        save : bool
            If `True`, saves the results buy serializing state snapshots and creating deltas and recording them to disk. The initial state of model (named `initial.json`), the final state of the model (named `final.json`) as well as the changes (deltas) during each step (named `simulation.json`) can be found in the `result` folder in the working directory.
        save_transactions : bool
            If `True`, record all transactions to disk. The file will be named `transaction.csv` and will be located in the `result` folder in the working directory.
        resume : bool
            If `True`, attempt to resume from last saved state instead of starting fresh.
        report : bool
            If `True`, print progress for n-step runs.
        """
        # Remove previous save file if exists
        if self.path is not None:
            path = self.result_directory
            if resume is False:
                # Remove deltas
                simulation_file = JsonFile(path, "simulation")
                simulation_file.remove()
                # Remove final state
                final_file = JsonFile(path, "final")
                final_file.remove()
                # Load initial state if exists
                initial_file = JsonFile(path, "initial")
                if initial_file.exists():
                    self.load_initial()
                else:
                    if save is True:
                        self.save_initial()
            else:
                # Load final state if exists
                final_file = JsonFile(path, "final")
                if final_file.exists() is True:
                    self.load_final()
                else:
                    # Load initial state if final state doesn't exists
                    initial_file = JsonFile(path, "initial")
                    if initial_file.exists() is True:
                        self.load_initial()
                        # Apply deltas if exists
                        simulation_file = JsonFile(path, "simulation")
                        if simulation_file.exists() is True:
                            self.apply_deltas()

        # Run until all agents die
        if n is None:
            while True:
                self.update(
                    duration=step_size, save=save, save_transactions=save_transactions
                )
                if len(self.society.alive_agents) == 0:
                    break

        # Run for certain steps
        else:
            for i in range(n):
                if report is True:
                    print(f"Progress: {(i + 1) / n * 100:.1f}% complete")
                self.update(
                    duration=step_size, save=save, save_transactions=save_transactions
                )

    def update(
        self, duration: float, save: bool = False, save_transactions: bool = False
    ):
        """
        Update model for a single step.

        Steps performed:
        1. (If save) snapshot current state for delta comparison.
        2. Execute trades in each market and household.
        3. Update agent behaviors and infrastructure effects.
        4. Reset market balances and refill resources.
        5. Increment time and step counters.
        6. (If save) compute & append state delta, save final state.
        7. (If save_transactions) append transaction list to log.
        """
        # Delta
        if save is True:
            # Create current state
            previous_serialized = deepcopy(self.serialize())

        # Trade
        transactions = []
        for market_id in self.infrastructure.markets:  # Agents in market
            agents = self.society.agents_in(id=market_id)
            if len(agents) >= 1:
                transactions += self.trade(agents=agents, markets=[market_id])
        for home_id in self.infrastructure.homes:  # Agents in home
            agents = self.society.agents_in(id=home_id)
            if len(agents) >= 2:
                transactions += self.trade(agents=agents)
        # transactions
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
                enough_amount = self.infrastructure.get_enough_resource(
                    id=id, name=name
                )
                self.infrastructure.set_resource(id=id, name=name, value=enough_amount)

        # General
        self.step += 1
        self.time += duration

        # Delta
        if save is True:
            # Create new current state and compare it to the previous one
            current_serialized = self.serialize()
            delta = kd.create(old=previous_serialized, new=current_serialized)
            self.append_delta(delta)
            self.save_final()

        # Transactions
        if save_transactions is True:
            self.append_transactions(transactions)

        return transactions
