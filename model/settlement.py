from core.entity import Entity
from core.tools.boundery import Circular
from agent import Agent


class Settlement(Entity):
    """
    Represents a place where people interact with each other freely, e.g., village, group, city, etc. They are nodes of the graph, where edges are infrastructures.
    
    Args:
        name: name
        pos: position
        agents: a list of agents within the settlement
        max_population: maximum number of agents within the settlement
        boundery: the boundery of the settlement
    
    """

    def __init__(self, name, pos=[0, 0], agents=None, max_population=10, boundery=None):
        super().__init__(
            name=name,
            pos=pos
        )
        self.agents = agents
        self.max_population = max_population

        if boundery is not None:
            if boundery['type'] == 'circular':
                self.boundery = Circular(
                    center=self.pos,
                    radius=boundery['radius']
                )

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


if __name__ == "__main__":
    from agent import Human

    
    a_1 = Human(
        name='person_1',
        pos=[0.3, 0.4],
    )
    agents = [a_1]
    s = Settlement(
        name='city_1',
        pos=[0, 0],
        agents=agents,
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )