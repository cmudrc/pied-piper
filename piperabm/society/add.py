from piperabm.actions import Queue
from piperabm.resource import Resource, DeltaResource
from piperabm.unit import Unit


class Add:

    def add(
        self,
        name: str = '',
        settlement=None,
        queue=Queue(),
        resource=None,
        idle_fuel_rate=None,
        wealth=0
        ):
        """
        Add a new agent to the society
        """
        index = self.find_next_index()
        self.index_list.append(index)
        if resource is None:
            resource = Resource(
                current_resource={
                    'food': 0,
                    'water': 0,
                    'energy': 0
                },
                max_resource={
                    'food': None,
                    'water': None,
                    'energy': None
                }
            )
        if idle_fuel_rate is None:
            idle_fuel_rate = DeltaResource(
                {
                    'food': Unit(2, 'kg/day').to_SI(),
                    'water': Unit(4, 'kg/day').to_SI(),
                    'energy': 0
                }
            )
        if settlement is None:
            settlement_index = self.env.random_settlement()
        else:
            settlement_index = self.env.find_node(settlement)
        settlement_node = self.env.G.nodes[settlement_index]
        pos = settlement_node['boundary'].center
        self.G.add_node(
            index,
            name=name,
            settlement=settlement_index,
            pos=pos,
            active=True,
            queue=queue,
            resource=resource,
            idle_fuel_rate=idle_fuel_rate,
            wealth=wealth
            )

    def add_agents(self, n):
        for _ in range(n):
            self.add_agent()