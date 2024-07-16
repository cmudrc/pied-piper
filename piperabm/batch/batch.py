from piperabm.model import Model


class Batch:

    def __init__(
            self,
            path,
            seed: int = None
        ):
        self.path = path
        self.seed = seed

    def create(
            self,
            populations,
            household_sizes
        ):
        pass

    