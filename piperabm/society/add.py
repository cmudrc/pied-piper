from copy import deepcopy

try: from .agent import Agent
except: from agent import Agent


class Add:
    """
    Contains methods for Society class
    Add new elements to the society
    """

    def add(self, agents):

        def add_single_agent(agent: Agent):
            index = self.find_next_index()
            self.index_list.append(index)
            self.G.add_node(
                index,
                agent=agent
            )

        if isinstance(agents, Agent):
            agents = [agents]
        if isinstance(agents, list):
            for agent in agents:
                add_single_agent(agent)
        
    def generate_agents(self, n, average_resource, average_income):
        
        def generate_agent(average_resource):
            wealth_factor = self.gini_gen.generate()
            agent = Agent(
                name=name_generator(),
                origin_node=self.env.random_settlement(),
                transportation=None, # default: Walk()
                queue=None, # default
                resource=resource_generator(wealth_factor, average_resource),
                idle_fuel_rate=None, # default: human_idle_fuel_rate
                balance=balance_generator(wealth_factor, average_income),
                wealth_factor=wealth_factor
            )
            return agent
        
        agents = []
        for _ in range(n):
            new_agent = generate_agent(average_resource)
            agents.append(new_agent)
        self.add(agents)


def name_generator():
    result = ''
    return result

def balance_generator(wealth_factor, average_income):
    return wealth_factor * average_income

def resource_generator(wealth_factor, average_resource):
    return average_resource * wealth_factor