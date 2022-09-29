from core.entity import Entity
from core.tools.boundery import Circular
from agent import Agent


class Settlement(Entity):
    def __init__(self, name, pos=[0, 0], agents=None, max_population=10, boundery=None):
        super().__init__(Entity(
            name=name,
            pos=pos
        ))
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
                self.agents.append(agent)


if __name__ == "__main__":
    s = Settlement(
        name='city_1',
        pos=[0, 0],
        max_population=10,
        boundery={
            'type': 'circular',
            'radius': 1
        }
    )