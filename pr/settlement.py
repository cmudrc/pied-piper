import matplotlib.pyplot as plt

from pr.tools import Entity
from pr.tools.boundery import Circular, Rectangular, Point
from pr.agent import Agent
from pr.tools import find_element, element_exists
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
        all_agents=None,
        members=[],
        asset:Asset=None,
        **entity_kwargs
    ):
        """
        Args:
            max_population: maximum number of agents within the settlement
            boundery: the boundery of the settlement
            members: a list of agents' names that are associated with the settlement
            asset: manages the settlement resources (apart from agent's resources)
            **entity_kwargs: kwargs for entity class
        """
        super().__init__(
            **entity_kwargs
        )
        self.all_agents = all_agents
        self.members = members
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
            self.boundery = Point(
                center=self.pos
            )

    def register_agent(self, agent):
        """
        Assign a new agent membership to the settlement
        """
        if isinstance(agent, Agent):
            agent_name = agent.name
        elif isinstance(agent, str):
            agent_name = agent
        if not agent_name in self.members:
            if len(self.members) < self.max_population:
                self.members.append(agent_name)
            else:
                print('ERROR: "max_population" reached.')
        else:
            print('ERROR: agent already exists.')

    def register_agents(self, agents: list):
        """
        Assign new agents memberships to the settlement in batch
        """
        for agent in agents:
            self.register_agent(agent)

    def tunnel_agent(self, agent):
        """
        Instantly transfer the agent into the settlement
        """
        if isinstance(agent, Agent):
            agent_name = agent.name
        elif isinstance(agent, str):
            agent_name = agent
        agent = find_element(agent_name, self.all_agents)
        if agent is not None:
            agent.pos = self.boundery.rand_pos()
        else:
            print("Agent not found.")

    def tunnel_agents(self, agents: list):
        """
        Instantly transfer a list of agents into the settlement
        """
        for agent in agents:
            self.tunnel_agent(agent)

    def add_agent(self, agent):
        """
        Add a single agent to members and move it inside the settlement
        """
        self.register_agent(agent)
        self.tunnel_agent(agent)

    def add_agents(self, agents: list):
        """
        Add a list of agents to members and move it inside the settlement
        """
        for agent in agents:
            self.add_agent(agent)

    def find_agents_inside(self, agents: list) -> list:
        """
        Find and add all agents within boundery based on their pos
        """
        result = []
        for agent in agents:
            if self.boundery.is_in(agent):
                result.append(agent.name)
        return result

    def to_graph(self):
        pass

    def solve(self):
        # gather all agents
        # 
        pass

    def is_in(self, element):
        return self.boundery.is_in(element)

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
            'agents': self.members,
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
        self.members = d['agents']
        self.asset = d['asset']

    def to_plt(self, ax=None, all_agents=None):
        """
        Add the required elements to plt
        """
        settlement_to_plt(self.to_dict(), ax, all_agents)

    def show(self):
        self.boundery.show()


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
        all_agents=all_agents,
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    s.add_agent(all_agents[0])
    print(s.members[0])
    print(all_agents[0].pos)
    #print(s.agents)
    #s.show()