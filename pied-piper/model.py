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
        next_date = self.step_size + self.current_date
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
            self.current_agents = []
            for agent in self.all_agents:
                if agent.is_active(start_date, end_date):
                    self.current_agents.append(agent)

            self.current_infrastructures = []
            for infrastructure in self.all_infrastructures:
                if infrastructure.is_active(start_date, end_date):
                    self.current_infrastructures.append(infrastructure)


if __name__ == "__main__":
    from datetime import date

    from tools import Unit
    from infrastructure import Road

    agents = []
    settlements = []
    infrastructures = [
        Road(
            start_node='city_1',
            end_node='city_2',
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
        step_size=Unit(5, 'day'),
        current_step=0,
        current_date=date(2000, 1, 1),
        agents=agents,
        settlements=settlements,
        infrastructures=infrastructures,
    )

    print(m.current_infrastructures)
    m.run_step()
    print(m.current_infrastructures)
