class Model():
    def __init__(
        self,
        step_size=None,
        settlements=None,
        infrastructures=None
    ):
        self.step_size = step_size
        self.settlements = settlements
        self.infrastructures = infrastructures

    def run_step(self):
        pass


if __name__ == "__main__":
    from datetime import timedelta
    from settlement import Settlement


    settlements = []
    infrastructures = []

    m = Model(
        step_size=timedelta(days=1),
        settlements=settlements,
        infrastructures = infrastructures,
        )

    m.run_step()
