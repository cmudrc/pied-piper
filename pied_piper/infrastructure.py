from turtle import st
import numpy as np

from agent import Agent
from tools import DegradationProperty
from tools import find_element, euclidean_distance


class Production(DegradationProperty):
    def __init__(
        self,
        name=None,
        pos=None,
        access=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
    ):
        super().__init__(
            active=active,
            initial_cost=initial_cost,
            initiation_date=initiation_date,
            distribution=distribution,
            seed=seed
        )
        self.name = name
        self.pos = pos
        self.access = access

    def has_access(self, agent):
        """
        Check the agent to see whether it has access to the source or not
        
        Args:
            agent: either an Agent instance or agent's name
        
        Returns:
            True/False
        """
        result = False
        if self.access is None:
            result = False
        elif self.access == 'all':
            result = True
        elif isinstance(self.access, list):
            if isinstance(agent, Agent):
                if agent.name in self.access:
                    result = True
            elif isinstance(agent, str):
                if agent in self.access:
                    result = True
        return result
        


class Road(DegradationProperty):
    def __init__(
        self,
        start_settlement,
        end_settlement,
        double_sided=True,
        length=None,
        name=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
    ):
        super().__init__(
            active=active,
            initial_cost=initial_cost,
            initiation_date=initiation_date,
            distribution=distribution,
            seed=seed
        )
        self.name = name
        self.start_settlement = start_settlement
        self.end_settlement = end_settlement
        self.double_sided = double_sided
        self.length = length

        self.transportation_needs = [
            'foot',
            'vehicle',
        ]

    def update_length(self, all_nodes):
        if self.length is None:
            self.length = self.distance_calc(all_nodes)

    def distance_calc(self, all_nodes):
        start_x, start_y = None, None
        node = find_element(self.start_node)
        start_x = node.pos[0]
        start_y = node.pos[1]

        end_x, end_y = None, None
        node = find_element(self.end_node)
        end_x = node.pos[0]
        end_y = node.pos[1]

        dist = euclidean_distance(start_x, end_x, start_y, end_y)
        return dist


if __name__ == "__main__":
    class City:
        """
        A helper class.
        """
        
        def __init__(self, name, pos):
            self.name = name
            self.pos = pos

    r = Road(
        start_node='city_1',
        end_node='city_2'
    )
    all_nodes = [
        City(name='city_1', pos=[0, 0]),
        City(name='city_2', pos=[0, 1]),
    ]
    length = r.length_calc(all_nodes=all_nodes)
    print(length)