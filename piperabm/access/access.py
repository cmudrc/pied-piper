from piperabm import Agent
from piperabm.search import find_element


class Access:

    def __init__(self, mode='all', all_agents=None):
        self.mode = mode

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