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
        self.agents = agents
        self.settlements = settlements
        self.infrastructures = infrastructures

    def run_step(self):
        next_date = self.step_size + self.current_date
        next_step = self.current_step + 1
        self.update_elements_list(self.current_date, next_date)
        ### agens update internally
        ### settlements update internally
        ### agents look for other neighboring settlements source/demands to move
        self.current_step = next_step
        self.current_date = next_date

    def update_elements_list(self, start_date, end_date):
        for agent in self.agents:
            agent.is_active(start_date, end_date)
        for settlement in self.settlements:
            settlement.is_active(start_date, end_date)
        for infrastructure in self.infrastructures:
            infrastructure.is_active(start_date, end_date)


if __name__ == "__main__":
    from datetime import date

    from core.utils.unit_manager import Unit
    from settlement import Settlement


    settlements = []
    infrastructures = []

    m = Model(
        step_size=Unit(1, 'day'),
        current_step=0,
        current_date=date(2000, 1, 1),
        settlements=settlements,
        infrastructures = infrastructures,
        )

    m.run_step()
