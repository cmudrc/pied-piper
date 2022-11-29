import matplotlib.pyplot as plt
import networkx as nx

from piperabm.boundery import Circular, Point, Rectangular
from piperabm.degradation import DegradationProperty
from piperabm.agent import Agent
from piperabm.tools import find_element
from piperabm.graphics.plt import settlement_to_plt
from piperabm.asset import Asset


degradation_kwargs = {
    'active': True,
    'initial_cost': None,
    'initiation_date': None,
    'distribution': None,
    'seed': None,
}


class Settlement(DegradationProperty):
    """
    Represents a place where people interact with each other freely, e.g., village, group, city, etc.
    They are nodes of the graph, where edges are infrastructures.
    """

    def __init__(
        self,
        name=None,
        pos=[0, 0],
        max_population=None,
        boundery=None,
        all_agents=None,
        members=[],
        asset:Asset=None,
        **degradation_kwargs
    ):
        """
        Args:
            name: 
            pos: 
            max_population: maximum number of agents within the settlement
            boundery: the boundery of the settlement
            all_agents: a reference to the main list of all agents (instances of Agent class)
            members: a list of agents' names that are associated with the settlement
            asset: manages the settlement resources (apart from agent's resources)
            **degradation_kwargs: kwargs for degradation class
        """
        super().__init__(
            **degradation_kwargs
        )
        self.name = name
        self.pos = pos
        self.all_agents = all_agents
        self.members = members
        self.asset = asset
        self.max_population = max_population
        self.add_boundery(boundery)

    def _add_boundery_from_dict(self, boundery_dict: dict):
        boundery = boundery_dict
        if boundery['type'] == 'circular':
            self.boundery = Circular(
                radius=boundery['radius']
            )
            self.boundery.center = self.pos
        elif boundery['type'] == 'rectangular':
            self.boundery = Rectangular(
                width=boundery['width'],
                height=boundery['height'],
                theta=boundery['theta']
            )
            self.boundery.center = self.pos
        else:
            self.boundery = Point()
            self.boundery.center = self.pos

    def add_boundery(self, boundery):
        if isinstance(boundery, dict):
            self._add_boundery_from_dict(boundery_dict=boundery)
        elif isinstance(boundery,
            (
                Point,
                Circular,
                Rectangular
            )
        ):
            self.boundery = boundery
            self.boundery.center = self.pos
        elif boundery is None:
            self.boundery = Point()
            self.boundery.center = self.pos

    def agent_name_exists_in_model(self, agent_name: str) -> bool:
        if self.all_agents is not None:
            agent = find_element(agent_name, self.all_agents)
            if agent is None:
                agent_exists_in_model = False
            else: agent_exists_in_model = True
        else:
            agent = None
            agent_exists_in_model = True
        return agent_exists_in_model

    def register_agent(self, agent):
        """
        Assign a new agent membership to the settlement
        """
        if isinstance(agent, Agent):
            agent_name = agent.name
        elif isinstance(agent, str):
            agent_name = agent

        if agent_name not in self.members and \
            self.agent_name_exists_in_model(agent_name):
            if len(self.members) < self.max_population:
                self.members.append(agent_name)
                agent = find_element(agent_name, self.all_agents)
                agent.settlement = self.name
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
            #print(self.boundery.rand_pos())
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
        self.register_agents(agents)
        self.tunnel_agents(agents)

    def find_agents_inside(self) -> list:
        """
        Find and add all agents within boundery based on their pos
        """
        result = []
        for agent in self.all_agents:
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
            'max_population': self.max_population,
            'boundery': self.boundery.to_dict(),
            'agents': self.members,
            'asset': None,
        }
        dictionary = {**dictionary, **self.degradation_to_dict()}
        if self.asset is not None:
            dictionary['asset'] = self.asset.to_dict()
        return dictionary

    def from_dict(self, dictionary: dict):
        d = dictionary
        self.degradation_from_dict(dictionary)
        self.name = d['name']
        self.pos = d['pos']
        self.max_population = d['max_population']
        self.add_boundery(d['boundery'])
        self.members = d['agents']
        
        self.asset = None
        asset_dict = d['asset']
        if asset_dict is not None:
            self.asset = Asset().from_dict(asset_dict)

    def to_plt(self, ax=None):
        """
        Add the required elements to plt
        """
        settlement_to_plt(self.to_dict(), ax, self.all_agents)

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.axis('equal')
        xlim, ylim = self.boundery.xylim()
        plt.xlim(xlim)
        plt.ylim(ylim)
        self.to_plt(ax)
        plt.show()


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
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )

    print(s.is_in(all_agents[0]))
    s.tunnel_agent(all_agents[0].name)
    print(s.is_in(all_agents[0]))
    
    s.show()