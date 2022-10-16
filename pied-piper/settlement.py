from tools import Entity
from tools.boundery import Circular
from agent import Agent


class Settlement(Entity):
    """
    Represents a place where people interact with each other freely, e.g., village, group, city, etc. They are nodes of the graph, where edges are infrastructures.
    """

    def __init__(
        self,
        name=None,
        pos=[0, 0],
        max_population=10,
        boundery=None,
        active=True,
        initial_cost=None,
        initiation_date=None,
        distribution=None,
        seed=None
        ):
        """
        Args:
            name: name
            pos: position in form of [x, y]
            max_population: maximum number of agents within the settlement
            boundery: the boundery of the settlement
            ** others from Entity class
        """

        super().__init__(
            name=name,
            pos=pos,
            active=active,
            initial_cost=initial_cost,
            initiation_date=initiation_date,
            distribution=distribution,
            seed=seed
        )
        self.agents = [] # a list of agents names that are within the settlement
        self.infrastructures = [] # a list of infrastructure names that are within the settlement
        self.max_population = max_population

        if boundery is not None:
            if boundery['type'] == 'circular':
                self.boundery = Circular(
                    center=self.pos,
                    radius=boundery['radius']
                )
    
    def find_element(self, name, all_elements):
        """
        Find an element between a list of elements based on its name property
        """

        result = None
        for element in all_elements:
            if element.name == name:
                result = element
                break
        return result

    def add_agent(self, agent):
        """
        Add a single agent
        """

        if isinstance(agent, Agent):
            agent.pos = self.pos
            self.agents.append(agent.name)

    def add_agents(self, agents: list):
        """
        Add a list of agents
        """

        for agent in agents:
            self.add_agent(agent)

    def all_sources(self, all_agents):
        result = {}
        for ag in self.agents:
            agent = self.find(ag, all_agents)
            

    '''
    def add_agent(self, agent):
        if isinstance(agent, Agent):
            if self.distance(agent) <= self.boundery['radius']:
                if self.max_population is not None:
                    if self.max_population >= len(self.agents) + 1:
                        agent.settlement = self.name
                        self.agents.append(agent)
                    else:
                        agent.pos = [self.pos[0] + self.boundery.radius, self.pos[1]]
                else:
                    agent.settlement = self.name
                    self.agents.append(agent)


    def find_all_agents(self, all_agents):
        for agent in all_agents:
            self.add_agent(agent)
    '''

if __name__ == "__main__":
    from agent import Human

    '''
    a_1 = Human(
        name='person_1',
        pos=[0.3, 0.4],
    )
    agents = [a_1]'''
    agents = ['John', 'Betty']
    s = Settlement(
        name='home_1',
        pos=[0, 0],
        agents=agents,
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )