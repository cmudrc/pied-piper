class Model():
    def __init__(
        self,
        step_size=None,
        current_step=0,
        current_date=None,
        settlements=None,
        infrastructures=None
    ):
        self.step_size = step_size
        self.current_step = current_step
        self.current_date = current_date
        self.settlements = settlements
        self.infrastructures = infrastructures

    def run_step(self):
        ### agens update internally
        ### settlements update internally
        ### agents look for other neighboring settlements source/demands to move
        self.current_step += 1
        self.current_date = self.step_size + self.current_date


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
