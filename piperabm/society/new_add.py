try: from .agent import Agent
except: from agent import Agent


class Add:

    def add_agent(
            self,
            id: int,
            name: str = '',
            origin_node=None,
            current_node=None,
            transportation=None,
            queue=None,
            resource=None,
            idle_fuel_rate=None,
            balance=0,
            wealth_factor=1
        ):
        agent = Agent(
            id=id,
            name=name,
            origin_node=origin_node,
            current_node=current_node,
            transportation=transportation,
            queue=queue,
            resource=resource,
            idle_fuel_rate=idle_fuel_rate,
            balance=balance,
            wealth_factor=wealth_factor
        )
        self.G.add_node(
            id,
            agent=agent,
            ready_for_trade=False
        )

    def add_agents(self):
        pass