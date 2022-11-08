import matplotlib.pyplot as plt

from pr.tools import Entity
from pr.tools.boundery import Circular, Rectangular
from pr.agent import Agent
from pr.tools import find_element
from pr.graphics.plt import settlement_to_plt
from pr.asset import Asset


entity_kwargs = {
    'name': None,
    'pos': [0, 0],
    'active': True,
    'initial_cost': None,
    'initiation_date': None,
    'distribution': None,
    'seed': None,
}


class Settlement(Entity):
    """
    Represents a place where people interact with each other freely, e.g., village, group, city, etc.
    They are nodes of the graph, where edges are infrastructures.
    """

    def __init__(
        self,
        max_population=10,
        boundery=None,
        agents=[],
        asset:Asset=None,
        **entity_kwargs
    ):
        """
        Args:
            max_population: maximum number of agents within the settlement
            boundery: the boundery of the settlement
            agents: a list of agents names that are within the settlement
            infrastructures: a list of infrastructure names that are within the settlement
            **entity_kwargs: kwargs for entity class
        """
        super().__init__(
            **entity_kwargs
        )
        self.agents = agents
        self.asset = asset
        self.max_population = max_population
        if boundery is not None:
            if boundery['type'] == 'circular':
                self.boundery = Circular(
                    center=self.pos,
                    radius=boundery['radius']
                )
            elif boundery['type'] == 'rectangular':
                self.boundery = Rectangular(
                    center=self.pos,
                    width=boundery['width'],
                    height=boundery['height'],
                    theta=boundery['theta']
                )
        else:
            self.boundery = Circular(
                center=self.pos,
                radius=0
            )

    def add_agent(self, agent):
        """
        Add a single agent
        """
        if isinstance(agent, Agent) and \
            agent.name not in self.agents and \
                len(self.agents) < self.max_population:
            agent.settlement = self.name
            if not self.boundery.is_in(agent):
                agent.pos = self.boundery.rand_pos()
            self.agents.append(agent.name)
        else:
            raise ValueError

    def add_agents(self, agents: list):
        """
        Add a list of agents
        """
        for agent in agents:
            self.add_agent(agent)

    def find_all_agents_by_pos(self, agents: list):
        """
        Find and add all agents within boundery based on their pos
        """
        for agent in agents:
            if self.boundery.is_in(agent):
                self.add_agent(agent)

    def find_all_agents_by_settlement(self, agents: list):
        """
        Find and add all agents having the settlement name based
        """
        for agent in agents:
            if agent.settlement == self.name:
                self.add_agent(agent)

    def find_all_agents(self, agents: list):
        """
        Find and add all agents having the settlement name based
        """
        self.find_all_agents_by_pos(agents)
        self.find_all_agents_by_settlement(agents)

    def has(self, agent_name):
        pass

    def to_graph(self):
        pass

    def solve(self):
        # gather all agents
        # 
        pass

    def to_dict(self):
        dictionary = {
            'name': self.name,
            'pos': self.pos,
            'active': self.active,
            'initial_cost': self.initial_cost,
            'initiation_date': self.initiation_date,
            'distribution': None,
            'seed': self.seed,
            'max_population': self.max_population,
            'boundery': self.boundery.to_dict(),
            'agents': self.agents,
            'asset': None,
        }
        if self.asset is not None:
            dictionary['asset'] = self.asset.to_dict()
        if self.distribution is not None:
            dictionary['distribution'] = self.distribution.to_dict()
        return dictionary

    def from_dict(self, dictionary: dict):
        ############
        d = dictionary
        self.name = d['name']
        self.pos = d['pos']
        self.active = d['active']
        self.initial_cost = d['initial_cost']
        self.initiation_date = d['initiation_date']
        self.distribution = d['distribution']
        self.seed = d['seed']
        self.max_population = d['max_population']
        self.boundery = d['boundery']
        self.agents = d['agents']
        self.asset = d['asset']

    def to_plt(self, ax=None, all_agents=None):
        """
        Add the required elements to plt
        """
        settlement_to_plt(self.to_dict(), ax, all_agents)


if __name__ == "__main__":
    from agent import Agent

    all_agents = [
        Agent(
            name='John',
            pos=[1, 1]
        ),
        Agent(
            name='Betty',
            pos=[1, 1]
        )
    ]

    s = Settlement(
        name='home_1',
        pos=[0, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    s.add_agents(all_agents)
    #print(s.agents)
    s.show()