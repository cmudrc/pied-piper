class Update:
    """
    Update the network
    """

    def update(self, duration: float, measure: bool = False):
        """
        Update the network
        """
        # Idle resource consumption & income
        for id in self.alives:
            # Resources
            for name in self.resource_names:
                resource_value = self.get_resource(id=id, name=name)
                resource_consumption_rate = self.idle_resource_rates[name]
                new_resource_value = resource_value - (resource_consumption_rate * duration)
                self.set_resource(id=id, name=name, value=new_resource_value)
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
                self.decide_destination(agent_id=id, duration=duration)

            # Execute
            action_queue.update(duration, measure=measure)


if __name__ == "__main__":

    from piperabm.model import Model

    model = Model()
    model.infrastructure.add_home(pos=[0, 0])
    model.bake()
    model.society.generate(num=1)

    print(f"deads: {len(model.society.deads)}")

    model.society.update(1000000)
    
    print(f"deads: {len(model.society.deads)}")