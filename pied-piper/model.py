import networkx as nx
import matplotlib.pyplot as plt
from tools import dt


class Model():
    def __init__(
        self,
        step_size=None,
        current_step=0,
        current_date=None,
        agents=[],
        settlements=[],
        infrastructures=[]
    ):
        self.step_size = step_size
        self.current_step = current_step
        self.current_date = current_date

        self.all_agents = agents
        self.current_agents = self.all_agents.copy()

        self.all_settlements = settlements
        self.current_settlements = self.all_settlements.copy()

        self.all_infrastructures = infrastructures
        self.current_infrastructures = self.all_infrastructures.copy()

    def run_step(self):
        next_date = dt(seconds=self.step_size) + self.current_date
        next_step = self.current_step + 1
        #print(self.current_date, next_date)
        self.update_elements_list(
            start_date=self.current_date,
            end_date=next_date
        )
        ### agens update internally
        ### settlements update internally
        ### agents look for other neighboring settlements source/demands to move
        self.current_step = next_step
        self.current_date = next_date

    def update_elements_list(self, start_date, end_date):
        if self.current_step == 0:
            current_agents = []
            for agent in self.all_agents:
                activeness = agent.is_active(start_date, end_date)
                if activeness is True:
                    current_agents.append(agent)
            self.current_agents = current_agents

            current_infrastructures = []
            for infrastructure in self.all_infrastructures:
                activeness = infrastructure.is_active(start_date, end_date)
                if activeness is True:
                    current_infrastructures.append(infrastructure)
            self.current_infrastructures = current_infrastructures
        else:
            current_agents = []
            for agent in self.all_agents:
                activeness = agent.is_active(start_date, end_date)
                if activeness is True:
                    current_agents.append(agent)
            self.current_agents = current_agents

            current_infrastructures = []
            for infrastructure in self.all_infrastructures:
                activeness = infrastructure.is_active(start_date, end_date)
                if activeness is True:
                    current_infrastructures.append(infrastructure)
            self.current_infrastructures = current_infrastructures

    def find_element(self, element_name, all_elements):
        result = None
        for el in all_elements:
            if element_name == el.name:
                result = el
        return result

    def to_graph(self):
        G = nx.DiGraph()
        pos = {}
        for settlement in self.all_settlements:
            G.add_node(settlement.name)
            pos[settlement.name] = settlement.pos
        for route in self.routes:
            G.add_edge(route.start_node, route.end_node)
        nx.draw(G, pos)
        plt.show()

if __name__ == "__main__":
    from datetime import date

    from tools import Unit
    from infrastructure import Road
    from settlement import Settlement
    from agent import Agent


    agents = [
        Agent(
            name='John',
            pos=[1, 1],
            settlement='home_1'
        ),
        Agent(
            name='Betty',
            pos=[0.5, 0.5]
        )
    ]
    settlements = [
        Settlement(
            name='home_1',
            pos=[0, 0],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        ),
        Settlement(
            name='home_2',
            pos=[0, 2],
            max_population=10,
            boundery={
                'type': 'circular',
                'radius': 1
            }
        ),
    ]
    infrastructures = [
        Road(
            start_node='home_1',
            end_node='home_2',
            double_sided=True,
            name='sample road',
            initiation_date=date(2000, 1, 1),
            distribution={
                'type': 'dirac delta',
                'main': Unit(10, 'day'),
            },
            seed=None
        )
    ]

    m = Model(
        step_size=Unit(5, 'day').to_SI(),
        current_step=0,
        current_date=date(2000, 1, 1),
        agents=agents,
        settlements=settlements,
        infrastructures=infrastructures,
    )
    #m.to_graph()
    #print(m.current_infrastructures)
    #m.run_step()
    #print(m.current_infrastructures)
