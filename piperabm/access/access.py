from piperabm import Agent
from piperabm.search import find_element


class Access:

    def __init__(self, mode='all', name=None, all_agents=None):
        self.mode = mode
        self.name = name
        self.all_agents = all_agents

    def has_access(self, agent) -> bool:
        result = None
        if isinstance(agent, Agent):
            agent_name = agent.name
        elif isinstance(agent, str):
            agent_name = agent
        agent = find_element(agent_name, self.all_agents)
        if self.mode == 'all':
            result = True
        elif self.mode == 'none':
            result = False
        elif self.mode == 'members only':
            if agent.settlement == self.name:
                result = True
            else:
                result = False
        return result