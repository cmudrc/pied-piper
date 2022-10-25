try:
    from .tools import Entity
except:
    from tools import Entity

try:
    from .tools.boundery import Circular, Rectangular
except:
    from tools.boundery import Circular, Rectangular

try:
    from .agent import Agent
except:
    from agent import Agent

try:
    from .tools import find_element
except:
    from tools import find_element

try:
    from .tools import entity_kwargs
except:
    from tools import entity_kwargs


class Settlement(Entity):
    """
    Represents a place where people interact with each other freely, e.g., village, group, city, etc.
    They are nodes of the graph, where edges are infrastructures.
    """

    def __init__(
        self,
        max_population=10,
        boundery=None,
        agents=None,
        infrastructure=None,
        **entity_kwargs
    ):
        """
        Args:
            max_population: maximum number of agents within the settlement
            boundery: the boundery of the settlement
            agents: 
            infrastructures: 
            **entity_kwargs: kwargs for entity class
        """
        super().__init__(
            **entity_kwargs
        )
        if agents is None:
            self.agents = []
        else:
            self.agents = agents  # a list of agents names that are within the settlement
        # a list of infrastructure names that are within the settlement
        self.infrastructures = infrastructure
        self.max_population = max_population

        if boundery is not None:
            if boundery['type'] == 'circular':
                self.boundery = Circular(
                    center=self.pos,
                    radius=boundery['radius']
                )

    def add_agent(self, agent):
        """
        Add a single agent
        """
        if isinstance(agent, Agent) and agent.name not in self.agents:
            agent.settlement = self.name
            if not self.boundery.is_in(agent):
                agent.pos = self.pos
            self.agents.append(agent.name)

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

    def update(self, agents: list):
        self.find_all_agents_by_pos(agents)
        self.find_all_agents_by_settlement(agents)


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
    print(s.agents)
